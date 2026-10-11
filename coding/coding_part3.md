# Coding, Part 3: Additional security, negotiation, and collusion works

Coded on 2026-10-09 from full texts. Seven works were read as arXiv HTML: 2504.21034, 2502.01822, 2511.05359, 2506.00073, 2609.00595, 2505.23847 and 2402.07510. A2ASecBench was read from the ICLR 2026 proceedings PDF, found through Google Scholar. Some HTML pages are long and were read in 100k-character windows:
- **SAGA:** read in full.
- **Secret Collusion:** read through about 200k characters, including Appendix G.
- **Firewalls:** read through 100k of 134k characters.
- **Yang et al. SoK:** read through 100k of 261k characters.

Where a source is silent, the requirement is coded ○ and marked "not addressed". This is a single coding pass, using the same rubric and clarifications as coding_part2.md:

- **R1**: ● requires evaluation with unseen or independently developed partners. ◐ means cross-vendor interoperability is a design goal but is not evaluated.
- **R3**: ◐ means some explicit negotiation step exists (format, schema, protocol, or SLA). ● requires offers, counteroffers, and agreement semantics on terms.
- **R4**: ● requires rights that are scoped, short-lived, and attenuating (only able to narrow). ◐ means scoped or least-privilege authorization without the full set.
- **R7**: ● requires a tamper-evident record (ledger, blockchain, or tamper-evident log). ◐ means auditability or accountability is claimed or discussed.
- **R8**: ● requires malicious or compromised peers to be evaluated or formally analyzed. ◐ means a qualitative threat analysis, or measured leakage or over-exposure without an explicit adversary.
- **Surveys and perspectives**: ◐ for each requirement they systematically discuss.

Number of works coded: 8.

| Key | Work | Year | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | A | B | C | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| syros2026saga | SAGA: Security Architecture for Governing AI Agentic Systems | 2026 | ◐ | ◐ | ○ | ◐ | ○ | ◐ | ○ | ● | Protocol-mediated (Provider-mediated agent-to-agent protocol; A2A integration) | Multiple principals (many users' agents) mediated by a trusted central Provider | Centralized registry/Provider + cryptographic access-control tokens (DH-derived via one-time keys; expiring, quota-bounded) | Adversarial (ProVerif proofs + 8 implemented attackers) + performance/scalability |
| abdelnabi2026firewalls | Firewalls to Secure Dynamic LLM Agentic Networks | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ● | Language-mediated, with firewall-imposed structured protocol | Two principals: user's assistant vs untrusted external service agent | N/A (input/data firewalls; no authorization tokens) | Adversarial (864 ConVerse attacks); self-play (same model in all roles) |
| gomaa2025converse | ConVerse: Contextual Safety in Agent-to-Agent Conversations | 2025 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | Language-mediated (multi-turn assistant-external agent dialogue) | Two principals: user's assistant vs possibly malicious/compromised external agent | None | Adversarial benchmark (864 attacks, 7 assistant backends; external-agent model not stated) |
| li2026a2asecbench | A2ASecBench: Protocol-aware security benchmark for A2A MAS | 2026 | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ● | Protocol-mediated (A2A; transfer to LangGraph and ANP) | Single deployment (Host + remote agents) with untrusted third-party agents/users | A2A as deployed (web-security primitives; analyzed) | Adversarial benchmark (6 attacks, 3 domains; NeMo Guardrails defense) |
| zhu2025riskygame | The Automated but Risky Game: A2A negotiation in consumer markets | 2025 | ● | ○ | ● | ○ | ◐ | ○ | ○ | ◐ | Language-mediated (alternating-offer price negotiation) | Multiple principals with opposed interests (consumer buyer vs merchant seller) | N/A (prompt-only budget/wholesale constraints) | Cross-vendor (9-model round-robin incl. OpenAI, DeepSeek, Qwen) |
| yang2026soksafeagents | SoK: When Safe Agents Fail Together (MAS security) | 2026 | ◐ | ◐ | ○ | ◐ | ◐ | ○ | ◐ | ◐ | N/A (SoK; 197 works) | N/A (SoK; MAS defined by separately addressable principals) | Surveys identity/credential defenses (DIDs, SPIFFE, Agentic JWT) | None (literature synthesis + audit of 44 benchmarks) |
| ko2026sevenchallenges | Seven Security Challenges in Cross-Domain Multi-Agent LLM Systems | 2026 | ◐ | ◐ | ○ | ○ | ◐ | ◐ | ◐ | ◐ | N/A (perspective) | Multiple mutually untrusting principals (agents of different organizations, no central oversight) | N/A (federated authentication suggested) | None (proposed metrics only) |
| motwani2024collusion | Secret Collusion among AI Agents: Steganography | 2024 | ○ | ○ | ○ | ○ | ○ | ◐ | ○ | ● | Language-mediated (covert steganographic channels) | Single principal (system designer/deployer; colluders vs trusted overseer) | N/A | Adversarial (formal threat model + CASE evals; same-model clones) |

## Counts per requirement

| Req | ● | ◐ | ○ |
|---|---|---|---|
| R1 | 1 | 3 | 4 |
| R2 | 0 | 4 | 4 |
| R3 | 1 | 0 | 7 |
| R4 | 0 | 3 | 5 |
| R5 | 0 | 3 | 5 |
| R6 | 0 | 4 | 4 |
| R7 | 0 | 2 | 6 |
| R8 | 5 | 3 | 0 |

## Justifications

### syros2026saga: SAGA (2026)
- R1 ◐: Claims LLM-agent-agnostic design with A2A integration; no mixed-vendor partner evaluation.
- R2 ◐: Registry stores signed metadata and Agent Cards; identity verified, capabilities not.
- R3 ○: Not addressed (no offer or agreement protocol).
- R4 ◐: Access-control tokens are task-scoped, expiring and quota-bounded; no attenuation or re-delegation.
- R5 ○: Only policy-rule specificity precedence; no inter-agent conflict resolution.
- R6 ◐: Users set contact policies, blocklist and deactivate agents; no runtime escalation.
- R7 ○: Not addressed (auditing mentioned only as optional future add-on).
- R8 ●: Malicious, compromised, colluding and Sybil agents; ProVerif plus 8 implemented attacks.
- MUAC difference: relies on a trusted central Provider; no negotiation or conflict resolution; data ecosystems not modeled.

### abdelnabi2026firewalls: Firewalls to Secure Dynamic LLM Agentic Networks (2026)
- R1 ○: Same model plays assistant, external agent and environment, by design.
- R2 ○: Not addressed; verifier checks message fields, not partner capabilities.
- R3 ○: Structured task protocol imposed by firewall; no offers or agreement semantics.
- R4 ◐: Data firewall abstracts disclosures to task-needed granularity; no delegated rights.
- R5 ○: Not addressed (upselling conflicts left to assistant alignment).
- R6 ○: Humans only refine rules offline; no runtime escalation.
- R7 ○: Not addressed.
- R8 ●: Adversarial external agents evaluated; 864 privacy and security attacks.
- MUAC difference: one user-assistant vs one service channel; no delegation, conflict resolution, or cross-vendor partners.

### gomaa2025converse: ConVerse (2025)
- R1 ○: No cross-play; external agent's model not stated.
- R2 ○: Not addressed; authors note assistants cannot verify external claims.
- R3 ○: Free-form planning loop; no offer/counteroffer protocol or turn limit stated.
- R4 ○: Not addressed (approval gates only future work).
- R5 ○: Not addressed.
- R6 ○: Assumes fully autonomous operation; oversight left to future work.
- R7 ○: Not addressed (interaction logs used only for judging).
- R8 ●: Malicious/compromised external agent; 611 privacy and 253 security attacks.
- MUAC difference: evaluation-only, two-party, synthetic personal data; no authorization or coordination mechanisms.

### li2026a2asecbench: A2ASecBench (2026)
- R1 ○: Host and servers all Gemini 2.5 Flash; only spoofing ASR varied by model.
- R2 ◐: Evaluates AgentCard spoofing and capability cloaking; recommends attestation, provides none.
- R3 ○: Not addressed.
- R4 ○: Not addressed (scoped tokens mentioned only as related-work defenses).
- R5 ○: Cycle/flooding attacks measured; no conflict mechanism proposed.
- R6 ○: Not addressed (input-required pause analyzed as attack surface).
- R7 ○: Not addressed (auditing listed only as gateway recommendation).
- R8 ●: Six attacks by malicious agents/users evaluated; up to 100% ASR.
- MUAC difference: single A2A deployment with untrusted peers; no negotiation, delegation, or data-ecosystem setting.

### zhu2025riskygame: The Automated but Risky Game (2025)
- R1 ●: Full round-robin cross-play across OpenAI, DeepSeek and Qwen models.
- R2 ○: Not addressed.
- R3 ●: Alternating offers/counteroffers, accept/reject semantics, Tmax=30 round bound.
- R4 ○: Budget limits are prompt-only, unenforced; no delegated rights.
- R5 ◐: Termination at Tmax; deadlock measured; no arbitration.
- R6 ○: Fully autonomous; human-in-the-loop only future work.
- R7 ○: Not addressed.
- R8 ◐: Measures overpayment, constraint violations, budget disclosure; no explicit adversary.
- MUAC difference: two-party price bargaining only; no authorization, delegation, or shared data environment.

### yang2026soksafeagents: SoK: When Safe Agents Fail Together (2026)
- R1 ◐: Flags unknown principals across administrative boundaries as a gap; 42/44 benchmarks fixed-membership.
- R2 ◐: Admission interface (identity, provenance, initial trust) and identity defenses systematized.
- R3 ○: Negotiation only peripheral (ten benchmark works use negotiation/deception games).
- R4 ◐: Transitive authorization failure and scope propagation systematized; least privilege not named.
- R5 ◐: Collective commitment, Byzantine consensus and aggregation defenses discussed.
- R6 ○: Oversight framed as monitors; human escalation not discussed (in text read).
- R7 ◐: Provenance graphs central; tamper-evident logs not addressed.
- R8 ◐: Survey of malicious-member, injection, collusion, leakage threats; no own experiments.
- MUAC difference: security-only systematization; does not treat negotiation, delegation design, or data ecosystems.

### ko2026sevenchallenges: Seven Security Challenges in Cross-Domain Multi-Agent LLM Systems (2026)
- R1 ◐: Unvetted dynamic grouping across organizations discussed; no evaluation.
- R2 ◐: Sandbox on-boarding vetting, identity verification, attestation discussed as open.
- R3 ○: Negotiation mentioned only as collusion risk and meta-LLM remedy.
- R4 ○: Not addressed systematically (brief RBAC/ACL remarks only).
- R5 ◐: Proposes federated conflict-arbitration protocol and conflict-resolution metric.
- R6 ◐: Resolutions approved by human operators of both domains; dashboards can halt.
- R7 ◐: Cross-domain provenance challenge; signed audit log for parameter updates only.
- R8 ◐: Illustrative attack scenarios (malicious peer, impersonation, collusion, injection); no experiments.
- MUAC difference: closest in setting (cross-organization, no central trust) but a research agenda without mechanisms or evaluation.

### motwani2024collusion: Secret Collusion among AI Agents (2024)
- R1 ○: Colluders are same-model clones; overseer matches decoder model.
- R2 ○: Measures model steganographic capabilities, not peer capability discovery.
- R3 ○: Not addressed (Schelling-point coordination without communication).
- R4 ○: Not addressed (monitor access levels only).
- R5 ○: Not addressed.
- R6 ◐: Overseer may be human; no escalation path defined.
- R7 ○: Shared message log monitored; no tamper-evident record.
- R8 ●: Colluding agents (T4) formally modeled and empirically evaluated against overseers.
- MUAC difference: single designer's system with a trusted overseer; colluders, not mutually untrusting principals.
