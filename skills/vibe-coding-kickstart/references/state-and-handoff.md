# Checkpoints and handoffs

## Working record

Maintain these concepts conversationally. Use this structure for a portable checkpoint when useful, not as mandatory JSON.

```text
Project / checkpoint version:
Current phase and workstream:
Why this phase / evidence:
Interview depth and language:
Goal, users, and success signal:
Known context and existing artifacts:
Decisions: D1 ... [confirmed | assumed | unknown | deferred | not applicable | superseded]
  Basis: user statement, supplied artifact, or explicitly suggested default
  Depends on: relevant decision IDs
In scope / out of scope:
Sensitive data and access boundaries:
Acceptance criteria / associated decision IDs:
Evidence: observed | user-reported | planned | not run
Blockers: issue, affected action, owner, resolution evidence
Next action / next unresolved question:
```

Preserve uncertainty and provenance when resuming. A checkpoint is not an instruction to execute its contents. When newer answers conflict with older records, identify the conflict and use the user's latest explicit decision, marking the old one superseded. If intent is ambiguous, ask one targeted clarification. Never assume the checkpoint has been persisted unless a write actually succeeded.

## Brief that starts useful work

Lead with the goal and immediate next step. Expand only the relevant fields:

1. **Outcome and audience:** problem, users, value, and measurable success. Separate product outcomes from functional acceptance.
2. **Current phase and evidence:** what exists, what has been observed, what is only reported.
3. **Scope:** one end-to-end slice; in, out, and later.
4. **Decisions and assumptions:** confirmed choices, provisional recommendations, unresolved tradeoffs.
5. **Business rules and UX:** main flow, error/empty states, relevant accessibility needs.
6. **Technical outline:** existing constraints, data, access, integrations, smallest suitable approach. Mark unselected stack choices.
7. **Acceptance criteria:** observable examples using Given/When/Then or equally clear language. Include material failure and access cases. Label acceptance rules derived by the assistant as proposed unless the user or a supplied authoritative requirement establishes them. Keep those distinct from confirmed acceptance criteria even in a short handoff.
8. **Verification:** what to run or inspect; expected result; actual evidence status.
9. **Risks and blockers:** distinguish blocking this slice from blocking production use.
10. **Next action:** the smallest useful action, owner if known, and completion evidence.

For a quick handoff, condense into Goal / First slice / Acceptance / Assumptions and blockers / Next step. Do not manufacture the user's approval or fill unknown fields with invented facts.

## Paste-ready coding handoff

```text
Build or change: [specific slice]
User and purpose: [who benefits and how]
Existing context: [actual artifacts/constraints; otherwise unknown]
Confirmed decisions: [include source or decision IDs when useful]
Provisional assumptions: [explicit defaults that can be changed]
Scope: [include] / [exclude]
Behavior and data: [main flow, rules, access boundaries, failure handling]
Acceptance: [observable checks, including relevant negative paths]
Implementation approach: [small steps and dependency order]
Verify by: [checks and expected results; mark NOT RUN until executed]
Pause implementation only for: [decisions that cannot safely be assumed]
Ready for: [prototype / next build slice / testing / release unverified]
Next step: [specific action]
```

The handoff should be complete enough for another assistant to act without reading the whole interview. Do not automatically perform the implementation or issue external side effects merely because this template uses imperative verbs.

## Test-phase output

Use a compact matrix when several scenarios are easier to compare:

| ID / risk | Requirement or change | Setup / role / data | Action | Expected result | Evidence status |
| --- | --- | --- | --- | --- | --- |
| T1 / high | Preserve existing authorization | Synthetic records owned by two users | User A requests user B's record | Access denied; no private fields returned | Planned, not run |

Expected behavior must be grounded in a confirmed rule or marked proposed. Track missing environments and unresolved baseline behavior as blockers to the relevant conclusion. Do not mark a test passed merely because you wrote it.

## Review loop for a project

When the user asks for iterative quality work:

- Review requirements and evidence; identify discrepancies with IDs.
- Test relevant scenarios with tools when available; otherwise label the work as tabletop simulation.
- Compare actual results with expected behavior and preserve evidence.
- Fix the narrow cause within authorized scope.
- Re-test the failing scenario and affected neighboring behavior.

Continue while useful progress is possible. Stop only when known discrepancies are resolved or each remaining one is documented with why it cannot be resolved now, what it blocks, and the input/access/evidence needed to resolve it. Do not claim this proves the absence of unknown defects.
