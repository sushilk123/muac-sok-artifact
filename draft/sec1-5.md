# 1. Introduction

AI agents are moving from single-vendor pipelines into shared, multi-organizational environments. A data-steward agent operated by one organization may run on one vendor's model, while an analytics agent operated by a partner runs on another's, and the two must jointly operate over a shared cloud data ecosystem. To do so they must discover what each other can do, negotiate access to datasets and compute, delegate sub-tasks under appropriate authority, and resolve conflicts over matters such as retention policies, schema changes, or budget allocations. They must accomplish all of this without having been trained together, without a shared reward, and without their principals fully trusting one another.

This setting combines three difficulties that the literature has largely studied in isolation.

**Independently trained agents coordinate poorly.** The ad hoc teamwork (AHT) and zero-shot coordination (ZSC) communities have spent more than a decade formalizing collaboration "without pre-coordination" [@stone2010adhoc; @mirsky2022survey; @hu2020otherplay]. Recent evidence shows that frontier LLM agents built by different providers also fail to coordinate in minimal ZSC settings, partly because they reason poorly about partner behaviour [@hayler2026zsc].

**Today's interoperability protocols assume a single controlling principal.** The Model Context Protocol (MCP) [@anthropic2024mcp] and Agent2Agent (A2A) [@google2025a2a] standardize how an agent reaches tools and other agents. As @qian2026mpac argue, however, both assume a single controlling principal, and neither expresses voting, dissent, or escalation [@kang2026governance].

**Inter-agent channels are an attack surface.** Prompt injection propagates from agent to agent [@lee2024prompt; @an2026aciarena], agent protocols admit systematic attacks [@lotfi2026a2abreak], and delegated authority is easily over-provisioned [@south2025authenticated; @veski2026capmas].

We call the resulting problem **Mutually Untrusting Ad Hoc Coordination (MUAC)**: independently developed agents, acting for distinct principals with partially conflicting interests, must coordinate, negotiate, delegate, and resolve conflicts in a shared, security-sensitive environment, with no prior joint training or alignment. MUAC sits at the intersection of four research communities that rarely cite one another: (i) ad hoc teamwork and zero-shot coordination; (ii) automated negotiation; (iii) agent interoperability protocols; and (iv) multi-agent security, identity, and delegation. Each community has mature results along its own axis. None, as we show, addresses the combination.

This paper is a systematization of knowledge (SoK) for MUAC. Our contributions are as follows.

- **C1. Problem formalization.** We define the MUAC setting precisely (§3.1), distinguishing it from cooperative multi-agent learning, single-principal orchestration, and classical open multi-agent systems. We build on the cross-domain framings of @ko2026sevenchallenges and @yang2026soksafeagents, adding coordination requirements to their security focus.
- **C2. Threat model.** We give a MUAC-specific threat model (§3.2) with five adversary classes, ranging from honest-but-curious peers to prompt-subverted and colluding agents.
- **C3. Requirements and taxonomy.** We derive eight requirements (R1–R8) that a MUAC solution must satisfy (§4) and a four-axis taxonomy (§5) covering coordination mechanism, trust assumption, authorization model, and evaluation regime.
- **C4. Systematization.** We code 85 works and protocols from all four communities, selected by the protocol in §2, against R1–R8 and taxonomy Axes B and D (§6–§7).
- **C5. Gap analysis and agenda.** We identify structural gaps (§7), most prominently that no surveyed work jointly demonstrates coordination with unseen partners (R1) and robustness to adversarial peers (R8), and we outline a research agenda, including a benchmark design, for closing them (§9).
- **C6. Pilot study.** We report an illustrative cross-vendor pilot of data-access negotiation that measures coordination and security outcomes in the same episodes (§8).

**Scope.** We focus on agents whose behaviour is driven primarily by large language models (LLMs), since these dominate current deployments and protocols, and include reinforcement-learning AHT/ZSC work where it supplies the formal foundations for coordination without joint training. Secure cloud data ecosystems serve as the running application: multi-tenant data platforms, data spaces, and cross-organizational analytics environments, in which coordination failures translate directly into data exposure, policy violations, or wasted resources.

# 2. Systematization Methodology

**Sources and search.** We searched arXiv, Google Scholar, the ACL Anthology, and OpenReview, and resolved venues through Crossref and OpenAlex. We complemented these sources with official protocol documentation (MCP, A2A, ACP, ANP) and with backward and forward citation chasing from five seed works [@stone2010adhoc; @hu2020otherplay; @qian2026mpac; @veski2026capmas; @hammond2025multiagent]. Search strings combined terms from four concept groups—(1) *ad hoc teamwork, zero-shot coordination, cross-play*; (2) *negotiation, bargaining, contract net*; (3) *agent protocol, interoperability, MCP, A2A*; and (4) *delegation, authorization, least privilege, prompt injection, agent identity*—each combined with *LLM agent* or *multi-agent*. The window spans 2010 to October 2026; seminal earlier work, such as the Contract Net Protocol [@smith1980contractnet], is included where it defines concepts still in use.

**Inclusion and exclusion.** A work is included if it addresses at least one of the following: coordination with partners not encountered during training, inter-agent negotiation, inter-agent delegation or authorization, inter-agent conflict resolution, or the security of inter-agent communication. We exclude single-agent tool-use work with no inter-agent interaction, and multi-agent learning that assumes joint training and reports no evaluation with novel partners.

**Coding.** Each included work is coded against requirements R1–R8 (§4) as fully supported (●), partially supported (◐), or not addressed (○), and against taxonomy Axes B and D (§5); Axes A and C are recorded in the released coding files. Where two versions of a work exist, such as a workshop paper and its extended arXiv version, we code a single entry. Codes are grounded in each work's own text: a requirement is marked ● only when the work both addresses it and provides empirical or formal evidence. The two most consequential codes follow stricter rules. R1 (coordination without joint training) is marked ● only when a work evaluates with independently trained or independently developed partners (cross-play); work designed for such partners but evaluated only in self-play receives ◐. R8 (adversarial robustness) is marked ● only when malicious, compromised, or subverted peers are evaluated empirically or analyzed formally. Surveys receive ◐ for requirements they discuss systematically, but never ●.

**Limitations of the method.** Coding is necessarily interpretive. It was performed in a single pass by one coder, without inter-rater agreement, and 73 of the 85 works were coded from abstracts and official pages rather than full text. We coded conservatively: absence of evidence in a work's text yields ○ even when its mechanism could plausibly be extended. Because the field moves quickly, our October 2026 snapshot will age; we therefore release the full coding table (Appendix A) so that others can update and contest individual codes.

# 3. Problem Setting and Threat Model

## 3.1 Mutually Untrusting Ad Hoc Coordination

A MUAC instance consists of a shared environment $\mathcal{E}$ and a set of agents $A = \{a_1, \dots, a_n\}$.

**Agents.** Each agent $a_i$ is characterized by four elements. Its **principal** $p_i$ is the organization or user on whose behalf it acts and to whom it is accountable; distinct agents may have distinct principals, whose objectives $u_{p_i}$ may partially conflict. Its **policy** $\pi_i$ is produced by an independent development process—a different model vendor, training run, prompting scaffold, or agent framework—and no agent has access to another's policy, training data, or reward. Its **capability set** $K_i$ comprises the actions and tools it can invoke; it advertises a **claimed** capability set $\hat{K}_i$ to others, and in general $\hat{K}_i \neq K_i$. Finally, its **credential set** $C_i$ is the authority it holds in $\mathcal{E}$, granted by $p_i$ through the environment's access-control layer.

**Environment.** $\mathcal{E}$ comprises resources $R$ (datasets, storage, compute, pipelines), an access-control layer $\mathcal{G}$ (identity, authorization, key management, audit logging), and a set of governance policies $\Phi$ (data usage, retention, residency, budget) that constrain which actions are permitted.

**Interaction.** Agents interact only through a communication protocol $\mathcal{P}$, which may be free-form natural language, a structured protocol such as A2A or MPAC, or a hybrid. A MUAC episode is a sequence of five interaction types: *discovery*, learning $\hat{K}_j$ and, ideally, evidence about $K_j$; *negotiation*, reaching an agreement $\alpha$ over resources, terms, or task allocation; *delegation*, in which $a_i$ transfers a subset of its authority $C' \subseteq C_i$ to $a_j$ to perform a task; *joint execution* over $R$; and *conflict resolution*, detecting and resolving incompatible intents, actions, or policy interpretations.

**What distinguishes MUAC.** Four properties hold *simultaneously*:

- **(i) No joint training.** Agents were not co-trained and share no conventions beyond $\mathcal{P}$—the standard ZSC/AHT condition [@stone2010adhoc; @hu2020otherplay].
- **(ii) Multiple principals.** Agents represent different principals with partially conflicting objectives, ruling out the single-principal orchestration assumed by most LLM multi-agent frameworks [@wu2023autogen; @hong2023metagpt; @fourney2024magenticone].
- **(iii) Bounded trust.** No agent's model or claims are trusted by default; only the environment's access-control layer $\mathcal{G}$ is trusted.
- **(iv) Consequential actions.** Actions in $\mathcal{E}$ affect real data and authority, so coordination failures carry security and compliance costs, not merely lost reward.

Classical open multi-agent systems research addressed (ii) and (iii) with symbolic agents and hand-designed protocols [@smith1980contractnet; @fipa2002acl]. Ad hoc teamwork addressed (i), typically for fully cooperative teams. MUAC requires all four properties for agents whose behaviour is driven by learned language models and is therefore not formally specifiable.

**Desired outcomes.** A MUAC solution should be *efficient*, reaching agreements and completing tasks with high joint utility; *safe*, never violating $\Phi$ and never granting authority beyond what an agreement requires; and *accountable*, leaving a verifiable record of who agreed to, delegated, and executed what. These properties should hold even when some agents are adversarial.

## 3.2 Threat Model

**Trust assumptions.** We trust the environment's access-control layer $\mathcal{G}$: cloud identity and authorization services, key management, attestation services where present, and append-only audit logs. We do not trust any agent's model weights, prompts, outputs, or self-reported capabilities. Principals are trusted to state their own policies, but not to be disinterested toward one another.

**Adversary classes.** We distinguish five classes of adversarial peer.

- **T1 — Malicious or compromised peer.** An agent whose principal is adversarial, or whose runtime has been compromised. It may lie, deviate from agreements, or attempt to escalate privileges.
- **T2 — Subverted honest peer.** An agent with an honest principal whose behaviour is hijacked through content it processes, such as indirect prompt injection in data or in messages from other agents; such subversion can propagate across agents [@lee2024prompt; @an2026aciarena]. T2 is particularly important because it turns any peer, including one's own delegate, into a potential adversary.
- **T3 — Misrepresenting peer.** An agent that misstates its identity or capabilities ($\hat{K}_i \neq K_i$), for example through spoofed agent descriptors [@habler2025securea2a; @lotfi2026a2abreak].
- **T4 — Colluding coalition.** Multiple agents coordinating covertly against other principals, for example to extract data or bias an arbitration outcome [@hammond2025multiagent; @motwani2024collusion].
- **T5 — Honest-but-curious peer.** An agent that follows the protocol but attempts to learn more than the agreement permits, for example by inferring sensitive attributes from shared intermediate results.

**Assets and scope.** The assets at risk are data confidentiality and integrity, credentials and delegated privileges, compute and storage budgets, the integrity of the governance policies $\Phi$, and the integrity and completeness of the audit trail. We exclude compromise of the trusted layer $\mathcal{G}$ itself, network-layer denial of service, and attacks on model training pipelines such as poisoning of base models; these are well studied elsewhere and orthogonal to coordination.

# 4. Requirements Framework

From the problem setting and threat model we derive eight requirements, each stated as the question we asked of every surveyed work.

- **R1 — Coordination without joint training.** Does the approach coordinate effectively with partners it was not trained or designed alongside, including partners built on other vendors' models, and is this demonstrated in cross-play rather than only in self-play? *(Property (i).)*
- **R2 — Verifiable capability discovery.** Can an agent discover what a peer can do *and* obtain evidence that the claim is true, for example through attestation, capability-bound credentials, or reputation? *(T3.)*
- **R3 — Structured negotiation.** Does the approach provide explicit negotiation semantics—offers, counter-offers, acceptance, binding agreements—with bounded rounds or termination? *(Property (ii).)*
- **R4 — Least-privilege delegation.** Is delegated authority scoped to the agreed task, time-bounded, and attenuating, so that a delegate can only narrow and never widen it, and is it enforced by $\mathcal{G}$ rather than by agent goodwill? *(T1, T2.)*
- **R5 — Conflict detection and resolution.** Are conflicts between intents, actions, or policy interpretations represented explicitly and resolved by a mechanism with defined outcomes (arbitration, voting, precedence rules) and guarantees such as termination or freedom from deadlock?
- **R6 — Human oversight and escalation.** Is there a defined condition and channel for escalating decisions to human principals, and for principals to override?
- **R7 — Auditability and accountability.** Does the approach produce a tamper-evident record of discovery, agreements, delegations, and actions, attributable to principals? *(Property (iv).)*
- **R8 — Adversarial robustness.** Is the approach evaluated empirically or analyzed formally against malicious, subverted, misrepresenting, colluding, or curious peers (T1–T5)?

The requirements fall into three groups. R1, R3, and R5 concern *coordination quality*, the traditional focus of the multi-agent and negotiation communities. R2, R4, R7, and R8 concern *security*, the traditional focus of the systems-security community. R6 concerns *governance*, increasingly emphasized in AI safety work [@hammond2025multiagent; @tomasev2026intelligent]. Our central claim, tested in §7, is that existing work achieves full support within at most one group.

# 5. Taxonomy

We organize approaches along four orthogonal axes, summarized in Table 1.

**Table 1. Four-axis taxonomy of approaches to coordination among independently developed agents.**

| Axis | Values |
|---|---|
| A. Coordination mechanism | A1 learned conventions [@hu2020otherplay; @strouse2021fcp; @wang2024naht]; A2 language-mediated [@zhang2024proagent; @agashe2023llmcoord]; A3 protocol-mediated [@smith1980contractnet; @google2025a2a; @qian2026mpac]; A4 market or mechanism-based [@bansal2025marketplace; @tomasev2025virtual] |
| B. Trust assumption | B1 single principal; B2 multiple cooperative principals; B3 multiple mutually untrusting principals (MUAC) |
| C. Authorization model | C0 not addressed; C1 identity pass-through; C2 centralized authorization (e.g., OAuth token exchange); C3 capability-based with attenuation [@veski2026capmas]; C4 decentralized identity or ledger-based [@zou2025blocka2a] |
| D. Evaluation regime | D0 none (specification or position); D1 self-play only; D2 cross-play within a model family; D3 cross-vendor or cross-developer; D4 adversarial; D5 human-in-the-loop |

*Coordination mechanism* (Axis A) distinguishes policies trained to be robust to diverse partners (A1) from LLM agents that coordinate through dialogue (A2), coordination through typed messages and state machines (A3), and coordination through prices, auctions, or incentive-compatible mechanisms (A4). *Trust assumption* (Axis B) distinguishes systems in which all agents serve one owner, as in most LLM multi-agent frameworks (B1), from teams of distinct but aligned owners, as in ad hoc teamwork (B2), and from the MUAC setting (B3). *Authorization model* (Axis C) ranges from acting with the user's full identity (C1) through per-request checks against an IAM service (C2) to bearer capabilities that can only be attenuated (C3) and decentralized identifiers, verifiable credentials, or ledgers (C4). *Evaluation regime* (Axis D) records how a work's claims were tested; a work may occupy several values.

The taxonomy makes MUAC's demands explicit: a MUAC-complete approach must operate at **B3**, should use **C3 or C4** authorization enforced by the trusted layer, and must be evaluated at least at **D3 and D4**.
