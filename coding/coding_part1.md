# Coding — Part 1 (outline §6.1–6.3)

Coder pass 1, 2026-10-09. Source = abstracts only (arXiv API, Crossref, NeurIPS proceedings page, Google Scholar snippets). FIPA ACL is excluded per instructions.
Legend: ● full / ◐ partial / ○ none. "n.a.a." = not addressed in abstract.

Rubric as applied:
- **R1**: ● = the abstract reports evaluation with unseen or independently trained partners (cross-play, held-out populations, other models, or humans). ◐ = the work is designed for unseen partners, but the abstract reports no such evaluation, or only implies it.
- **R2**: ◐ = the agent infers partner type or behaviour from observation (this is not capability verification). ● = cryptographic or attested verification. No work received ●.
- **R3**: ● requires offers, counteroffers, agreement semantics, and bounded rounds all stated. Natural-language negotiation games get ◐ when bounded rounds are not stated.
- **R4**: covers rights or privilege delegation only. Delegating a task without scoping rights is coded ○.
- **R8**: ● = malicious, adversarial, or manipulative peers are evaluated. ◐ = only self-interested or defecting peers are evaluated (mixed-motive), or only exploitative tactics are studied.
- **Flagged**: rows marked † were coded from a Google Scholar snippet or partial abstract because OpenReview or IEEE blocked automated access. Verify these against the full text.

## Table

| Key | Work | Year | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | A (mechanism) | B (trust) | C (authz) | D (evaluation) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stone2010adhoc | Ad Hoc Autonomous Agent Teams | 2010 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (AHT problem def.) | multiple cooperative principals | n/a | none (position paper; proposes eval paradigm) |
| mirsky2022survey | Survey of Ad Hoc Teamwork Research | 2022 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (AHT) | multiple cooperative principals | n/a | n/a (survey) |
| hu2020otherplay | Other-Play | 2020 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (ZSC) | multiple cooperative principals | n/a | cross-play (independently trained) + human-in-the-loop |
| carroll2019overcooked | Overcooked-AI (Utility of Learning about Humans) | 2019 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions | multiple cooperative principals (human–AI) | n/a | self-play vs. human model + human-in-the-loop |
| strouse2021fcp | Fictitious Co-Play | 2021 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (ZSC) | multiple cooperative principals (human–AI) | n/a | cross-play (novel agents) + human-in-the-loop |
| wang2024naht | N-Agent Ad Hoc Teamwork (POAM) | 2024 | ● | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (NAHT) | multiple cooperative principals | n/a | cross-play (OOD unseen teammates) |
| wang2025matnaht | Sequence Modeling for NAHT (MAT-NAHT) | 2025 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (NAHT) | multiple cooperative principals | n/a | cross-play (unseen teammates) |
| wang2025shapley | Shapley Machine for NAHT | 2025 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (NAHT, coop. game theory) | multiple cooperative principals | n/a | unclear from abstract |
| bard2020hanabi | The Hanabi Challenge | 2019 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions | multiple cooperative principals | n/a | self-play; ad hoc framework proposed |
| zhang2024proagent | ProAgent | 2023 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (LLM planning) | multiple cooperative principals | n/a | cross-play (AI partners) + human proxy models |
| agashe2023llmcoord | LLM-Coordination | 2023 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated | multiple cooperative principals | n/a | cross-play (ZSC experiments) |
| shi2023avalon | Cooperation on the Fly (Avalon AHT) | 2023 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated | multiple cooperative principals | n/a | unclear from abstract |
| liu2024heteroaht | LLM for Heterogeneous AHT Collaboration | 2024 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (LLM planner) | multiple cooperative principals | n/a | benchmark with varied teams + physical robots |
| wallace2025recollab | ReCollab | 2025 | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (LLM teammate modeling) | multiple cooperative principals | n/a | teammate types in Overcooked (protocol unclear) |
| hayler2026zsc | Zero-Shot Coordination among LLM Agents | 2026 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated | multiple cooperative principals | n/a | cross-play across 5 vendors (XP_LLM) + XP_seed (full text read) |
| qu2026riskaversion | Strategic Risk Aversion | 2026 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (MARL; incl. LLM task) | multiple cooperative principals | n/a | cross-play (unseen, heterogeneous partners) |
| smith1980contractnet † | Contract Net Protocol | 1980 | ○ | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | protocol-mediated | single principal (distributed problem solver) | n/a | none in abstract |
| lewis2017dealnodeal | Deal or No Deal? | 2017 | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | language-mediated (learned dialogue) | multiple self-interested principals | n/a | unclear from abstract (human–human data) |
| fair2022cicero | CICERO (Diplomacy) | 2022 | ● | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | language-mediated + strategic planning | multiple mutually untrusting (mixed-motive) | n/a | human-in-the-loop (anonymous online league) |
| bianchi2024negotiationarena | NegotiationArena | 2024 | ◐ | ○ | ◐ | ○ | ○ | ○ | ○ | ◐ | language-mediated | multiple self-interested principals | n/a | cross-model (implied, e.g. vs GPT-4) |
| abdelnabi2024stakeholders | LLM-Stakeholders Interactive Negotiation | 2023 | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ● | language-mediated | multiple mutually untrusting (mixed-motive) | n/a | adversarial (greedy/adversarial players, attacks) |
| davidson2024agency | Evaluating LM Agency through Negotiations | 2024 | ● | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | language-mediated | multiple self-interested principals | n/a | self-play + cross-play across six LMs (cross-vendor) |
| bansal2025marketplace | Magentic Marketplace | 2025 | ◐ | ○ | ◐ | ○ | ○ | ○ | ○ | ● | market / mechanism design (LLM agents) | multiple mutually untrusting (consumers vs. businesses) | n/a | adversarial (manipulation); multiple frontier models |
| qu2026bgt † | Behavioral Game Theory for Collaborative LLM Agents | 2026 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (SRPO; LLM debate) | multiple cooperative principals | n/a | cross-play (GSM8K debate) |
| wu2023autogen | AutoGen | 2023 | ○ | ○ | ○ | ○ | ○ | ◐ | ○ | ○ | language-mediated (conversation programming) | single principal | n/a | single-system application benchmarks |
| li2023camel | CAMEL | 2023 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (role-playing) | single principal | n/a | self-play (role-play) |
| hong2023metagpt | MetaGPT | 2023 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (SOP workflows) | single principal | n/a | single-system benchmarks |
| fourney2024magenticone | Magentic-One | 2024 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (orchestrator) | single principal | n/a | single-system benchmarks (GAIA, AssistantBench, WebArena) |
| zhu2025multiagentbench | MultiAgentBench | 2025 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | language-mediated (topologies) | single principal (collab. + competition scenarios) | n/a | self-play (per-model teams) |
| shao2024cogym | Collaborative Gym | 2024 | ● | ○ | ○ | ○ | ○ | ◐ | ○ | ○ | language-mediated (human–agent) | single principal (human user + agent) | n/a | human-in-the-loop (simulated + real users) |
| leibo2021meltingpot | Melting Pot | 2021 | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | learned conventions (MARL) | multiple mutually untrusting (mixed-motive social dilemmas) | n/a | cross-play (novel test scenarios / co-players) |
| vezhnevets2023concordia | Concordia | 2023 | ○ | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | language-mediated (GABM; Game Master) | n/a (simulation library) | n/a | n/a (library) |
| smith2025concordiagen | Concordia generalization (NeurIPS 2025 D&B) | 2025 | ● | ○ | ◐ | ○ | ○ | ○ | ○ | ◐ | language-mediated | multiple mutually untrusting (mixed-motive) | n/a | cross-play (contest; zero-shot, diverse partners) |
| tewolde2026coopeval | CoopEval | 2026 | ◐ | ○ | ◐ | ○ | ◐ | ○ | ○ | ◐ | market / mechanism design (repetition, reputation, mediation, contracts) | multiple mutually untrusting (mixed-motive) | n/a | varied co-players; evolutionary pressure |
| cemri2025mast | MAST failure taxonomy | 2025 | ○ | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | language-mediated (7 MAS frameworks analysed) | single principal | n/a | n/a (trace analysis) |
| kaliyev2026noisefloor | Paired Noise-Floor Protocol | 2026 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | protocol-mediated substrate (MCP-conformant store) | single principal | n/a | self-play (single model, Claude Haiku 4.5) |

## Per-work justifications

### stone2010adhoc: Stone, Kaminka, Kraus, Rosenschein (AAAI 2010)
- R1 ◐: defines collaboration "without pre-coordination" and an evaluation paradigm, but runs no evaluation.
- R2–R8 ○: n.a.a.
- A/B/C/D: AHT problem with cooperative teammates of unknown origin. Position paper with no experiments.

### mirsky2022survey: Mirsky et al. (EUMAS 2022)
- R1 ◐: surveys collaboration with new teammates without prior coordination. As a survey it has no evaluation of its own.
- R2–R8 ○: n.a.a.

### hu2020otherplay: Hu, Lerer, Peysakhovich, Foerster
- R1 ●: in Hanabi, scores higher when paired with independently trained agents and with humans.
- R2–R8 ○: n.a.a.
- D: cross-play with independently trained agents, plus preliminary human pairing.

### carroll2019overcooked: Carroll et al. (NeurIPS 2019)
- R1 ●: agents evaluated with a learned human model and in a real-human user study.
- R2–R8 ○: n.a.a.
- D: self-play/PBT agents vs. human model; user study.

### strouse2021fcp: Strouse et al. (NeurIPS 2021)
- R1 ●: FCP scores higher than baselines with novel agent and human partners.
- R2–R8 ○: n.a.a.

### wang2024naht: Wang, Rahman, Durugkar, Liebman, Stone (NeurIPS 2024)
- R1 ●: POAM shows out-of-distribution generalization to unseen teammates. The setup is motivated by cars from different companies cooperating.
- R2 ◐: learns representations of teammate behaviours (behavioural inference, not capability verification).
- R3–R8 ○: n.a.a.
- B: explicitly multi-company, but all parties are cooperative.

### wang2025matnaht: Wang et al. (RLDM 2025)
- R1 ●: transformer method generalizes to "diverse and unseen teammates" (StarCraft II).
- R2–R8 ○: n.a.a.

### wang2025shapley: Wang, Li, Kaski, Lawry
- R1 ◐: targets NAHT, but the abstract does not state an unseen-teammate evaluation.
- R2–R8 ○: n.a.a. (Shapley values here are for credit assignment, not conflict resolution).

### bard2020hanabi: Bard et al. (Artificial Intelligence 280, 2020)
- R1 ◐: proposes an evaluation framework and stresses human partners. The abstract reports only current state-of-the-art results.
- R2–R8 ○: n.a.a.

### zhang2024proagent: Zhang et al. (AAAI 2024)
- R1 ●: outperforms self-play and population-based training baselines with unfamiliar AI agents and human proxy models (Overcooked-AI).
- R2 ○: infers teammates' intentions, not their capabilities.
- R3–R8 ○: n.a.a.

### agashe2023llmcoord: Agashe, Fan, Reyna, Wang
- R1 ●: ZSC experiments show that LLM agents are robust to unseen partners.
- R2–R8 ○: n.a.a.

### shi2023avalon: Shi et al.
- R1 ◐: frames the problem as ad hoc teamwork with new teammates. The abstract states no unseen-partner evaluation protocol.
- R2–R7 ○: n.a.a.
- R8 ○: Avalon has hidden adversarial roles, but the abstract does not address adversaries.

### liu2024heteroaht: Liu et al.
- R1 ◐: works with unknown heterogeneous teammates. The abstract does not specify whether the evaluation teams are unseen.
- R2–R8 ○: n.a.a.

### wallace2025recollab: Wallace, Siddique, Cao
- R1 ◐: designed for previously unseen teammates. The evaluation protocol for teammate types is unclear.
- R2 ◐: classifies partner types from behavioural traces (inference, not verification).
- R3–R8 ○: n.a.a.

### hayler2026zsc †: Hayler et al. (2026 workshop)
- R1 ◐: studies ZSC among LLM agents and finds that frontier LLMs fail to coordinate. The snippet does not confirm a cross-play protocol. Verify in the PDF; upgrade to ● if cross-play is confirmed.
- R2–R8 ○: n.a.a. (from the snippet).

### qu2026riskaversion: Qu, Zhang, Lanzetti, Mazumdar
- R1 ●: reliable collaboration with heterogeneous, previously unseen partners, including an LLM task.
- R2–R7 ○: n.a.a.
- R8 ○: robust to partner deviations, which is not the same as malicious peers.

### smith1980contractnet †: Smith (IEEE TC 1980)
- Only a partial abstract was available (Scholar snippet). The IEEE page was blocked.
- R1 ○: n.a.a.
- R2 ◐: nodes bid on announced tasks, so capability is claimed in the bid, not verified. (Based on the protocol's well-known announce/bid/award design. Confirm in the full text.)
- R3 ◐: negotiation-based task distribution via announcement, bid, and award. There are no counteroffers.
- R4–R8 ○: n.a.a. Task contracting is not rights delegation.

### lewis2017dealnodeal: Lewis et al.
- R1 ○: n.a.a.
- R3 ◐: multi-issue bargaining that reaches a deal via natural language. Bounded rounds are not stated.
- Others ○: n.a.a.

### fair2022cicero: Meta FAIR Diplomacy Team et al. (Science 2022)
- R1 ●: human-level play against unseen humans in 40 anonymous online league games.
- R3 ◐: natural-language negotiation within Diplomacy. There are no formal offer or agreement semantics.
- R8 ○: n.a.a. (Diplomacy is mixed-motive, but the abstract does not evaluate adversaries).

### bianchi2024negotiationarena: Bianchi et al.
- R1 ◐: LLMs negotiate with one another, e.g. against GPT-4. Cross-model pairing is implied, not systematic.
- R3 ◐: ultimatum, trading, and price negotiation over multiple turns. Formal semantics are not stated.
- R8 ◐: deceptive tactics such as feigning desperation exploit opponents. These are tactics, not attacks.

### abdelnabi2024stakeholders: Abdelnabi et al.
- R1 ○: cross-model pairing n.a.a.
- R3 ◐: scorable multi-issue, multi-party negotiation games with an agreement target.
- R8 ●: evaluates greedy and adversarial players. The updated version adds attacks.

### davidson2024agency: Davidson et al. (ICLR 2024)
- R1 ●: evaluates six LMs in both self-play and cross-play.
- R3 ◐: negotiation games. Offer and round structure are not stated in the abstract.
- Others ○: n.a.a.

### bansal2025marketplace: Bansal et al.
- R1 ◐: agents with opaque behaviours from multiple frontier models. Cross-model pairing is not explicit.
- R3 ◐: proposals and transactions between agents (it reports first-proposal bias).
- R7 ○: motivated by agent accountability, but no audit mechanism is described.
- R8 ●: studies vulnerability to manipulation in two-sided markets.

### qu2026bgt †: Qu et al. (COLM 2026 workshop)
- R1 ●: SRPO improves cross-play accuracy in multi-agent LLM debate (GSM8K).
- Others ○: n.a.a.
- This appears to be a workshop version of qu2026riskaversion (same authors and method). Consider merging the two rows.

### wu2023autogen: Wu et al.
- R6 ◐: agents can operate with human inputs. There is no defined escalation protocol.
- Others ○: n.a.a.

### li2023camel: Li et al. (NeurIPS 2023)
- All ○: role-playing for autonomous cooperation within one framework. It aims to reduce human input.

### hong2023metagpt: Hong et al.
- All ○: SOP-encoded roles verify intermediate results. This is quality control within a single principal's system.

### fourney2024magenticone: Fourney et al.
- All ○: the orchestrator delegates tasks and re-plans on errors. There is no rights scoping and no inter-principal setting.

### zhu2025multiagentbench: Zhu et al.
- All ○: evaluates collaboration and competition across coordination topologies. Cross-model, security, and negotiation aspects are n.a.a.

### shao2024cogym: Shao et al. (ICLR 2026)
- R1 ●: agents are evaluated with real users, who are unseen partners.
- R6 ◐: human–agent collaboration that preserves human control. This is not escalation between agents.
- Others ○: n.a.a.

### leibo2021meltingpot: Leibo et al. (ICML 2021)
- R1 ●: tests generalization to novel situations in which other agents form the test environment.
- R8 ○: social dilemmas are included, but the abstract does not address adversaries.

### vezhnevets2023concordia: Vezhnevets et al.
- R5 ◐: the Game Master adjudicates the plausibility and effects of agent actions. This is centralized arbitration.
- Others ○: a simulation library with no evaluation in the abstract.

### smith2025concordiagen: Smith et al. (NeurIPS 2025 D&B)
- R1 ●: zero-shot, mixed-motive evaluation across varied partners (NeurIPS 2024 Concordia Contest).
- R3 ◐: scenarios include negotiation.
- R8 ◐: mixed-motive partners, including persuasion and norm enforcement. These are not malicious attacks.

### tewolde2026coopeval: Tewolde et al. (ICML 2026)
- R1 ◐: varies co-players (repetition-induced cooperation degrades). Cross-play is not the primary protocol.
- R3 ◐: contract agreements for outcome-conditional payments.
- R5 ◐: mediators and contracts resolve social-dilemma conflicts. There are no termination guarantees.
- R8 ◐: covers defecting, payoff-maximizing agents under evolutionary pressure, but not malicious peers.

### cemri2025mast: Cemri et al.
- R5 ◐: taxonomizes inter-agent misalignment failures (detection and diagnosis only).
- R7 ○: annotated traces support research, not tamper-evident accountability.
- Others ○.

### kaliyev2026noisefloor: Kaliyev, Maryanskyy
- All ○: a statistical reporting protocol run on a single model. Its SHA-256 audit checks experimental inputs, not agent accountability. (Its methodology is still useful for our pilot.)

## Coding issues to log
1. Three rows (†) rely on snippets: Hayler, Qu-COLM, and Contract Net. Fetch the full text.
2. qu2026bgt and qu2026riskaversion are likely the same work. Decide whether to merge them.
3. Venues not verified in this pass (BibTeX left as arXiv): Other-Play, Deal or No Deal, MetaGPT, AutoGen, Magentic-One, MultiAgentBench, MAST, NegotiationArena, LLM-Stakeholders, LLM-Coordination.
4. Axis B: the taxonomy has no "self-interested but non-adversarial" category. Negotiation work is coded "multiple self-interested" or "mutually untrusting (mixed-motive)". Consider adding a category.
