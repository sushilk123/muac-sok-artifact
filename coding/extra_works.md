# Extra works for the MUAC SoK (verified additions)

Compiled 2026-10-09 to fill gaps in `outline.md`. Every entry below was confirmed to exist in at least one of these sources: Crossref, OpenAlex, the arXiv API, Google Scholar, the publisher's or proceedings' PDF or page, or the standards body's page. The *Verified via* line for each entry names the source. Entries already in the outline are not repeated. Every BibTeX block here also appears in `refs_extra.bib`.

**Access notes:** dblp blocked automated access (Anubis bot check), as did fipa.org (Cloudflare). IEEE Xplore and the ACM DL were not queried directly; venues were confirmed through OpenAlex/Crossref DOIs and Scholar `source:` searches instead.

**Priority legend:** [MUST] means a reviewer will expect it. [SHOULD] means it strengthens an argument. [OPT] means optional.


---

## (c) Classic MAS foundations


### Automated Negotiation: Prospects, Methods and Challenges  `[MUST]`

- **Relevance:** The standard framing of automated negotiation (negotiation protocol, negotiation objects, agents' decision models). Use it to ground R3 and to define what counts as 'structured negotiation' in the coding rubric.
- **Suggested section:** 6.2 Automated negotiation (foundations); §4 R3
- **Verified via:** Crossref DOI; ~925 citations


```bibtex
@article{jennings2001automated,
  author  = {Jennings, Nicholas R. and Faratin, Peyman and Lomuscio, Alessio R. and Parsons, Simon and Wooldridge, Michael J. and Sierra, Carles},
  title   = {Automated Negotiation: Prospects, Methods and Challenges},
  journal = {Group Decision and Negotiation},
  volume  = {10},
  number  = {2},
  pages   = {199--215},
  year    = {2001},
  doi     = {10.1023/A:1008746126376}
}
```


### Argumentation-Based Negotiation  `[MUST]`

- **Relevance:** Argumentation-based negotiation lets agents exchange reasons and not just offers. It is the classic precedent for LLM agents justifying data-access requests, and it supports the argument that today's LLM negotiation benchmarks drop the semantics of commitment and justification.
- **Suggested section:** 6.2; §9 open problem 2 (negotiated delegation)
- **Verified via:** Crossref DOI


```bibtex
@article{rahwan2003abn,
  author  = {Rahwan, Iyad and Ramchurn, Sarvapali D. and Jennings, Nicholas R. and McBurney, Peter and Parsons, Simon and Sonenberg, Liz},
  title   = {Argumentation-Based Negotiation},
  journal = {The Knowledge Engineering Review},
  volume  = {18},
  number  = {4},
  pages   = {343--375},
  year    = {2003},
  doi     = {10.1017/S0269888904000098}
}
```


### Trust in Multi-Agent Systems  `[MUST]`

- **Relevance:** The canonical survey of individual-level and system-level trust in open MAS. It directly backs R2 (verifiable capability claims) and open problem 4 (reputation).
- **Suggested section:** New 6.x 'Trust & reputation' paragraph; R2
- **Verified via:** Crossref DOI


```bibtex
@article{ramchurn2004trust,
  author  = {Ramchurn, Sarvapali D. and Huynh, Dong and Jennings, Nicholas R.},
  title   = {Trust in Multi-Agent Systems},
  journal = {The Knowledge Engineering Review},
  volume  = {19},
  number  = {1},
  pages   = {1--25},
  year    = {2004},
  doi     = {10.1017/S0269888904000116}
}
```


### Review on Computational Trust and Reputation Models  `[MUST]`

- **Relevance:** A widely cited taxonomy of computational trust and reputation models. Use it with Ramchurn et al. to show that the LLM-agent security work (Trust Paradox, Trust-Gated Capability Control) rarely engages with this literature.
- **Suggested section:** New trust & reputation paragraph; R2
- **Verified via:** Crossref DOI


```bibtex
@article{sabater2005review,
  author  = {Sabater, Jordi and Sierra, Carles},
  title   = {Review on Computational Trust and Reputation Models},
  journal = {Artificial Intelligence Review},
  volume  = {24},
  number  = {1},
  pages   = {33--60},
  year    = {2005},
  doi     = {10.1007/s10462-004-0041-5}
}
```


### An Integrated Trust and Reputation Model for Open Multi-Agent Systems  `[SHOULD]`

- **Relevance:** The FIRE model, which combines interaction trust, role-based trust, witness reputation, and certified reputation. Certified reputation is a direct ancestor of the 'verifiable capability claims' in R2.
- **Suggested section:** Trust & reputation; R2/R8
- **Verified via:** Crossref DOI; ~540 citations


```bibtex
@article{huynh2006fire,
  author  = {Huynh, Trung Dong and Jennings, Nicholas R. and Shadbolt, Nigel R.},
  title   = {An Integrated Trust and Reputation Model for Open Multi-Agent Systems},
  journal = {Autonomous Agents and Multi-Agent Systems},
  volume  = {13},
  number  = {2},
  pages   = {119--154},
  year    = {2006},
  doi     = {10.1007/s10458-005-6825-4}
}
```


### Computational Trust and Reputation Models for Open Multi-Agent Systems: A Review  `[OPT]`

- **Relevance:** A follow-up review focused on open MAS. It is optional, but it extends the Sabater & Sierra survey to 2013.
- **Suggested section:** Trust & reputation
- **Verified via:** Crossref/OpenAlex DOI


```bibtex
@article{pinyol2013trust,
  author  = {Pinyol, Isaac and Sabater-Mir, Jordi},
  title   = {Computational Trust and Reputation Models for Open Multi-Agent Systems: A Review},
  journal = {Artificial Intelligence Review},
  volume  = {40},
  number  = {1},
  pages   = {1--25},
  year    = {2013},
  doi     = {10.1007/s10462-011-9277-z},
  note    = {Published online 2011}
}
```


### Agent Communication Languages: Rethinking the Principles  `[SHOULD]`

- **Relevance:** Critiques mentalistic ACL semantics (FIPA/KQML) and argues for social or commitment semantics. This is the right citation for why MCP and A2A, like FIPA, lack verifiable semantics among untrusting parties.
- **Suggested section:** 6.4 Interoperability protocols (historical lineage); resolves the FIPA TODO
- **Verified via:** Crossref DOI


```bibtex
@article{singh1998acl,
  author  = {Singh, Munindar P.},
  title   = {Agent Communication Languages: Rethinking the Principles},
  journal = {Computer},
  volume  = {31},
  number  = {12},
  pages   = {40--47},
  year    = {1998},
  doi     = {10.1109/2.735849}
}
```


### An Ontology for Commitments in Multiagent Systems: Toward a Unification of Normative Concepts  `[MUST]`

- **Relevance:** Social commitments as first-class objects. These give the formal notion of 'who agreed to what' that R7 (auditability) and R5 (conflicts as commitment violations) need.
- **Suggested section:** 6.4/6.6; §4 R5, R7
- **Verified via:** Crossref DOI


```bibtex
@article{singh1999commitments,
  author  = {Singh, Munindar P.},
  title   = {An Ontology for Commitments in Multiagent Systems: Toward a Unification of Normative Concepts},
  journal = {Artificial Intelligence and Law},
  volume  = {7},
  number  = {1},
  pages   = {97--113},
  year    = {1999},
  doi     = {10.1023/A:1008319631231}
}
```


### Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments  `[SHOULD]`

- **Relevance:** Commitment-based protocol specification. It shows that agreement semantics can be flexible and still verifiable, which is a useful contrast to the rigid task lifecycles in A2A and MPAC.
- **Suggested section:** 6.4; R3/R5
- **Verified via:** Crossref DOI (AAMAS 2002)


```bibtex
@inproceedings{yolum2002flexible,
  author    = {Yolum, P{\i}nar and Singh, Munindar P.},
  title     = {Flexible Protocol Specification and Execution: Applying Event Calculus Planning Using Commitments},
  booktitle = {Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS)},
  pages     = {527},
  publisher = {ACM},
  year      = {2002},
  doi       = {10.1145/544862.544867}
}
```


### On the Formal Specification of Electronic Institutions  `[SHOULD]`

- **Relevance:** Electronic institutions: norm-governed spaces for interaction among heterogeneous, self-interested agents. These are the closest classic analogue to a governed cloud data ecosystem, and arguably the pre-LLM version of what MPAC and Governance Gaps propose.
- **Suggested section:** 6.6 Governance; §9 open problem 3
- **Verified via:** Crossref DOI


```bibtex
@incollection{esteva2001electronic,
  author    = {Esteva, Marc and Rodr{\'\i}guez-Aguilar, Juan A. and Sierra, Carles and Garcia, Pere and Arcos, Josep L.},
  title     = {On the Formal Specification of Electronic Institutions},
  booktitle = {Agent Mediated Electronic Commerce: The European AgentLink Perspective},
  series    = {Lecture Notes in Computer Science},
  pages     = {126--147},
  publisher = {Springer},
  year      = {2001},
  doi       = {10.1007/3-540-44682-6_8}
}
```


### FIPA ACL Message Structure Specification  `[MUST]`

- **Relevance:** The standard citation for FIPA ACL.
- **Suggested section:** 6.2/6.4: replaces the 'FIPA ACL (UNVERIFIED)' TODO
- **Verified via:** Google Scholar lists 'FIPA ACL Message Structure Specification', fipa.org/specs/fipa00061, 2002, ~358 citations. fipa.org itself blocked automated access, so the document ID SC00061G and its 'Standard' status follow standard FIPA numbering but were not read directly from the page.


```bibtex
@misc{fipa2002acl,
  author       = {{Foundation for Intelligent Physical Agents}},
  title        = {{FIPA} {ACL} Message Structure Specification},
  howpublished = {FIPA Standard SC00061G},
  year         = {2002},
  url          = {http://www.fipa.org/specs/fipa00061/}
}
```


---

## (a) AI / MAS venues 2024-2026 (negotiation, ad hoc teamwork, conflict resolution, agent networks)


### Large Language Model Assisted Multi-Agent Dialogue for Ontology Alignment  `[SHOULD]`

- **Relevance:** LLM-assisted agents negotiate ontology correspondences through a formal dialogue model. This is relevant to cross-vendor semantic mismatch: agents from different vendors with different schemas.
- **Suggested section:** 6.2 Automated negotiation (LLM + AAMAS); R1/R3
- **Verified via:** Full text read (AAMAS 2024 extended abstract, 3 pp.)


```bibtex
@inproceedings{zhang2024ontologydialogue,
  author    = {Zhang, Shiyao and Dong, Yuji and Zhang, Yichuan and Payne, Terry R. and Zhang, Jie},
  title     = {Large Language Model Assisted Multi-Agent Dialogue for Ontology Alignment},
  booktitle = {Proceedings of the 23rd International Conference on Autonomous Agents and Multiagent Systems (AAMAS), Extended Abstract},
  pages     = {2594--2596},
  publisher = {IFAAMAS},
  year      = {2024}
}
```


### Will Systems of LLM Agents Lead to Cooperation: An Investigation into a Social Dilemma  `[OPT]`

- **Relevance:** LLM-written strategies in the iterated Prisoner's Dilemma. Outcomes depend on prompt dispositions and formatting. This is evidence for the fragility of cooperation among independently prompted agents (R1, F2).
- **Suggested section:** 6.1/6.3 (mixed-motive LLM agents); Axis D
- **Verified via:** KCL repository page (AAMAS 2025, pp. 2786-2788)


```bibtex
@inproceedings{willis2025cooperation,
  author    = {Willis, Richard and Du, Yali and Leibo, Joel Z.},
  title     = {Will Systems of {LLM} Agents Lead to Cooperation: An Investigation into a Social Dilemma},
  booktitle = {Proceedings of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), Extended Abstract},
  pages     = {2786--2788},
  publisher = {IFAAMAS},
  year      = {2025},
  doi       = {10.5555/3709347.3744012}
}
```


### Agentic LLMs and Distributed Constraint Reasoning: A Symbiotic Perspective for Neurosymbolic Multi-Agent Systems  `[SHOULD]`

- **Relevance:** Proposes combining LLM agents with distributed constraint reasoning (DCOP/DisCSP). This is the strongest classic route to conflict resolution with termination and optimality guarantees, which directly supports F3.
- **Suggested section:** 6.6 or new 'Conflict resolution' paragraph; R5; §9 open problem 3
- **Verified via:** Full text read (AAMAS 2026 Blue Sky)


```bibtex
@inproceedings{picard2026dcr,
  author    = {Picard, Gauthier and Yeoh, William and Zivan, Roie},
  title     = {Agentic {LLMs} and Distributed Constraint Reasoning: A Symbiotic Perspective for Neurosymbolic Multi-Agent Systems},
  booktitle = {Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), Blue Sky Ideas Track},
  publisher = {IFAAMAS},
  year      = {2026},
  doi       = {10.65109/YNZM5391}
}
```


### No Future for LLM-based Agents without Formal Dialogue Verification  `[SHOULD]`

- **Relevance:** Argues that LLM-agent dialogues need formal dialogue verification, building on argumentation theory. It supports the claim that negotiation and conflict protocols need provable properties.
- **Suggested section:** 6.2/§9 open problem 3; R3/R5
- **Verified via:** Full text read (AAMAS 2026 Blue Sky)


```bibtex
@inproceedings{nieves2026dialogue,
  author    = {Nieves, Juan Carlos and Br{\"a}nnstr{\"o}m, Andreas and Guerrero, Esteban},
  title     = {No Future for {LLM}-based Agents without Formal Dialogue Verification},
  booktitle = {Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), Blue Sky Ideas Track},
  publisher = {IFAAMAS},
  year      = {2026},
  doi       = {10.65109/JFKY8456}
}
```


### Secret Collusion among AI Agents: Multi-Agent Deception via Steganography  `[MUST]`

- **Relevance:** Formalizes steganographic collusion among LLM agents and shows that monitoring overt messages is not enough. This is the key peer-reviewed citation for T4, which currently has no citation.
- **Suggested section:** §3.2 T4 (colluding coalition); R8
- **Verified via:** OpenAlex (NeurIPS 2024 proceedings DOI); arXiv


```bibtex
@inproceedings{motwani2024collusion,
  author    = {Motwani, Sumeet Ramesh and Baranchuk, Mikhail and Strohmeier, Martin and Bolina, Vijay and Torr, Philip H. S. and Hammond, Lewis and Schroeder de Witt, Christian},
  title     = {Secret Collusion among {AI} Agents: Multi-Agent Deception via Steganography},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {37},
  pages     = {73439--73486},
  year      = {2024},
  doi       = {10.52202/079017-2336},
  eprint    = {2402.07510},
  archivePrefix = {arXiv}
}
```


### The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets  `[SHOULD]`

- **Relevance:** Benchmarks agent-to-agent buyer/seller negotiation between different LLMs and finds behavioral asymmetries and risky outcomes (overpayment, accepting bad deals). This is cross-model negotiation evidence outside games, so it is relevant to F5.
- **Suggested section:** 6.2; Axis D cross-vendor; F5
- **Verified via:** OpenAlex (NLLP 2025 workshop DOI); arXiv


```bibtex
@inproceedings{zhu2025riskygame,
  author    = {Zhu, Shenzhe and Sun, Jiao and Nian, Yi and South, Tobin and Pentland, Alex and Pei, Jiaxin},
  title     = {The Automated but Risky Game: Modeling Agent-to-Agent Negotiations and Transactions in Consumer Markets},
  booktitle = {Proceedings of the Natural Legal Language Processing Workshop (NLLP)},
  publisher = {Association for Computational Linguistics},
  year      = {2025},
  doi       = {10.18653/v1/2025.nllp-1.2},
  eprint    = {2506.00073},
  archivePrefix = {arXiv}
}
```


### Firewalls to Secure Dynamic LLM Agentic Networks  `[MUST]`

- **Relevance:** Dual firewalls for agent-to-agent communication across trust boundaries: incoming messages are projected onto a closed structured protocol, and outgoing data onto the task context. It is evaluated on multi-turn tasks with task-completion metrics.
- **Suggested section:** 6.5 Security; R3/R8; NOVELTY THREAT for F2
- **Verified via:** arXiv (comment: TMLR 2026)


```bibtex
@article{abdelnabi2026firewalls,
  author  = {Abdelnabi, Sahar and Gomaa, Amr and Bagdasarian, Eugene and Kristensson, Per Ola and Shokri, Reza},
  title   = {Firewalls to Secure Dynamic {LLM} Agentic Networks},
  journal = {Transactions on Machine Learning Research},
  year    = {2026},
  eprint  = {2502.01822},
  archivePrefix = {arXiv}
}
```


### ConVerse: Benchmarking Contextual Safety in Agent-to-Agent Conversations  `[SHOULD]`

- **Relevance:** A benchmark of multi-turn conversations between a user's assistant and external service agents (travel, real estate, insurance), with 864 privacy and security attacks. It is the closest existing benchmark to the outline's planned pilot.
- **Suggested section:** 6.3/6.5 Benchmarks; Axis D; R8
- **Verified via:** arXiv only (preprint)


```bibtex
@misc{gomaa2025converse,
  author        = {Gomaa, Amr and Salem, Ahmed and Abdelnabi, Sahar},
  title         = {{ConVerse}: Benchmarking Contextual Safety in Agent-to-Agent Conversations},
  year          = {2025},
  eprint        = {2511.05359},
  archivePrefix = {arXiv}
}
```


### A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems  `[SHOULD]`

- **Relevance:** A protocol-aware security benchmark for A2A multi-agent systems, with a threat taxonomy, six attacks, and paired safety/utility tests on official A2A demos.
- **Suggested section:** 6.4/6.5; R8
- **Verified via:** ICLR 2026 proceedings page


```bibtex
@inproceedings{li2026a2asecbench,
  author    = {Li, Tianhao and Chu, Chuangxin and Zheng, Yujia and Zhang, Bohan and Gong, Neil and Xiao, Chaowei},
  title     = {{A2ASecBench}: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026}
}
```


### Infrastructure for AI Agents  `[SHOULD]`

- **Relevance:** Proposes agent infrastructure for attribution (IDs), interaction (channels), and response (incident reporting, rollback). It is a key reference for R7 and for escalation (R6).
- **Suggested section:** 6.6 Governance; R6/R7
- **Verified via:** arXiv (comment: accepted to TMLR)


```bibtex
@article{chan2025infrastructure,
  author  = {Chan, Alan and Wei, Kevin and Huang, Sihao and Rajkumar, Nitarshan and Perrier, Elija and Lazar, Seth and Hadfield, Gillian K. and Anderljung, Markus},
  title   = {Infrastructure for {AI} Agents},
  journal = {Transactions on Machine Learning Research},
  year    = {2025},
  eprint  = {2501.10114},
  archivePrefix = {arXiv}
}
```


---

## (b) Security venues and agent-protocol security 2024-2026


### SAGA: A Security Architecture for Governing AI Agentic Systems  `[MUST]`

- **Relevance:** User-controlled registration of agents with a Provider that enforces user-defined access policies on inter-agent communication through cryptographically derived access-control tokens, with formal guarantees. This is the strongest peer-reviewed system for multi-user inter-agent authorization.
- **Suggested section:** 6.5 Security/delegation; Axis C; R4/R7; NOVELTY THREAT (partial) for F4
- **Verified via:** OpenAlex NDSS 2026 DOI; arXiv


```bibtex
@inproceedings{syros2026saga,
  author    = {Syros, Georgios and Suri, Anshuman and Ginesin, Jacob and Nita-Rotaru, Cristina and Oprea, Alina},
  title     = {{SAGA}: A Security Architecture for Governing {AI} Agentic Systems},
  booktitle = {Network and Distributed System Security Symposium (NDSS)},
  year      = {2026},
  doi       = {10.14722/ndss.2026.230869},
  eprint    = {2504.21034},
  archivePrefix = {arXiv}
}
```


### SoK: Attack and Defense Landscape of Agentic AI Systems  `[MUST]`

- **Relevance:** A SoK on agentic AI security covering the design space, attacks, and defenses. It must be cited as the nearest security SoK; differentiate it as mostly single-principal and not coordination-centric.
- **Suggested section:** §2 related SoKs; 6.5
- **Verified via:** USENIX Sec '26 prepub PDF read (authors and title)


```bibtex
@inproceedings{kim2026sokagentic,
  author    = {Kim, Juhee and Guo, Wenbo and Song, Dawn},
  title     = {{SoK}: Attack and Defense Landscape of Agentic {AI} Systems},
  booktitle = {35th USENIX Security Symposium (USENIX Security)},
  year      = {2026},
  note      = {Extended version: arXiv:2603.11088}
}
```


### MASLeak: Investigating and Exposing Intellectual Property Leakage Vulnerabilities in Multi-Agent Systems  `[SHOULD]`

- **Relevance:** Black-box extraction of a multi-agent system's topology, system prompts, and tools (~87-92% attack success). This is concrete evidence for T5 and for confidentiality of agent configurations as an asset.
- **Suggested section:** 6.5; §3.2 T5 (curious peer, extraction)
- **Verified via:** USENIX Sec '26 prepub PDF read


```bibtex
@inproceedings{wang2026masleak,
  author    = {Wang, Liwen and Wang, Wenxuan and Wang, Shuai and Li, Zongjie and Ji, Zhenlan and Lyu, Zongyi and Wu, Daoyuan and Cheung, Shing-Chi},
  title     = {{MASLeak}: Investigating and Exposing Intellectual Property Leakage Vulnerabilities in Multi-Agent Systems},
  booktitle = {35th USENIX Security Symposium (USENIX Security)},
  year      = {2026},
  note      = {Preprint: arXiv:2505.12442}
}
```


### Towards Automating Data Access Permissions in AI Agents  `[SHOULD]`

- **Relevance:** Automated permission management for agents, learned from a user study. It is relevant to escalation design (when to ask the human principal) and to data-access decisions.
- **Suggested section:** 6.5/6.7; R4/R6
- **Verified via:** IEEE S&P 2026 DOI (OpenAlex) and arXiv


```bibtex
@inproceedings{wu2026permissions,
  author    = {Wu, Yuhao and Yang, Ke and Roesner, Franziska and Kohno, Tadayoshi and Zhang, Ning and Iqbal, Umar},
  title     = {Towards Automating Data Access Permissions in {AI} Agents},
  booktitle = {IEEE Symposium on Security and Privacy (S\&P)},
  pages     = {2609--2627},
  year      = {2026},
  doi       = {10.1109/SP63933.2026.00018},
  eprint    = {2511.17959},
  archivePrefix = {arXiv}
}
```


### AirGapAgent: Protecting Privacy-Conscious Conversational Agents  `[MUST]`

- **Relevance:** Contextual-integrity data minimization against third-party agents that try to extract user data. It is the canonical peer-reviewed defense for T5.
- **Suggested section:** 6.5; §3.2 T5; R8
- **Verified via:** arXiv comment 'at CCS'24'; ACM DOI via OpenAlex


```bibtex
@inproceedings{bagdasarian2024airgapagent,
  author    = {Bagdasarian, Eugene and Yi, Ren and Ghalebikesabi, Sahra and Kairouz, Peter and Gruteser, Marco and Oh, Sewoong and Balle, Borja and Ramage, Daniel},
  title     = {{AirGapAgent}: Protecting Privacy-Conscious Conversational Agents},
  booktitle = {Proceedings of the ACM SIGSAC Conference on Computer and Communications Security (CCS)},
  year      = {2024},
  doi       = {10.1145/3658644.3690350},
  eprint    = {2405.05175},
  archivePrefix = {arXiv}
}
```


### IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems  `[SHOULD]`

- **Relevance:** A hub-and-spoke execution-isolation architecture for LLM apps and agents with mediated inter-app communication. It is a systems precedent for isolating mutually untrusting components.
- **Suggested section:** 6.5; Axis C; R4
- **Verified via:** OpenAlex NDSS 2025 DOI


```bibtex
@inproceedings{wu2025isolategpt,
  author    = {Wu, Yuhao and Roesner, Franziska and Kohno, Tadayoshi and Zhang, Ning and Iqbal, Umar},
  title     = {{IsolateGPT}: An Execution Isolation Architecture for {LLM}-Based Agentic Systems},
  booktitle = {Network and Distributed System Security Symposium (NDSS)},
  year      = {2025},
  doi       = {10.14722/ndss.2025.241131},
  eprint    = {2403.04960},
  archivePrefix = {arXiv}
}
```


### Defeating Prompt Injections by Design  `[MUST]`

- **Relevance:** CaMeL separates control flow from data flow and attaches capabilities to values. It is the leading capability-based defense against prompt injection, and the natural bridge from object capabilities and macaroons to LLM agents.
- **Suggested section:** 6.5; Axis C (capabilities); R4/R8
- **Verified via:** Google Scholar (IEEE SaTML 2026, ~453 citations); arXiv


```bibtex
@inproceedings{debenedetti2026camel,
  author    = {Debenedetti, Edoardo and Shumailov, Ilia and Fan, Tianqi and Hayes, Jamie and Carlini, Nicholas and Fabian, Daniel and Kern, Christoph and Shi, Chongyang and Terzis, Andreas and Tram{\`e}r, Florian},
  title     = {Defeating Prompt Injections by Design},
  booktitle = {IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)},
  year      = {2026},
  eprint    = {2503.18813},
  archivePrefix = {arXiv}
}
```


### Red-Teaming LLM Multi-Agent Systems via Communication Attacks  `[SHOULD]`

- **Relevance:** The Agent-in-the-Middle attack intercepts and manipulates inter-agent messages in LLM multi-agent systems. It is a peer-reviewed communication-channel attack.
- **Suggested section:** 6.5; §3.2 T1/T2
- **Verified via:** ACL Anthology DOI


```bibtex
@inproceedings{he2025aitm,
  author    = {He, Pengfei and Lin, Yuping and Dong, Shen and Xu, Han and Xing, Yue and Liu, Hui},
  title     = {Red-Teaming {LLM} Multi-Agent Systems via Communication Attacks},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
  pages     = {6726--6747},
  year      = {2025},
  doi       = {10.18653/v1/2025.findings-acl.349}
}
```


### Multi-Agent Systems Execute Arbitrary Malicious Code  `[SHOULD]`

- **Relevance:** Shows that adversarial content can hijack the orchestrators of AutoGen, CrewAI, and similar frameworks into executing arbitrary code (58-90%). Widely cited, but no peer-reviewed venue was found.
- **Suggested section:** 6.5; §3.2 T2
- **Verified via:** arXiv only; ~67 citations on Scholar


```bibtex
@misc{triedman2025masmalicious,
  author        = {Triedman, Harold and Jha, Rishi and Shmatikov, Vitaly},
  title         = {Multi-Agent Systems Execute Arbitrary Malicious Code},
  year          = {2025},
  eprint        = {2503.12188},
  archivePrefix = {arXiv}
}
```


### Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions  `[MUST]`

- **Relevance:** The most cited MCP security survey (~900 citations on Scholar) and a necessary citation for the MCP threat landscape.
- **Suggested section:** 6.4 Protocols; 6.5
- **Verified via:** ACM TOSEM DOI


```bibtex
@article{hou2026mcp,
  author  = {Hou, Xinyi and Zhao, Yanjie and Wang, Shenao and Wang, Haoyu},
  title   = {Model Context Protocol ({MCP}): Landscape, Security Threats, and Future Research Directions},
  journal = {ACM Transactions on Software Engineering and Methodology},
  volume  = {35},
  number  = {10},
  year    = {2026},
  doi     = {10.1145/3796519}
}
```


### Improving Google A2A Protocol: Protecting Sensitive Data and Mitigating Unintended Harms in Multi-Agent Systems  `[SHOULD]`

- **Relevance:** Analyzes A2A's handling of sensitive data (payment and identity tokens) and proposes protocol changes such as short-lived, scoped tokens and explicit consent. It is a peer-reviewed A2A security analysis to set alongside A2ABreak.
- **Suggested section:** 6.4/6.5; R4
- **Verified via:** ACM TOSEM DOI (OpenAlex)


```bibtex
@article{louck2026a2a,
  author  = {Louck, Yedidel and Stulman, Ariel and Dvir, Amit Z.},
  title   = {Improving {Google} {A2A} Protocol: Protecting Sensitive Data and Mitigating Unintended Harms in Multi-Agent Systems},
  journal = {ACM Transactions on Software Engineering and Methodology},
  year    = {2026},
  doi     = {10.1145/3821216}
}
```


### Seven Security Challenges in Cross-Domain Multi-Agent LLM Systems  `[MUST]`

- **Relevance:** A position paper on cross-domain, cross-organization multi-agent LLM security: agents cooperate across organizational boundaries without unified trust. It defines seven challenge categories.
- **Suggested section:** §1/§3; NOVELTY THREAT
- **Verified via:** npj AI 2026 DOI; arXiv


```bibtex
@article{ko2026sevenchallenges,
  author  = {Ko, Ronny and Chung, JiSeong and Zheng, Shuyuan and Xiao, Chuan and Kim, Tae-Wan and Onizuka, Makoto and Shin, Won-Yong},
  title   = {Seven Security Challenges in Cross-Domain Multi-Agent {LLM} Systems},
  journal = {npj Artificial Intelligence},
  volume  = {2},
  year    = {2026},
  doi     = {10.1038/s44387-026-00128-9},
  eprint  = {2505.23847},
  archivePrefix = {arXiv}
}
```


### SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems  `[MUST]`

- **Relevance:** A SoK on multi-agent LLM security across principal boundaries. It covers 197 works with an A-I-R framework (adversary position, interaction interface, system-level risk) and audits 44 benchmarks.
- **Suggested section:** §2 related SoKs; §3; NOVELTY THREAT (highest)
- **Verified via:** arXiv only (Sept 2026)


```bibtex
@misc{yang2026soksafeagents,
  author        = {Yang, Rui and Xu, Junjie and Liu, Zhengyu and Fendley, Neil and Hong, Yang and Li, Ziyang and Cao, Yinzhi},
  title         = {{SoK}: When Safe Agents Fail Together: The Security of Multi Agent {LLM} Systems},
  year          = {2026},
  eprint        = {2609.00595},
  archivePrefix = {arXiv}
}
```


### Lineage: A UMA 2.0 Protocol Extension for Multi-Hop LLM Agent Delegation  `[SHOULD]`

- **Relevance:** Extends UMA 2.0 for multi-hop LLM-agent delegation with provenance (lineage) of delegated authority. It is a concrete OAuth/UMA-family alternative to CAPMAS and macaroons.
- **Suggested section:** 6.5; Axis C; R4; F4
- **Verified via:** IEEE Access DOI


```bibtex
@article{stefanescu2026lineage,
  author  = {{\c{S}}tef{\u{a}}nescu, {\c{S}}tefania and Aciob{\u{a}}ni{\c{t}}ei, Iulian},
  title   = {Lineage: A {UMA} 2.0 Protocol Extension for Multi-Hop {LLM} Agent Delegation},
  journal = {IEEE Access},
  volume  = {14},
  pages   = {104574--104591},
  year    = {2026},
  doi     = {10.1109/ACCESS.2026.3708618}
}
```


---

## (d) Data spaces, data sovereignty, usage control


### Designing Data Spaces: The Ecosystem Approach to Competitive Advantage  `[MUST]`

- **Relevance:** The reference book on data spaces (IDS, Gaia-X, data sovereignty, usage control). Cite it for the 'cloud data ecosystem' environment model.
- **Suggested section:** 6.7 Data ecosystems; §3.1 environment
- **Verified via:** Crossref DOI (Springer, open access)


```bibtex
@book{otto2022designing,
  editor    = {Otto, Boris and ten Hompel, Michael and Wrobel, Stefan},
  title     = {Designing Data Spaces: The Ecosystem Approach to Competitive Advantage},
  publisher = {Springer},
  address   = {Cham},
  year      = {2022},
  doi       = {10.1007/978-3-030-93975-5}
}
```


### International Data Spaces in a Nutshell  `[SHOULD]`

- **Relevance:** A concise description of the IDS architecture (connectors, broker, clearing house, usage policies). The clearing house is a ready-made analogue for R7 audit.
- **Suggested section:** 6.7
- **Verified via:** OpenAlex/Crossref DOI


```bibtex
@incollection{pettenpohl2022ids,
  author    = {Pettenpohl, Heinrich and Spiekermann, Markus and Both, Jan Ruben},
  title     = {International Data Spaces in a Nutshell},
  booktitle = {Designing Data Spaces},
  editor    = {Otto, Boris and ten Hompel, Michael and Wrobel, Stefan},
  publisher = {Springer},
  year      = {2022},
  doi       = {10.1007/978-3-030-93975-5_3}
}
```


### The Road to European Digital Sovereignty with Gaia-X and IDSA  `[SHOULD]`

- **Relevance:** A short overview of Gaia-X and IDSA for European data sovereignty. It is a peer-reviewed anchor for citing Gaia-X; the Gaia-X architecture documents can be added as grey literature.
- **Suggested section:** 6.7
- **Verified via:** Crossref DOI


```bibtex
@article{braud2021gaiax,
  author  = {Braud, Arnaud and Fromentoux, Ga{\"e}l and Radier, Benoit and Le Grand, Olivier},
  title   = {The Road to {European} Digital Sovereignty with {Gaia-X} and {IDSA}},
  journal = {IEEE Network},
  volume  = {35},
  number  = {2},
  pages   = {4--5},
  year    = {2021},
  doi     = {10.1109/MNET.2021.9387709}
}
```


### ODRL Information Model 2.2  `[MUST]`

- **Relevance:** ODRL Information Model 2.2. It is the policy language used by IDS, Gaia-X, and AgentODRL, and the natural target format for 'negotiated terms' in open problem 2.
- **Suggested section:** 6.7; R3/R4 (policy language for negotiated terms)
- **Verified via:** w3.org page read: W3C Recommendation, 15 Feb 2018


```bibtex
@techreport{w3c2018odrl,
  author      = {Iannella, Renato and Villata, Serena},
  title       = {{ODRL} Information Model 2.2},
  institution = {World Wide Web Consortium (W3C)},
  type        = {W3C Recommendation},
  month       = feb,
  year        = {2018},
  url         = {https://www.w3.org/TR/2018/REC-odrl-model-20180215/}
}
```


### The UCONABC Usage Control Model  `[MUST]`

- **Relevance:** The UCON_ABC model, with mutable attributes, ongoing authorization, and obligations. It is the theoretical basis for enforcing retention and usage terms after data access, which matches the outline's retention-conflict scenario.
- **Suggested section:** 6.7; R4/R5 (continuous enforcement and obligations)
- **Verified via:** Crossref DOI; ~730 citations


```bibtex
@article{park2004ucon,
  author  = {Park, Jaehong and Sandhu, Ravi},
  title   = {The {UCON\textsubscript{ABC}} Usage Control Model},
  journal = {ACM Transactions on Information and System Security},
  volume  = {7},
  number  = {1},
  pages   = {128--174},
  year    = {2004},
  doi     = {10.1145/984334.984339}
}
```


### Usage Control in Computer Security: A Survey  `[OPT]`

- **Relevance:** A survey of usage-control models and enforcement. Optional, but it complements Park & Sandhu.
- **Suggested section:** 6.7
- **Verified via:** Crossref DOI


```bibtex
@article{lazouski2010ucsurvey,
  author  = {Lazouski, Aliaksandr and Martinelli, Fabio and Mori, Paolo},
  title   = {Usage Control in Computer Security: A Survey},
  journal = {Computer Science Review},
  volume  = {4},
  number  = {2},
  pages   = {81--99},
  year    = {2010},
  doi     = {10.1016/j.cosrev.2010.02.002}
}
```


### Usage Control Architecture Options for Data Sovereignty in Business Ecosystems  `[SHOULD]`

- **Relevance:** Usage-control architecture options for data sovereignty in IDS-style business ecosystems. It bridges UCON to data spaces.
- **Suggested section:** 6.7; R4
- **Verified via:** Crossref DOI


```bibtex
@article{zrenner2019usagecontrol,
  author  = {Zrenner, Johannes and M{\"o}ller, Frederik and Jung, Christian and Eitel, Andreas and Otto, Boris},
  title   = {Usage Control Architecture Options for Data Sovereignty in Business Ecosystems},
  journal = {Journal of Enterprise Information Management},
  volume  = {32},
  number  = {3},
  pages   = {477--495},
  year    = {2019},
  doi     = {10.1108/JEIM-03-2018-0058}
}
```


---

## (e) Object capabilities, tokens, workload identity


### Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud  `[MUST]`

- **Relevance:** Macaroons: attenuable bearer credentials with contextual and third-party caveats. The outline already names macaroons in F4, but this citation is missing.
- **Suggested section:** 6.5; Axis C; R4
- **Verified via:** Crossref NDSS DOI


```bibtex
@inproceedings{birgisson2014macaroons,
  author    = {Birgisson, Arnar and Politz, Joe Gibbs and Erlingsson, {\'U}lfar and Taly, Ankur and Vrable, Michael and Lentczner, Mark},
  title     = {Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud},
  booktitle = {Network and Distributed System Security Symposium (NDSS)},
  year      = {2014},
  doi       = {10.14722/ndss.2014.23212}
}
```


### The Confused Deputy (or Why Capabilities Might Have Been Invented)  `[SHOULD]`

- **Relevance:** The confused-deputy problem. A prompt-injected agent that holds delegated rights is a confused deputy, and this is the classic motivation for capabilities over ambient authority.
- **Suggested section:** §3.2 (confused-deputy framing of T2); R4
- **Verified via:** Crossref DOI


```bibtex
@article{hardy1988confused,
  author  = {Hardy, Norm},
  title   = {The Confused Deputy (or Why Capabilities Might Have Been Invented)},
  journal = {ACM SIGOPS Operating Systems Review},
  volume  = {22},
  number  = {4},
  pages   = {36--38},
  year    = {1988},
  doi     = {10.1145/54289.871709}
}
```


### Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control  `[SHOULD]`

- **Relevance:** The foundation of object-capability security (POLA, attenuation, revocation patterns), which underlies CAPMAS-style designs.
- **Suggested section:** 6.5; Axis C
- **Verified via:** Google Scholar (JHU dissertation, ~577 citations)


```bibtex
@phdthesis{miller2006robust,
  author = {Miller, Mark Samuel},
  title  = {Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control},
  school = {Johns Hopkins University},
  year   = {2006}
}
```


### OAuth 2.0 Token Exchange  `[MUST]`

- **Relevance:** OAuth 2.0 Token Exchange, including the act/may_act claims for delegation versus impersonation. This is the main standards mechanism for agent on-behalf-of chains.
- **Suggested section:** 6.5; Axis C; R4
- **Verified via:** rfc-editor.org page read (Proposed Standard, 2020). The DOI follows the RFC DOI scheme.


```bibtex
@misc{rfc8693,
  author       = {Jones, Michael B. and Nadalin, Anthony and Campbell, Brian and Bradley, John and Mortimore, Chuck},
  title        = {{OAuth} 2.0 Token Exchange},
  howpublished = {RFC 8693, Internet Engineering Task Force},
  year         = {2020},
  doi          = {10.17487/RFC8693},
  url          = {https://www.rfc-editor.org/info/rfc8693}
}
```


### OAuth 2.0 Rich Authorization Requests  `[SHOULD]`

- **Relevance:** Rich Authorization Requests (authorization_details): structured, fine-grained authorization payloads. It is the most direct standards hook for binding negotiated terms into tokens (open problem 2).
- **Suggested section:** 6.5; R3/R4 (negotiated, fine-grained grants)
- **Verified via:** rfc-editor.org page read (Proposed Standard, 2023)


```bibtex
@misc{rfc9396,
  author       = {Lodderstedt, Torsten and Richer, Justin and Campbell, Brian},
  title        = {{OAuth} 2.0 Rich Authorization Requests},
  howpublished = {RFC 9396, Internet Engineering Task Force},
  year         = {2023},
  doi          = {10.17487/RFC9396},
  url          = {https://www.rfc-editor.org/info/rfc9396}
}
```


### Secure Production Identity Framework for Everyone (SPIFFE) Standard  `[SHOULD]`

- **Relevance:** SPIFFE IDs and SVIDs for cross-domain workload identity. It is relevant to attesting which agent runtime is speaking, separate from the model.
- **Suggested section:** 6.5; R2 (workload identity); §3.2 assumptions
- **Verified via:** GitHub spec read


```bibtex
@misc{spiffe,
  author       = {{SPIFFE Project}},
  title        = {Secure Production Identity Framework for Everyone ({SPIFFE}) Standard},
  howpublished = {Cloud Native Computing Foundation},
  url          = {https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE.md},
  note         = {Accessed 2026-10-09}
}
```


### Solving the Bottom Turtle: A SPIFFE Way to Establish Trust in Your Infrastructure via Universal Identity  `[OPT]`

- **Relevance:** The book-length description of SPIFFE/SPIRE. Optional companion to the spec.
- **Suggested section:** 6.5
- **Verified via:** PDF front matter read (1st ed., 2020, ISBN)


```bibtex
@book{feldman2020bottomturtle,
  author    = {Feldman, Daniel and Fox, Emily and Gilman, Evan and Haken, Ian and Kautz, Frederick and Khan, Umair and Lambrecht, Max and Lum, Brandon and Mart{\'\i}nez Fay{\'o}, Agust{\'\i}n and Nesterov, Eli and Vega, Andr{\'e}s and Wardrop, Michael},
  title     = {Solving the Bottom Turtle: A {SPIFFE} Way to Establish Trust in Your Infrastructure via Universal Identity},
  publisher = {SPIFFE Project / CNCF},
  edition   = {First},
  isbn      = {978-0-578-77737-5},
  year      = {2020},
  url       = {https://spiffe.io/book/}
}
```


---

## Works that threaten the novelty claims

1. **Yang et al. 2026, "SoK: When Safe Agents Fail Together" (arXiv 2609.00595).** This is the highest threat.
   - It is a security SoK on multi-agent LLM systems that explicitly frames failures as crossing *principal boundaries*.
   - It covers 197 works, with adversary positions, interaction interfaces, and a benchmark audit.
   - It overlaps C2 (threat model), R8, and part of C4.
   - Ways to differentiate:
     - It is security-only, with no negotiation, ad hoc teamwork, or coordination-without-joint-training (R1/R3/R5).
     - It has no data-ecosystem setting.
     - It does not do requirement-based scoring across four communities.
   - The SoK should cite it prominently and position itself against it.
2. **Ko et al. 2026, "Seven Security Challenges in Cross-Domain Multi-Agent LLM Systems" (npj AI).**
   - This position paper already frames LLM agents cooperating *across organizational boundaries without unified trust*, which is very close to the MUAC setting (C1).
   - Ways to differentiate: it is an agenda, not a systematization; it has no requirements coding, no negotiation or delegation analysis, and no comparison table.
3. **Abdelnabi et al. 2026 Firewalls (TMLR) and ConVerse (arXiv 2511.05359).**
   - These work on agent-to-agent tasks across trust boundaries and evaluate *both* task completion and attacks.
   - That directly weakens **F2** ("security work evaluated without coordination tasks").
   - ConVerse is also close to the planned pilot study (C6).
   - Recommendation: soften F2 to "rarely", cite these as the exception, and note that they assume a single trusted user-side agent rather than symmetric mutual distrust or negotiated delegation.
4. **Syros et al. 2026, SAGA (NDSS).**
   - It provides user-controlled, cryptographically scoped access-control tokens for inter-agent communication, with formal guarantees.
   - That partially covers R4 and R7 in a multi-user setting and weakens the claim in **F4** that delegation is solved "never combined with" policy.
   - SAGA's policies are set unilaterally by each user, not *negotiated*, so F4 still holds if stated precisely.
5. **Zhu et al. 2025, "The Automated but Risky Game" (NLLP).**
   - It evaluates negotiation between different LLM families in consumer markets.
   - That weakens **F5** ("cross-vendor evaluation nearly nonexistent outside games").
   - Rephrase F5 to "nearly nonexistent with security or authorization in the loop."
6. **Kim, Guo & Song 2026, SoK on agentic AI security (USENIX Security).**
   - It is an overlapping security SoK, though centered on a single agent and its system components.
   - The paper must cite it in related SoKs to avoid a "missed SoK" review comment.
7. **A2ASecBench (ICLR 2026) and Stefanescu & Aciobanitei 2026, Lineage (IEEE Access).** These are lower threats.
   - A2ASecBench is a protocol-aware A2A benchmark with paired safety and utility testing; it partially overlaps F2 and F5.
   - Lineage covers multi-hop agent delegation with provenance; it is relevant to the novelty of open problem 2, but has no negotiation.
