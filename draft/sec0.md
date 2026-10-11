---
title: "SoK: Coordination Among Mutually Untrusting, Independently Developed AI Agents"
subtitle: "Negotiation, Delegation, and Conflict Resolution in Secure Cloud Data Ecosystems"
author: "[AUTHOR NAME, AFFILIATION]"
date: "October 2026 — Draft"
bibliography: refs.bib
link-citations: true
abstract: |
  AI agents built by different vendors and operated by different organizations increasingly need to cooperate in shared cloud data ecosystems: they must discover one another's capabilities, negotiate access, delegate tasks, and resolve conflicts without prior joint training and without fully trusting one another. We call this setting *Mutually Untrusting Ad Hoc Coordination* (MUAC). Relevant research is fragmented across four communities that rarely cite one another: ad hoc teamwork and zero-shot coordination, automated negotiation, agent interoperability protocols, and multi-agent security. We formalize MUAC, give a threat model with five adversary classes, derive eight requirements spanning coordination, security, and governance, and code {{N}} works against them. No work in our corpus demonstrates both coordination with unseen partners and robustness to adversarial peers; conflict resolution remains structural rather than guaranteed; and attenuating delegation exists within single trust domains but is never bound to terms negotiated between principals. An illustrative 540-episode pilot pairs models from three developers in a data-access negotiation. Free-form agents sometimes declared deals on different terms and delegated access anyway; structured agents committed no violations but walked away from 41% of negotiations under a forged-authority attack; and a trusted enforcement gate guaranteed compliance at the cost of reducing benign agreement from 98% to 78%. We conclude with a research agenda centred on negotiated delegation, conflict resolution with guarantees, robustness without refusal, and benchmarks in which agreements carry real authority.
---

