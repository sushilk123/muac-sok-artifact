# Coding, Part 2: Sections 6.4-6.7 (excluding MPAC, CAPMAS, Governance Gaps)

Coded on 2026-10-09 from abstracts and official pages: arXiv abstracts via the export API, the MCP and A2A announcement posts, the ACP site and README, and Crossref or Google Scholar records for the non-arXiv works. Full texts were not read, so where a source is silent the requirement is coded ○ and marked "not addressed". Single coding pass; this is the first of the two planned passes.

Rubric applied:

- **R1**: ● requires evaluation with unseen or independently developed partners. ◐ means cross-vendor interoperability is a design goal but is not evaluated.
- **R3**: ◐ means some explicit negotiation step exists (format, schema, protocol, or SLA). ● requires offers, counteroffers, and agreement semantics on terms.
- **R4**: ● requires rights that are scoped, short-lived, and attenuating (only able to narrow). ◐ means scoped or least-privilege authorization without the full set.
- **R7**: ● requires a tamper-evident record (ledger, blockchain, or tamper-evident log). ◐ means auditability or accountability is claimed or discussed.
- **R8**: ● requires malicious or compromised peers to be evaluated or formally analyzed. ◐ means a qualitative threat analysis, or measured leakage or over-exposure without an explicit adversary.
- **Surveys**: ◐ for each requirement they systematically discuss.

Number of works coded: 39.

| Key | Work | Year | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | A | B | C | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| anthropic2024mcp | Model Context Protocol (MCP) announcement | 2024 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (client-server, agent-to-tool/data) | Single principal (host app connects to data-owner servers) | Unspecified in source ("secure, two-way connections") | None (spec/announcement) |
| google2025a2a | Agent2Agent Protocol (A2A) announcement | 2025 | ◐ | ◐ | ◐ | ○ | ○ | ◐ | ○ | ○ | Protocol-mediated (task lifecycle, Agent Cards) | Multiple cooperative principals (agents from different vendors/frameworks) | Centralized IAM ("parity with OpenAPI auth schemes") | None (spec/announcement) |
| beeai2025acp | Agent Communication Protocol (ACP; merged into A2A) | 2025 | ◐ | ◐ | ○ | ○ | ○ | ◐ | ○ | ○ | Protocol-mediated (RESTful, sync/async, Await) | Multiple cooperative principals (inter-company use case) | Unspecified (no authentication described) | None (spec) |
| chang2025anp | Agent Network Protocol (ANP) white paper | 2025 | ◐ | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (three-layer: identity, meta-protocol, application) | Multiple principals on open Agentic Web (trust via identity authentication) | Decentralized identity (DIDs per ehtesham2025survey; ANP abstract says "identity and encrypted communication layer") | None (white paper) |
| ehtesham2025survey | Ehtesham et al., survey of MCP/ACP/A2A/ANP | 2025 | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (survey) | Mixed (surveyed protocols) | Compares security models (role-based, DIDs) | None (survey) |
| sander2026taxonomy | Sander et al., technical taxonomy of agent communication protocols | 2026 | ◐ | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (taxonomy of 9 protocols) | N/A (taxonomy) | N/A | None (taxonomy) |
| krishnan2026unified | Unified Agent Communication Protocol (ACP) for A2A orchestration | 2026 | ◐ | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (federated orchestration) | Multiple principals, federated, "zero-trust posture" | Decentralized identity verification | Latency evaluation only (partner regime not stated) |
| du2025internet | Du et al., agent communication from Internet-architecture perspective | 2025 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (perspective) | N/A (position) | N/A | None (perspective) |
| south2025authenticated | Authenticated Delegation and Authorized AI Agents | 2025 | ○ | ○ | ○ | ◐ | ○ | ○ | ◐ | ○ | N/A (delegation infrastructure) | Single principal (human user delegating to agent) | Centralized IAM (OAuth 2.0/OIDC extended with agent credentials) | None (framework proposal) |
| zouari2025agentic | Zouari, Toward Agentic IAM (probabilistic least-privilege) | 2025 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | Pipeline of specialized IAM agents (Analyze/Impact/Minimize/Validate/Reanalyze) | Single principal (one organization) | Centralized IAM (cloud IAM; AWS Lambda case) | Formal analysis + single-org case study |
| huang2025ans | Agent Name Service (ANS) | 2025 | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ◐ | Protocol-mediated (directory; adapters for A2A/MCP/ACP) | Multiple principals, public registry | PKI certificates (CA-anchored identity) | None (design + threat analysis) |
| huang2025zerotrust | Zero-Trust Identity Framework for Agentic AI | 2025 | ◐ | ◐ | ○ | ◐ | ○ | ○ | ◐ | ◐ | Protocol-agnostic identity/policy layer | Multiple mutually untrusting principals (zero-trust) | Decentralized identity (DIDs + VCs, ZKPs) | None (architecture) |
| nagabhushanaradhya2025oidca | OpenID Connect for Agents (OIDC-A) 1.0 | 2025 | ○ | ◐ | ○ | ◐ | ○ | ○ | ◐ | ○ | N/A (identity spec, agent-to-service) | Single principal (agent acting for user toward services) | Centralized IAM (OAuth 2.0/OIDC extension) | None (spec) |
| lee2024prompt | Prompt Infection: LLM-to-LLM prompt injection | 2024 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | Language-mediated (LLM MAS) | Single principal (one MAS) | None | Adversarial (self-built MAS) |
| an2026aciarena | ACIArena: agent cascading injection benchmark | 2026 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | Language-mediated (six MAS implementations) | Single principal | None | Adversarial benchmark (1,356 cases) |
| lotfi2026a2abreak | A2ABreak: systematic security analysis of A2A | 2026 | ○ | ◐ | ○ | ◐ | ○ | ○ | ○ | ● | Protocol-mediated (A2A) | Multiple mutually untrusting principals (cross-organizational) | A2A as specified (analyzed) | Adversarial (formal FSM + expert review) |
| zou2025blocka2a | BlockA2A | 2025 | ○ | ◐ | ○ | ◐ | ○ | ○ | ● | ● | Protocol-mediated (A2A extension) | Multiple mutually untrusting principals (cross-domain, no central trust) | Decentralized identity + blockchain (DIDs, smart contracts) | Adversarial (prompt, communication, behavioral, systemic attacks) |
| zheng2026agentrfc | AgentRFC: security principles and conformance testing | 2026 | ○ | ○ | ○ | ◐ | ○ | ◐ | ◐ | ● | Protocol-mediated (MCP, A2A, ANP, ACP) | Multiple principals across trust boundaries | N/A (analyzes protocol credential lifecycles) | Adversarial (TLA+ model checking + SDK replay) |
| anbiaee2026threat | Threat modeling of MCP, A2A, Agora, ANP | 2026 | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ◐ | Protocol-mediated (four protocols) | Multiple principals (cross-organizational) | N/A (analysis) | Qualitative threat model + MCP measurement |
| xu2025trust | The Trust Paradox in LLM MAS | 2025 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ◐ | Language-mediated (multiple orchestration frameworks) | Parameterized inter-agent trust (principal structure not stated) | None formal (trust-parameterized information sharing) | Multi-backend empirical (no cross-vendor pairing stated) |
| nipu2026trustgated | Trust-Gated Capability Control | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ● | N/A (trust/authorization mechanism for LLM MAS) | Untrusting peers (trust earned; principal structure not stated) | Capability tokens (short-lived, revocable grants) | Adversarial (formal proofs + numerical sleeper-adversary simulation) |
| elhelou2026hybrid | Hybrid Inspection and Task-Based Access Control (CASA) | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ◐ | N/A (agent tool authorization, multi-turn) | Single principal (subject commissioning agent) | Centralized IAM (authorization server + zero-trust interception layer) | Dataset benchmark (relevant vs irrelevant tool calls) |
| raza2025trism | TRiSM for Agentic AI (review) | 2025 | ○ | ○ | ○ | ○ | ○ | ○ | ◐ | ◐ | N/A (survey) | N/A | N/A | None (survey) |
| vargas_identity | Vargas et al., agent-as-principal identity/authorization survey | n.d. | ○ | ◐ | ○ | ◐ | ○ | ○ | ○ | ◐ | N/A (survey) | Multiple principals (delegation and peer-identity planes) | Capability security / speaks-for delegation (surveyed) | None (survey; 72 papers coded) |
| mostafavi2026trustworthy | Mostafavi, Trustworthy Agentic AI survey | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ◐ | ◐ | N/A (survey) | N/A | Capability-Based Access Control (in proposed defense architecture) | None (survey) |
| forough2026confidential | Confidential computing for agentic AI (survey) | 2026 | ○ | ◐ | ○ | ○ | ○ | ○ | ○ | ◐ | N/A (survey) | Multiple untrusting parties (pipelines no single party controls) | Hardware attestation (TEEs) -- outside Axis C list | None (survey) |
| dafoe2020open | Open Problems in Cooperative AI | 2020 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | N/A (research agenda) | Multiple principals (mixed-motive cooperation) | N/A | None (agenda) |
| hammond2025multiagent | Multi-Agent Risks from Advanced AI | 2025 | ◐ | ○ | ○ | ○ | ◐ | ○ | ○ | ◐ | N/A (risk taxonomy) | Multiple mixed-motive principals | N/A | None (report) |
| sourbut2024delegation | Cooperation and Control in Delegation Games | 2024 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | Game-theoretic (mechanism/market design family) | Multiple principals, each delegating to own agent | N/A | Formal analysis + empirical (synthetic games) |
| tomasev2025virtual | Virtual Agent Economies | 2025 | ○ | ○ | ◐ | ○ | ◐ | ○ | ◐ | ○ | Market or mechanism design (auctions, mission economies) | Multiple principals (agent markets) | N/A | None (position) |
| tomasev2026intelligent | Intelligent AI Delegation | 2026 | ○ | ○ | ○ | ◐ | ○ | ◐ | ◐ | ○ | Delegation framework (conceptual, for agentic-web protocols) | Multiple principals (delegation networks) | N/A (conceptual) | None (framework) |
| ruan2026agentcity | AgentCity: constitutional governance (Separation of Power) | 2026 | ○ | ○ | ○ | ○ | ◐ | ◐ | ◐ | ○ | Mechanism design / institutional (smart-contract legislation) | Multiple mutually untrusting principals (cross-org, open internet) | Blockchain (EVM L2 smart contracts, ownership chain) | Pre-registered simulation, 50-1,000 agents (results not in abstract) |
| yang2026multiuser | Multi-User LLM Agents | 2026 | ○ | ○ | ○ | ○ | ◐ | ○ | ○ | ◐ | Language-mediated (single agent, multi-user protocol) | Multiple principals with conflicting interests (single agent) | N/A | Stress tests on frontier LLMs |
| hu2025regulatory | Regulatory multi-agent collaboration (blockchain architecture) | 2025 | ○ | ◐ | ○ | ○ | ◐ | ○ | ◐ | ◐ | N/A (governance architecture) | Multiple heterogeneous, potentially adversarial agents | Blockchain (on-chain anchoring) | None reported in abstract |
| alonsoruiz2026bridging | Bridging LLM agents and data spaces via MCP (Eunomia) | 2026 | ◐ | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | Protocol-mediated (MCP mediation layer) | Multiple principals (sovereign cross-org data sharing) | Data-space governance (via mediation; mechanism not detailed) | Prototype functional validation |
| zhong2025agentodrl | AgentODRL: multi-agent ODRL generation | 2025 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | Language-mediated (orchestrator-workers) | Single principal | N/A (output is ODRL policy) | Self-play (in-house MAS, 770 use cases) |
| ren2026gatemem | GateMem: memory governance benchmark | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ◐ | Language-mediated (shared-memory agent) | Multiple principals sharing one memory pool | Contextual role/scope-based access control | Benchmark across backbones and memory methods |
| johnson2026aim | AIM: privacy-aware interoperable memory | 2026 | ○ | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | Language-mediated (shared memory) | Multiple users (cooperative) | Index-level access control (centralized) | Benchmark (MUMBench, three runs) |
| shukla2025multiagent | Shukla & Parker, Multi-Agent Orchestration Protocol for GenAI | 2025 | ○ | ◐ | ○ | ◐ | ○ | ○ | ● | ○ | Protocol-mediated (central orchestrator) | Single principal (central orchestrator) | Centralized policy engine (GDPR/HIPAA rules) + Agent Registry | Simulation (latency, compliance violations) |

## Counts per requirement

| Req | ● | ◐ | ○ |
|---|---|---|---|
| R1 | 0 | 13 | 26 |
| R2 | 0 | 17 | 22 |
| R3 | 0 | 5 | 34 |
| R4 | 0 | 16 | 23 |
| R5 | 0 | 5 | 34 |
| R6 | 1 | 4 | 34 |
| R7 | 4 | 8 | 27 |
| R8 | 6 | 13 | 20 |

## Justifications

### anthropic2024mcp: Model Context Protocol (MCP) announcement (2024)
- R1 ◐: Open standard for independently built clients/servers; no partner evaluation.
- R2 ○: Not addressed in announcement.
- R3 ○: Not addressed.
- R4 ○: Not addressed; no auth/authz details given.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Coded from the announcement post only (as instructed); later MCP spec revisions (e.g., authorization) are not reflected.

### google2025a2a: Agent2Agent Protocol (A2A) announcement (2025)
- R1 ◐: Designed for agents from different vendors/frameworks; no cross-vendor evaluation.
- R2 ◐: JSON Agent Cards advertise capabilities; claims are not verified.
- R3 ◐: Only content-type "UX negotiation"; no offers, counteroffers, or agreement on terms.
- R4 ○: Enterprise authn/authz mentioned; no scoping, expiry, or attenuation described.
- R5 ○: Not addressed.
- R6 ◐: Humans-in-the-loop mentioned for long tasks; no defined escalation mechanism.
- R7 ○: Not addressed (partners mention observability only).
- R8 ○: Not addressed.

### beeai2025acp: Agent Communication Protocol (ACP; merged into A2A) (2025)
- R1 ◐: Framework-agnostic interoperability (BeeAI, LangChain, CrewAI); not evaluated.
- R2 ◐: Agent Manifest and online/offline discovery; no verification of claims.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ◐: "Await" lets agents pause to request client input; not explicit human escalation.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Coded from agentcommunicationprotocol.dev and the GitHub README; repo archived 27 Aug 2025, now part of A2A. IBM affiliation not stated on these pages.

### chang2025anp: Agent Network Protocol (ANP) white paper (2025)
- R1 ◐: Targets large-scale interconnection of heterogeneous agents; no partner evaluation.
- R2 ◐: Addresses identity authentication and capability discovery; capability claims not verified.
- R3 ◐: Meta-protocol negotiation layer negotiates interaction protocols, not task terms.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.

### ehtesham2025survey: Ehtesham et al., survey of MCP/ACP/A2A/ANP (2025)
- R1 ◐: Systematically discusses interoperability across heterogeneous systems.
- R2 ◐: Compares discovery mechanisms (Agent Cards, DIDs, offline discovery).
- R3 ○: Not addressed.
- R4 ○: Security models compared; delegation scoping/attenuation not discussed in abstract.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.

### sander2026taxonomy: Sander et al., technical taxonomy of agent communication protocols (2026)
- R1 ◐: Interoperability across fragmented protocol landscape is the organizing problem.
- R2 ◐: Discovery mechanism is a taxonomy dimension; verification not covered.
- R3 ◐: Notes two protocols negotiate schemas at runtime (schema-level only).
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed; privacy and policy enforcement flagged as open gaps.

### krishnan2026unified: Unified Agent Communication Protocol (ACP) for A2A orchestration (2026)
- R1 ◐: Heterogeneous agents across disparate environments; cross-vendor evaluation not described.
- R2 ◐: Discovery plus decentralized identity verification; capabilities not verified.
- R3 ◐: Negotiation and automated service-level agreements; no semantics described in abstract.
- R4 ○: Not addressed beyond claimed zero-trust posture.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Zero-trust claimed; no adversarial evaluation reported.
- Note: Abstract contains an incomplete figure ("reduces ... latency by %"); single author.

### du2025internet: Du et al., agent communication from Internet-architecture perspective (2025)
- R1 ◐: Discusses cross-domain interoperability and fragmentation systematically.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed (security discussed generically).
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed ("manageability" discussed, not audit).
- R8 ○: Not addressed specifically.
- Note: Self-described "Work in Progress".

### south2025authenticated: Authenticated Delegation and Authorized AI Agents (2025)
- R1 ○: Not addressed; no inter-agent coordination.
- R2 ○: Agent credentials identify on whose behalf; capabilities not verified.
- R3 ○: Not addressed.
- R4 ◐: Users delegate and restrict scope; expiry/attenuation not stated in abstract.
- R5 ○: Not addressed.
- R6 ○: Humans set scope up front; no runtime escalation path described.
- R7 ◐: "Auditable" delegation and accountability chains; tamper-evidence not stated.
- R8 ○: Not addressed.

### zouari2025agentic: Zouari, Toward Agentic IAM (probabilistic least-privilege) (2025)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Probabilistic permission minimization (~40% reduction); no delegation chains or attenuation.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Coded from Crossref/Scholar abstract; ACM DL page blocked.

### huang2025ans: Agent Name Service (ANS) (2025)
- R1 ◐: Protocol-agnostic adapter layer for diverse standards; not evaluated.
- R2 ◐: PKI-verified identity and capability-aware resolution; capability claims themselves unverified.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Registration/renewal lifecycle only; no audit trail.
- R8 ◐: Qualitative threat analysis; no adversarial evaluation.

### huang2025zerotrust: Zero-Trust Identity Framework for Agentic AI (2025)
- R1 ◐: Policy layer across heterogeneous agent protocols; not evaluated.
- R2 ◐: VCs encapsulate capabilities, provenance, and posture; issuer-attested, design only.
- R3 ○: Not addressed.
- R4 ◐: Fine-grained dynamic access control and consistent revocation; attenuation not stated.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ◐: Accountability stated as goal; no tamper-evident log detailed.
- R8 ◐: Security considerations discussed; no evaluation.

### nagabhushanaradhya2025oidca: OpenID Connect for Agents (OIDC-A) 1.0 (2025)
- R1 ○: Not addressed.
- R2 ◐: Attestation verification and agent attribute claims; capabilities self/issuer asserted.
- R3 ○: Not addressed.
- R4 ◐: Delegation-chain validation and capability-based authorization; attenuation not stated.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ◐: Delegation chains represented in claims; no audit log.
- R8 ○: Not addressed.

### lee2024prompt: Prompt Infection: LLM-to-LLM prompt injection (2024)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ●: Self-replicating injection across agents evaluated (T2); LLM Tagging defense.

### an2026aciarena: ACIArena: agent cascading injection benchmark (2026)
- R1 ○: Not addressed; MAS are internally co-designed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ●: Compromised-agent attacks across three surfaces systematically evaluated (T1/T2).

### lotfi2026a2abreak: A2ABreak: systematic security analysis of A2A (2026)
- R1 ○: Not addressed.
- R2 ◐: Identifies rogue agents advertising unattested capability claims (analysis, not mechanism).
- R3 ○: Not addressed.
- R4 ◐: Finds credential harvesting via identity loss in delegation chains (analysis).
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ●: Formal verification against spec-compliant adversary; 11 vulnerabilities.

### zou2025blocka2a: BlockA2A (2025)
- R1 ○: Not addressed.
- R2 ◐: DID-based cross-domain authentication; capability claims not verified.
- R3 ○: Not addressed.
- R4 ◐: Smart-contract context-aware access control and instant revocation; attenuation not stated.
- R5 ○: Not addressed (execution halting is defensive, not conflict resolution).
- R6 ○: Not addressed.
- R7 ●: Blockchain-anchored immutable ledgers for auditability and accountability.
- R8 ●: Byzantine agents and prompt attacks empirically neutralized.

### zheng2026agentrfc: AgentRFC: security principles and conformance testing (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Credential lifecycle gaps checked as invariants; no delegation mechanism.
- R5 ○: Not addressed.
- R6 ◐: Consent enforcement among checked properties; no escalation path.
- R7 ◐: Audit completeness formalized as invariant; gaps found.
- R8 ●: Explicit adversary actions model-checked; composition attacks.
- Note: Preliminary; full evaluation details withheld pending disclosure.

### anbiaee2026threat: Threat modeling of MCP, A2A, Agora, ANP (2026)
- R1 ○: Not addressed (interoperability context only).
- R2 ◐: Formalizes missing validation/attestation of executable components in MCP.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Qualitative risk assessment; MCP wrong-provider measurement, not adversarial peer agents.
- Note: Borderline R8: the wrong-provider measurement relates to T3 (impersonation) but is framed as resolver-policy risk.

### xu2025trust: The Trust Paradox in LLM MAS (2025)
- R1 ○: Multiple backends tested; cross-vendor pairing not stated.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Measures authorization drift against minimum-necessary-information baseline.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Measures over-exposure (T5-like); adversarial peers not explicit; guardian-agent defense.

### nipu2026trustgated: Trust-Gated Capability Control (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed (behavioral trust, not capability verification).
- R3 ○: Not addressed.
- R4 ◐: Short-lived, revocable, capability-specific grants; narrowing/attenuation not stated.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ●: Proves stealthy compromise cannot escalate privilege; sleeper adversary simulated.
- Note: Evaluation is numerical simulation; no LLM experiments reported in abstract.

### elhelou2026hybrid: Hybrid Inspection and Task-Based Access Control (CASA) (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Task-scoped tool authorization from extracted intent; no delegation chain attenuation.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Threat model includes compromised agents; evaluation detects irrelevant calls, not live attacks.

### raza2025trism: TRiSM for Agentic AI (review) (2025)
- R1 ○: Not addressed (CSS metric measures collaboration quality, not cross-play).
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ○: Not addressed (coordination failures in taxonomy, no resolution).
- R6 ○: Not addressed.
- R7 ◐: Lifecycle governance, transparency, accountability discussed.
- R8 ◐: Risk taxonomy includes prompt-based adversarial manipulation.
- Note: Also published in AI Open (2026).

### vargas_identity: Vargas et al., agent-as-principal identity/authorization survey (n.d.)
- R1 ○: Not addressed.
- R2 ◐: Peer-identity plane surveys inter-agent authentication.
- R3 ○: Not addressed.
- R4 ◐: Delegation-identity plane, capability security, revocation across chains discussed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed in available summary.
- R8 ◐: Case analyses of structural failures; 14 defenses assessed vs 8 properties.
- Note: Year/venue unverified (ResearchGate preprint); coded from Google Scholar snippet.

### mostafavi2026trustworthy: Mostafavi, Trustworthy Agentic AI survey (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Capability-based access control in zero-trust defense-in-depth architecture.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ◐: Accountability is a taxonomy dimension; governance mapping.
- R8 ◐: Threat surfaces across interaction planes systematically analyzed.

### forough2026confidential: Confidential computing for agentic AI (survey) (2026)
- R1 ○: Not addressed.
- R2 ◐: Remote attestation for verifiable trust; compound attestation for multi-hop chains open.
- R3 ○: Not addressed.
- R4 ○: Not addressed (credential theft discussed as threat).
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Threat model incl. inter-agent message poisoning, compromised operator.

### dafoe2020open: Open Problems in Cooperative AI (2020)
- R1 ◐: Cooperation among machine/human agents is the central topic.
- R2 ○: Not addressed in abstract.
- R3 ○: Not addressed in abstract.
- R4 ○: Not addressed.
- R5 ○: Not addressed in abstract.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Coded from abstract only; full text may discuss commitment/bargaining.

### hammond2025multiagent: Multi-Agent Risks from Advanced AI (2025)
- R1 ◐: Miscoordination is a key failure mode.
- R2 ○: Not addressed.
- R3 ○: Not addressed (commitment problems named as risk factor only).
- R4 ○: Not addressed.
- R5 ◐: Conflict is a key failure mode; no resolution mechanism.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Collusion and multi-agent security systematically discussed.

### sourbut2024delegation: Cooperation and Control in Delegation Games (2024)
- R1 ○: Not addressed (unseen-partner play not studied).
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Delegation is preference-alignment, not rights scoping.
- R5 ○: Cooperation failures formalized; no resolution mechanism.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Contributes formal grounding for Axis B (multi-principal) rather than R1-R8 mechanisms.

### tomasev2025virtual: Virtual Agent Economies (2025)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ◐: Auction mechanisms proposed for allocation; no bilateral offer semantics.
- R4 ○: Not addressed.
- R5 ◐: Auctions for preference resolution; no guarantees stated.
- R6 ○: Not addressed (notes scale beyond direct human oversight).
- R7 ◐: Socio-technical infrastructure for trust and accountability discussed.
- R8 ○: Not addressed (systemic economic risk only).

### tomasev2026intelligent: Intelligent AI Delegation (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed (trust-establishment mechanisms unspecified).
- R3 ○: Not addressed.
- R4 ◐: Transfer of authority with roles and boundaries; no scoping/attenuation mechanism.
- R5 ○: Not addressed.
- R6 ◐: Humans included as delegators/delegatees; no defined escalation trigger.
- R7 ◐: Responsibility and accountability transfer discussed.
- R8 ○: Not addressed ("unexpected failures", not adversaries).

_Recoded after review: R6 and R7 lowered from ● to ◐ (designs without reported results; rubric requires evidence for ●)._

### ruan2026agentcity: AgentCity: constitutional governance (Separation of Power) (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Agents legislate rules as contracts; no offer/counteroffer semantics.
- R4 ○: Not addressed.
- R5 ◐: Human adjudication of disputes; termination/deadlock guarantees not stated.
- R6 ●: Humans adjudicate via complete ownership chain to responsible principal.
- R7 ●: On-chain ownership chain binds every agent to a principal.
- R8 ○: Not addressed in abstract.

### yang2026multiuser: Multi-User LLM Agents (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed (authority levels modeled, no delegation).
- R5 ◐: Conflicting objectives formalized and stress-tested; prioritization unstable; no guarantees.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Privacy violations across users measured (T5-like); no adversarial agents.

_Recoded after review: R7 lowered from ● to ◐ (no evaluation reported)._

### hu2025regulatory: Regulatory multi-agent collaboration (blockchain architecture) (2025)
- R1 ○: Not addressed.
- R2 ◐: Dynamic reputation evaluation for trust; capabilities not verified.
- R3 ○: Not addressed.
- R4 ○: Not addressed.
- R5 ◐: Behavior tracing and arbitration module; no guarantees stated.
- R6 ○: Not addressed.
- R7 ●: On-chain anchoring with behavior tracing for automated accountability.
- R8 ◐: Malicious-behavior forecasting proposed; evaluation not reported.

### alonsoruiz2026bridging: Bridging LLM agents and data spaces via MCP (Eunomia) (2026)
- R1 ◐: Integrates with unmodified data-space components; not agent-to-agent cross-vendor.
- R2 ◐: Catalog discovery exposed as schema-driven MCP tools; no verification.
- R3 ○: Not addressed.
- R4 ○: "Preserving governance constraints" claimed; scoping not detailed.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.

### zhong2025agentodrl: AgentODRL: multi-agent ODRL generation (2025)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ○: Not addressed (generates policies, no inter-agent delegation).
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed.
- Note: Relevant to data-ecosystem policy authoring, not inter-agent coordination.

### ren2026gatemem: GateMem: memory governance benchmark (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Evaluates access control across contextual authorization boundaries; no delegation.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ◐: Leakage of unauthorized/deleted information measured (T5-like); adversarial intent not stated.

### johnson2026aim: AIM: privacy-aware interoperable memory (2026)
- R1 ○: Not addressed.
- R2 ○: Not addressed.
- R3 ○: Not addressed.
- R4 ◐: Private memories retrievable only by owner; no delegation.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ○: Not addressed.
- R8 ○: Not addressed (classification accuracy only).

### shukla2025multiagent: Shukla & Parker, Multi-Agent Orchestration Protocol for GenAI (2025)
- R1 ○: Not addressed.
- R2 ◐: Agent Registry consulted for eligibility; verification not described.
- R3 ○: Not addressed.
- R4 ◐: Policy checks and access controls before routing; isolated memory shards; no attenuation.
- R5 ○: Not addressed.
- R6 ○: Not addressed.
- R7 ●: Tamper-evident audit log records every decision.
- R8 ○: Not addressed.
- Note: Coded from Google Scholar abstract snippet; IEEE Xplore page blocked.
