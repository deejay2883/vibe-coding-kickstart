# Phase routing and question seeds

Use the current phase's section, plus a relevant risk overlay. These are prompts to adapt, not a form to administer. Skip questions already answered. Keep the skill's per-turn question limit.

## Route by evidence

| Phase | Evidence | Useful output |
| --- | --- | --- |
| Discovery | Problem or audience remains unclear | Problem brief and a cheap validation experiment |
| MVP | The problem is known; deciding the smallest valuable scope | One end-to-end user journey, exclusions, success signal |
| Initial build | Implementing the first working slice | Incremental build plan and acceptance criteria |
| Feature/change | Working product needs a specific change | Impact assessment and bounded change handoff |
| Regression/testing | Checking existing behavior after changes | Risk-ranked test matrix and defect triage |
| Release | Preparing to expose a version to real users | Go/no-go criteria, rollout and rollback plan |
| Maintenance/growth | Live use, incidents, feedback, or scaling | Incident/iteration priorities and measurable follow-up |

MVP is a scope decision; initial build is implementation. They can overlap. Ask about what the user is doing next, not which label they know. A feature can be in MVP while the existing core is live. Record a phase per workstream when this distinction matters. If live users are currently affected by an incident, focus first on maintenance/incident triage even when the project is called an MVP. Briefly explain the distinction and retain the MVP scope for later.

## Discovery

Business seeds:
- Who has the problem, and what do they do today to work around it?
- What recent example shows this is painful enough to change?
- Who benefits, who decides, and who pays or owns the internal budget?
- What observable outcome would make exploring this worthwhile?

Technical seeds:
- Could we test the idea with a mockup or manual service before building software?
- Where would the necessary information come from, and do we have permission to use it?
- Must it work on a phone, offline, or inside an existing workplace system?

Enough for next step: a provisional user/problem and an experiment with an observable result. Do not force revenue questions on a personal tool or internal service. Validation means actual evidence; a founder's confidence is a hypothesis.

## MVP

Business seeds:
- What single task should the first user complete from start to finish?
- What could we remove and still deliver that benefit?
- Who will try the first version, and how will we know it helped?
- Which deadline or budget constraint genuinely changes the first version?

Technical seeds:
- What is the smallest information we need to save between visits?
- Is this a private demo, a small pilot, or available to anyone?
- Which roles need different access, if any?
- Which outside system is essential now, and what could be simulated for a demo?

Enough for next step: one user journey, explicit in/out scope, an observable success signal, a data/access assumption, and a testable first slice. Prefer a simple reversible architecture; do not default to microservices or AI because this is vibe coding.

## Initial build

Business seeds:
- Which slice gives the earliest usable feedback?
- What must the user see when a task succeeds or cannot be completed?
- Which business rules and exceptions decide whether a result is correct?

Technical seeds:
- What code or prototype exists, and what must we preserve?
- Are any tools or hosting choices already fixed by your team?
- What entities, relationships, and validation rules support this slice?
- Who can create, view, update, or delete each kind of record?
- How should failures be surfaced and recovered without losing user work?
- What setup, test data, and checks will let another person run this locally?

Enough for next step: boundaries, data model outline, access rules, acceptance criteria, and a runnable verification approach. For a nontechnical user, explain choices in terms of setup effort, cost, privacy, and maintainability. If the stack is unknown, recommend a provisional option only when the requirements warrant it; avoid unverified claims about current pricing or capabilities.

## Feature/change

Business seeds:
- Which user's current behavior should change, and why now?
- What existing behavior must continue to work exactly as it does?
- Is a workaround acceptable while this is delivered?

Technical seeds:
- Which screens, APIs, data, and external systems does the change touch?
- Could old records, clients, permissions, or saved links break?
- Does the change need data migration, a feature flag, or a reversible rollout?

Enough for next step: before/after behavior, unaffected behavior, dependencies, compatibility risks, and acceptance examples. Use a targeted discovery detour for missing context, not a complete restart.

## Regression/testing

Business seeds:
- Which user journeys would cause the most harm if they broke?
- What version or behavior is the accepted baseline?
- Which failures must block a release, and who accepts residual risk?

Technical seeds:
- What changed since the baseline, including dependencies and configuration?
- What environment, devices, roles, and test data represent real use?
- Which automated and manual checks already exist, and what results can we inspect?
- How do we exercise denied access, invalid values, duplicates, retries, and partial failures?
- How will we isolate a flaky test from a real product defect?

Enough for next step: known change scope or explicitly missing baseline, risk-ranked scenarios, expected results, environment, and evidence status. If a baseline is unavailable, propose characterization tests and mark expected behavior as proposed. Never invent pass rates or certify "fully tested" from a test plan. Regression is preservation of intended existing behavior; include new-feature acceptance tests separately.

## Release

Business seeds:
- Who gets this version first, and who handles support?
- What observed result or failure should stop the rollout?
- Who owns the go/no-go decision?

Technical seeds:
- Have the critical journeys and access controls been verified on the release candidate?
- How will we detect failures and return to a known working state?
- Are migrations reversible, and has backup restoration been exercised where data matters?
- What configuration, domain, secrets provisioning, and operational ownership remain unresolved?

Enough for next step: release evidence, decision owner, rollout scope, measurable stop conditions, and feasible recovery. Distinguish rollback of code from recovery of changed data. Missing evidence yields "release readiness unverified" rather than approval.

## Maintenance/growth

Business seeds:
- Which observed pain, support issue, or metric should this iteration improve?
- What is the impact on users right now?
- What evidence would justify expanding rather than simplifying the product?

Technical seeds:
- Where are the failures or bottlenecks actually observed?
- What logs or metrics can be shared safely to narrow the cause?
- What is the lowest-risk reversible mitigation?
- Which maintenance debt creates real operational risk?

Enough for next step: impact, evidence, owner, reversible intervention, and verification. During a live incident, prioritize impact and containment before growth strategy. Start with one focused question about affected users or the failing journey; offer a reversible containment option only as a proposal based on known context. Do not demand a full project brief or assert a root cause before evidence exists. Do not request raw logs containing credentials or personal records.

## Risk overlays (only when relevant)

- Personal or financial data: data minimization, consent/authority, access boundaries, retention/deletion, synthetic test fixtures.
- Multi-user/tenant apps: server-side authorization, tenant separation, ownership changes, cross-role tests.
- Payments/booking/inventory: duplicate submissions, idempotency, reconciliation, concurrent changes, failure between steps.
- AI features: cost/latency constraints, incorrect outputs, fallback to people, evaluation examples, provenance, untrusted input, permissible data sharing. Generated output must not silently become an authoritative decision.
- Offline/mobile: connectivity loss, sync conflicts, accessible interaction, device/browser constraints.
- Public-facing flows: keyboard access, clear errors, abuse controls, account recovery when accounts exist.
- Migration/integration: contracts, version compatibility, rate limits, retries, rollback and data recovery.

Do not overwhelm a toy prototype with every overlay. Explain the concrete consequence that makes an overlay relevant.
