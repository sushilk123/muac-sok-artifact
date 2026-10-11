# Key Papers — Deep-Read Notes

Read on 2026-10-09. MPAC, CAPMAS, and Governance Gaps were read as full text via arxiv.org/html. Hayler et al. was read via the Google Scholar cached HTML of the OpenReview PDF, because OpenReview blocks bots.

**Caveat on quotes:** I extracted the quotes below with a fetch tool. Before camera-ready, re-check every quote and section number against the PDF. Any statement marked "(paraphrase)" is not verbatim.

---

## 1. MPAC

**Bib:** Kaiyang Qian, Xinmin Fang, Zhengxiong Li. "MPAC: A Multi-Principal Agent Coordination Protocol for Interoperable Multi-Agent Collaboration." arXiv:2604.09744 [cs.MA], v1, 10 Apr 2026. doi:10.48550/arXiv.2604.09744.
- There is no venue or comments field.
- License: CC BY 4.0.

### Problem
MCP and A2A "assume a single controlling principal" (Abstract). When agents of independent principals share state, "coordination collapses to ad-hoc chat, manual merging, or silent overwrites" (§1).

Definition of a multi-principal session (§2.1, paraphrase): at least two independent principals, where "no one principal has authority over the others' agents".

§2.1 sets three requirements:
- no unified decision-maker
- limited trust: "The protocol must be defensible against adversarial or buggy participants, not just correct ones."
- auditability across boundaries

§2.2 scenarios:
- shared codebase
- trip planning
- inter-organization contract drafting
- multi-tenant cluster resource allocation

### Mechanism
**Layers (§4.1).** MPAC is an application-layer protocol with five layers:
- **Session:** HELLO-first gate, credentials, capability/role negotiation, heartbeats.
- **Intent:** objective, scope, priority, TTL; supports announce, update, withdraw, supersede, claim.
- **Operation:** optimistic concurrency control via `state_ref_before/after` SHA-256; `STALE_STATE_REF` triggers a rebase.
- **Conflict:** `CONFLICT_REPORT` carries one of 8 categories, including `policy_violation`, `authority_conflict`, and `resource_contention`. An unresolved conflict times out and the scope freezes.
- **Governance:** role-policy authority checks; `RESOLUTION` records the deciding principal.

**Message types and state machines (§5).** 21 message types:
- 6 Session
- 5 Intent
- 5 Operation
- 4 Conflict: REPORT, ACK (seen/accepted/disputed), ESCALATE, RESOLUTION
- 1 Error

There are three state machines: intent, operation, and conflict.

**Execution and ordering (§4.2–4.4).**
- Two execution models, post-commit and pre-commit. Pre-commit requires the Governance profile and coordinator authorization.
- A single coordinator gives a total order ("analogous to single-leader replication").
- Lamport-clock watermarks are mandatory on OP_COMMIT, CONFLICT_REPORT, and RESOLUTION.

**Security profiles (§6.1).**
- **Open:** no credentials.
- **Authenticated:** bearer_token, mtls_fingerprint, api_key, x509_chain, or custom credentials, plus replay detection with a 5-minute window.
- **Verified:** the issuer verifies credentials; "self-asserted arbiter roles are rejected."
- Key management, identity issuance, and trust binding are out of scope (§3.2). No message-signing scheme is specified.

**Human override.**
- "it must be reachable from any state" (§3.1).
- It is a normative requirement for Governance-profile deployments (§3.3).
- Unauthorized RESOLUTION messages are rejected, and this "is not advisory" (§6.3, as extracted).

### Threat model and assumptions
- The coordinator is assumed "well-behaved (crash-stop, not Byzantine)" (§10). Byzantine consensus is not addressed (§9).
- Participants are assumed to follow the protocol "unless they are explicitly testing enforcement" (§10).
- Lying or forging participants are only partially addressed: "a rigorous threat model is future work" (§10).
- The paper does not discuss prompt injection, collusion, or malicious principals manipulating LLM reasoning. Free-text justification fields such as CONFLICT_ACK are a possible injection channel that it also leaves unaddressed.

### Evaluation
**Implementations (§7, Table 2).**
- Python: ~3.5k LOC, 122 tests, of which 34 are adversarial.
- TypeScript: ~2.9k LOC, 101 tests, of which 32 are adversarial.
- That makes 223 tests in total and **66 "enforcement-bypass" tests**, written after five rounds of independent audit. They cover:
  - pre-HELLO messages
  - credential bypass
  - self-asserted arbiter
  - unauthorized resolver
  - frozen-scope evasion
  - replay after recovery
  - batch rollback
- JSON Schema suite (Draft 2020-12).
- Cross-language interop: 14 messages with zero wire deviation.

**Live demos (§8, Table 3).**
- Seven live demos run on the Anthropic Claude API ("none uses mocked agents"):
  - code editing (2 agents)
  - trip planning (3)
  - overhead benchmark (3)
  - pre-commit plus fault recovery (3)
  - escalation to arbiter (3)
  - remote pip-packaged (2+)
  - Python/TS interop (2)
- **Every agent is Claude, including the arbiter.** The benchmark used claude-sonnet-4 with the same prompts in both modes (§8.4). Agents differ only by persona or system prompt.
- No other vendor appears, and no adversarial LLM agent appears.
- The "human" arbiter in the escalation demo is a Claude agent (§8.5).

**Benchmark (§8.4, Table 4).** Three-agent cross-module PR review, single run, against a serialized, human-mediated baseline.

| Metric | Baseline | MPAC | Change |
|---|---|---|---|
| Wall-clock | 131.76 s | 27.38 s | −79.2%, 4.8× |
| Decision time | 63.11 s | 57.13 s | −9.5% |
| Coordination overhead | 68.65 s | 3.02 s | −95.6% |
| Overhead share | 52.1% | 11.0% | — |

The paper attributes the gain to parallelism: "The speedup comes from eliminating coordination waits, not compressing model calls." (Abstract). It does not detail how the baseline's human-mediation delay was produced.

### Stated limitations (§10–11)
- "Single-run benchmark"; "treat the present numbers as calibration, not as a performance curve."
- "Coordinator is a single point of failure."
- Split-brain detection is not exercised.
- "No formal verification" (TLA+ is future work).
- "No head-to-head comparison with frameworks."
- Scope detection is coordinator-local, using set intersection of declared resources.
- "Signature verification and trust binding across organizational boundaries remain gaps."
- "We are not asking readers to adopt MPAC in production today."

### R1–R8
| R | Score | Justification |
|---|---|---|
| R1 | ◐ | Designed for independent principals, but every evaluation agent is claude-sonnet-4 or Claude with persona prompts. There is no cross-play and no cross-vendor run. |
| R2 | ◐ | HELLO negotiates capabilities and roles; the Verified profile checks credentials and roles against an issuer. Capabilities themselves are self-declared and unverified, and there is no discovery registry. |
| R3 | ○ | No offers, counteroffers, or agreement semantics. The intent and claim lifecycle with TTLs is the closest construct. |
| R4 | ◐ | Role policy, scope freezing, and pre-commit coordinator authorization. There are no scoped, expiring, attenuating tokens and no principal-to-agent delegation. |
| R5 | ◐ | The strongest in the corpus: conflicts are first-class objects with 8 categories, a state machine, arbiter or escalation resolution, and timeout-then-freeze. However, there is no formal termination or deadlock-freedom proof ("No formal verification"). |
| R6 | ● | Normative human override "reachable from any state" plus CONFLICT_ESCALATE. In the demos the arbiter was Claude, not a human. |
| R7 | ◐ | Principal attribution of every operation, conflict, and resolution, plus Lamport watermarks, an audit log, and replay. The log is not tamper-evident and messages are not signed. |
| R8 | ◐ | 66 protocol-enforcement bypass tests, partially covering T1 and T3 at the message level. The coordinator is assumed crash-stop. T2 (prompt injection), T4 (collusion), and T5 are not evaluated. No adversarial LLM agents are used. |

---

## 2. CAPMAS

**Bib:** Rasmus Moorits Veski, Rachid Guerraoui, David Froelicher. "CAPMAS: Capability-Based Delegation of Privileges in Multi-Agent Systems." arXiv:2609.06500 [cs.MA; cs.CR], v1, 6 Sep 2026.
- There is no venue field.
- The HTML renders the name as lowercase "capmas".

### Problem
- Identity passthrough "violates the principle of least privilege" (§1).
- JWTs are "inherently tied to a single request initiator" (§1).
- RFC 8693 token exchange requires an IAM round-trip per hop, making the IAM "an operational bottleneck" (§1).
- The core task is to map natural-language intent to a bounded privilege set and delegate it offline (§4).

### Mechanism
**Semantic scoping (§6.4, §9, §10.4.1).** Privilege derivation is treated as retrieval.
- The encoder is a contrastively fine-tuned BAAI/bge-large-en-v1.5 Siamese encoder, trained with InfoNCE and in-batch negatives.
- Selection uses top-k retrieval with an elbow cutoff at α=0.2.
- The retrieved privileges become `permit` caveats on a root macaroon.

**Macaroons (§2.1, §6.1–6.3).**
- HMAC-chained tokens, with the root secret held only by the IAM.
- Caveats:
  - `rid`, `iss`, `exp`, `aud`, `agent_id`, `permit`, which are verified deterministically
  - `query`, which supports reasoning and traceability
- Default-deny: each agent "must explicitly re-declare the privileges in[sic] intends to delegate."
- The IAM computes "the strict intersection of all accumulated permit caveats" (§6.1).
- Sub-agent delegation works by cloning and attenuating the token (§6.2).

**Verification (§6.3, step 10).** Verification happens once, at the service, through the IAM, in three steps:
1. HMAC chain check.
2. Deterministic checks on expiry, aud/agent_id coherence, and the permit intersection.
3. An LLM-based semantic check, which is "a heuristic defence against prompt injection and logical drift."

Revocation works through `rid` (§7).

**Prototype (§9).** LangGraph + A2A, a Flask IAM and services, pymacaroons, and an MCP proxy for legacy services (A.4).

### Threat model (§4–5, §8, A.3)
- Infrastructure (IAM, services) is "honest-but-curious" and enforces crypto correctly.
- "Agent code is assumed to be non-malicious" (§5).
- "Users are modelled as arbitrary adversaries who may attempt prompt injection" (§5).
- Agent reasoning and external inputs are untrusted. The primary threat is "privilege escalation via non-deterministic execution" (§5).
- The system model is a **single network** with a "centralized trust authority" IAM (§4).
- Malicious agents are only discussed as an extension (§8):
  - Impersonation and forwarding are mitigated by sidecar-injected agent_id, or by asymmetric schemes such as Biscuits in open settings.
  - Collusion (A.3): two colluders tamper with plaintext caveats to mislead an honest intermediary. The paper calls this "a highly specific attack scenario." Two mitigations are proposed: hash-of-state caveats and third-party caveats.

### Evaluation (§10)
**Setup.**
- Apple M3 for benchmarks.
- A10G for encoder training: about 100 minutes, 12,239 pairs.
- The LLM is GPT-oss; GPT-oss-120B is the "Basic Agent" baseline.

**End-to-end (§10.1).** 10 runs of a 3-agent flow.
- 10.8 s average per request, with about 18 LLM calls.
- About 800 ms of non-LLM overhead.

**Micro-benchmarks (Table 1).**
- CAPMAS addCaveat: 0.01 ms, versus 0.30 ms for RFC 8693.
- Verify at N=100: 0.30 ms, versus 0.27 ms for RFC 8693. Signed Nested hits OOM.
- Token size at 100 caveats: 17.4 kB.

**Scaling (§10.3).** 1–25 simulated hops at 20 ms per hop.
- RFC 8693 has about 2× the latency.
- Signed Nested tokens reach about 2 MB at depth 25.

**Headline claims.** 30× faster delegation operations, 2× lower delegation latency, and up to 3× less bandwidth than RFC 8693.

**Scoping (Table 2, k=10).**

| Dataset | Method | Perfect bundle | Complete miss |
|---|---|---|---|
| ASTRA (1,217 tools) | CAPMAS | 90.9% | 2.1% |
| ASTRA (1,217 tools) | Basic Agent | 37.4% | 53.0% |
| XLAM (3,176 tools) | CAPMAS | 92.3% | 3.1% |
| XLAM (3,176 tools) | Basic Agent | context exceeded | — |

- Retrieval takes about 17 ms.
- Privileges are reduced by more than 99.5% compared with full passthrough.
- Relative over-privilege is 73.8–75.6%, but absolute over-privilege is only 0.12–0.47%.

**No attack evaluation.** The paper has no prompt-injection, malicious-agent, or anomaly-detector accuracy experiments.

### Stated limitations (§11, §6.3)
- Plaintext caveats are "a vector for information leakage."
- "enforcing strict memory isolation on a per-delegation basis remains an open challenge."
- Fixed top-k limits "adaptability to query complexity"; "Setting k too low stops legitimate workflows."
- The IAM is "a single point of failure for both trust and operation."
- The "Closed Room" encoder is deliberately fit to a static tool set and must be retrained when new services are onboarded (A.5.2).

### R1–R8
| R | Score | Justification |
|---|---|---|
| R1 | ○ | A single deployment and single network with GPT-oss agents. There is no unseen or cross-vendor partner. |
| R2 | ○ | No capability discovery or verification. `agent_id` records identity in the path but not capability. |
| R3 | ○ | No negotiation. |
| R4 | ● | Macaroon attenuation with `exp`, `aud`, and permit intersection, default-deny, and monotonic reduction. This is the reference R4 mechanism. |
| R5 | ○ | Conflicts are resolved only mechanically (intersection or deny). There are no conflict objects or arbitration. |
| R6 | ○ | No human escalation path; approve or block decisions are automated. |
| R7 | ● (within one IAM trust domain) | The HMAC chain makes the delegation path tamper-evident, and `query` caveats bind intent. Colluders can alter the plaintext view (A.3). The approach is not cross-organizational. |
| R8 | ◐ | The threat model includes prompt-injecting users (T2) and over-scoped agents. Collusion (T4) and impersonation (T3) are discussed analytically. Agent code is assumed non-malicious, and there are no attack experiments. |

---

## 3. Governance Gaps

**Bib:** Richard (Khoon Seang) Kang, Yudho Diponegoro. "Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express." arXiv:2606.31498 [cs.MA; cs.SE], v1, 30 Jun 2026.
- There is no venue field.

### Problem
"Yet coordination is not governance" (§I). The research question is "Do current agent interoperability protocols encode these governance capabilities?"

### Method (§III)
**Taxonomy.** Six dimensions drawn from three sources: organizational theory (Habermas, Robert's Rules), multi-agent systems (Ostrom, electronic institutions), and enterprise standards (SR 11-7, ISO/IEC 42001, EU AI Act).
- G1 Membership
- G2 Deliberation
- G3 Voting
- G4 Dissent preservation
- G5 Human escalation
- G6 Audit/replay: "tamper-evident event logs enabling deterministic reconstruction"

The authors claim the six are "necessary and sufficient for governance (not for all coordination)" (§III-A).

**Rubric.** Each dimension is rated Supported, Partial, or Absent. Ratings are based on what the spec "encodes, not what could theoretically be built on top" (§III-B).

**Specs assessed "as of June 2026" (§V-F):**
- MCP "v1.1": schema 2025-11-25
- A2A v1.0.1: May 2026
- IBM ACP: 2025
- ANP: 2025
- ERC-8004: draft, 2025-08-13

### Results (Table III)
| Protocol | G1 | G2 | G3 | G4 | G5 | G6 | Score (of 12) |
|---|---|---|---|---|---|---|---|
| MCP | A | A | A | A | A | P | 1 |
| A2A | P | A | A | A | A | A | 1 |
| ACP | P | P | A | A | A | A | 2 |
| ANP | A | A | A | A | A | A | 0 |
| ERC-8004 | P | A | A | A | A | P | 2 |

**Notes on the ratings:**
- MCP Elicitation is judged "not governance escalation."
- ACP's negotiation is "bilateral."

**Gap classification (§V-A).**
- A2A gaps are extensible, but "no one has done so."
- MCP gaps are structurally awkward.
- ERC-8004 gaps are scope-limited by on-chain latency.

**Urgency (§V-B).** The authors say the gap "could narrow significantly within 6–12 months."

**Proposal (Fig. 1, Listing 1).** A new Layer-4 "governance" layer with hypothetical primitives:
- ADMIT
- CHALLENGE
- VOTE_BLIND
- DISSENT_RECORD
- ESCALATE, triggered for example when mean confidence is below 0.6
- a hash-chained EVENT

No spec, state machine, or implementation is given.

### Threat model and evaluation
- **No threat model.** The paper does not address Sybil attacks, malicious members, vote manipulation, or key management.
- **No empirical evaluation.** The ratings are the authors' qualitative coding, and there is no inter-rater reliability.
- An AI declaration says Claude was used for literature search and structuring.

### Stated limitations (§V-F)
1. Specs are a June 2026 snapshot.
2. "Partial" requires judgment.
3. The taxonomy is drawn from "Western organizational theory."
4. It assesses what protocols encode, not what can be built on top of them.

### Issues found
- **Inconsistency.** The Abstract and Conclusion say voting and dissent are universally absent, but §IV-G (and Table III) also show G5 human escalation as universally absent.
- **Chronology.** The ERC-8004 "within approximately six months" chronology is questionable against the paper's own references.
- **Possible mis-citation.** "Electronic institutions" is cited to a negotiation paper [11].
- **MPAC is not cited.** This matters because MPAC already provides G5 escalation and a form of G6 audit.

### R1–R8
This is an analysis paper, not a mechanism. I scored what it contributes conceptually; consider coding it as a "survey/analysis" row.

| R | Score | Justification |
|---|---|---|
| R1 | ○ | Not addressed. |
| R2 | ○ | Discovery is mentioned only as protocol background (A2A Agent Cards); no verification. |
| R3 | ○ | Only notes that ACP's bilateral propose/accept/reject/counter exists. G2 and G3 concern deliberation and voting, not bounded negotiation. |
| R4 | ○ | Not addressed (Cedar/AgentCore is mentioned only in passing). |
| R5 | ◐ | Conceptual only: deliberation, voting, and dissent primitives for collective decisions. No termination semantics. |
| R6 | ◐ | Conceptual only: G5 is a defined requirement and ESCALATE is sketched. Finds G5 absent in all five protocols. |
| R7 | ◐ | Conceptual only: G6 requires tamper-evident replay, and a hash-chained EVENT is sketched. |
| R8 | ○ | No threat model. |

---

## 4. Hayler et al. — Zero-Shot Coordination among LLM Agents

**Bib (from the PDF header via Scholar cache):** Adrian Hayler\*, Shashank Reddy\*, Andrei Lupu, Johannes Forkel, Bidipta Sarkar, Siheng Feng, Jakob Foerster. "Zero-Shot Coordination Among LLM Agents." ICLR 2026 Workshop on MALGAI. OpenReview HHPbQlyA7Y. (\* marks equal contribution.)
- **Affiliations:** FLAIR, University of Oxford. Reddy and Sarkar are also at WhiRL.
- **Venue:** The PDF header reads "Published as a conference paper at ICLR 2026 Workshop on MALGAI." Scholar gives "Workshop on Multi-Agent Learning and Its Opportunities in the Era of…, 2026" (truncated). The full workshop name is **UNVERIFIED**; it probably ends in "Generative AI", but I could not confirm that.
- **Second author's name is UNVERIFIED.** Scholar lists "SR Chirra"; the PDF lists "Shashank Reddy". The full name is probably Shashank Reddy Chirra, but check it on OpenReview.
- The OpenReview page itself was not reachable because of a bot check.

### Problem
Prior LLM-coordination work relies on bespoke scaffolds and overly complex tasks such as Overcooked. The authors instead use minimal ZSC environments with generic scaffolds. Their finding: "frontier LLM agents fail to coordinate due to a limited understanding of the underlying coordination challenge" and poor partner reasoning (Abstract).

The motivating examples are explicitly cross-vendor (§1): Waymo, Tesla, and Wayve vehicles, and coding agents built on different LLM providers.

### Mechanism
**Coordination Friendly Definitions (CFDs, §6, Fig. 6).** A natural-language, Dec-POMDP-agnostic "learning rule" placed in every agent's prompt, analogous to a Constitutional AI constitution.

The candidate CFD flags any action that "assumes the existence of arbitrary conventions." It tests this by checking whether swapping signals or flipping roles yields an equivalent policy.

**Scaffolds (§2).**
- Text agents act turn by turn.
- Code agents write a Python joint policy.

### Evaluation
**Environments.** Nine minimal environments:
- Cat & Dog
- Ad-Hoc Conventions
- Ad-Hoc Conventions with permuted signals
- Tiny Hanabi
- Tiny Hanabi Fixed
- Brittle Bridge
- Narrow Tunnel
- 11×11 Matrix Game
- Permuted Levers

Plus the Semantic Selection and Semantic Convention games, and Trampoline–Tiger.

**Models.**
- Grok 4.1 Fast, GPT-5.2, Gemini 3 Pro, Claude Opus 4.5, DeepSeek V3.2.
- GPT-5 mini is used for the reasoning-effort study.

**Cross-play regimes.**
- **XP_seed:** same model, independent runs.
- **XP_LLM:** different models, described as "more closely reflecting real-world coordination scenarios."
- Pairs are scored symmetrically (Eq. 1).
- Episode counts: 100 per code-agent pairing; 10–100 for text agents.

**Metrics.** Joint return, and coordination failure rate, defined as the share of episodes at or below a threshold.

**Results.**

| Result | Without CFD | With CFD |
|---|---|---|
| Fig. 1: Cat & Dog text-agent cross-play cells | −4.00 to 9.00 (Grok→Gemini −4.00) | 5.00 in every cell |
| Table 4: code agents, Cat & Dog (SP / XP_seed / XP_LLM) | 9.75 / 2.41 / −0.51 | 5.50 / 4.55 / 4.46 |
| Table 4: code agents, Ad-Hoc Conventions (same) | 96.33 / 76.19 / 25.49 | 63.12 / 40.22 / 36.23 |
| Table 5: code agents, Cat & Dog XP_LLM failure rate | 0.51 | 0.01 |
| Fig. 5 / Fig. 17: Semantic Selection, Gemini–Claude | 0.000 (self-pairs ≈ 1.0) | 1.010 |

- **Cross-play degrades sharply.** SP exceeds XP_seed, which exceeds XP_LLM.
- **CFD trade-off.** The CFD often lowers self-play scores and sometimes hurts cross-play. Examples: Brittle Bridge, where it produces deadlock, and Matrix Game XP_LLM failure, which rises from .07 to .27.
- **Self-play prompting.** GPT-5.2's reveal rate falls from about 75% to 5% when it is told its partner is an identical copy (§4).
- **Reasoning effort (B.7).** For small models, more reasoning effort lowers cross-play, because the models "hallucinate a shared convention."
- **Brittle code-agent rule.** Code agents use lexicographic ordering, "a brittle ZSC coordination rule" (§4).

### Threat model
None. Every environment is fully cooperative, and the paper assumes "entities are willing to coordinate on such learning rules" (§6). Trust is mentioned only in the sense that natural-language CFDs "foster[] trust" through interpretability.

### Stated limitations (§6–7, B.3–B.4)
- "we do not claim that this candidate CFD resolves coordination failures in general"
- The CFD is narrow: it targets symmetry-breaking and role assignment.
- It can be over-restrictive, for example deadlock in Brittle Bridge.
- It has a weaker effect on code agents.
- The scope of the experiments was limited by resource constraints.

**Internal inconsistency.** §4 says the variable-LLM setting was limited to Cat & Dog, yet Table 4 reports all five models across all environments.

### R1–R8
| R | Score | Justification |
|---|---|---|
| R1 | ● | Explicit cross-play across five frontier models from different providers (XP_LLM) plus XP_seed. This is the most rigorous R1 evidence among LLM papers. |
| R2 | ○ | Not addressed. |
| R3 | ○ | No negotiation; fully cooperative games. |
| R4 | ○ | Not addressed. |
| R5 | ○ | Coordination failure is measured, but no conflict mechanism is proposed. |
| R6 | ○ | Not addressed. |
| R7 | ○ | Not addressed. |
| R8 | ○ | Purely cooperative and assumes willing partners. |

---

## Cross-cutting implications for the SoK
1. **MPAC.** It explicitly claims "defensible against adversarial or buggy participants." Its adversarial evidence, however, is 66 message-level enforcement unit tests, and its live evaluation is single-vendor Claude self-play with a Claude "human" arbiter. This supports F1, F2, and F3; F3 is reinforced by the explicit "No formal verification". The paper should credit MPAC's protocol-level enforcement tests so that it does not overclaim "limited R8".
2. **CAPMAS.** It is single-trust-domain: one IAM, one network, and non-malicious agent code. This supports F4 (no negotiated terms) and adds a point: R4 is solved only *intra-organization*. Cross-organization attenuation (Biscuits, asymmetric signatures) is left as an extension.
3. **Governance Gaps.** It independently confirms that G5 human escalation is absent in MCP, A2A, ACP, ANP, and ERC-8004, but it does not cite MPAC. The SoK can bridge the two papers. Treat it as an analysis row, not a mechanism.
4. **Hayler et al.** It *is* cross-vendor, across 5 providers, but only in cooperative toy games. That is consistent with F5 ("nearly nonexistent outside games"). It strengthens the motivating claim that coordination fails even without adversaries.
