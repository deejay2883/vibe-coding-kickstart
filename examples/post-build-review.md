# Post-build review example

This is an illustrative report for a synthetic app described below. It is not a live host test, security certification, or an audit of this repository.

## Input and the one consequential question

The owner supplies this example function for a shared notes app:

```python
# Supplied example: notes_api.py, lines 1-3
@app.get('/notes/{note_id}')
def read_note(note_id: int):
    return database.get_note(note_id)
```

The owner says this is a pilot for two teams, each with private notes, and no middleware or database authorization applies to this endpoint. The owner also confirms the app has no AI, payments, booking, or inventory features. The reviewer first inspects the snippet and asks: **Should a user be able to read a note owned by the other team?**

Owner: **No. We want 20 simultaneous users eventually, but have done no load testing. Give me the report now.**

## Assessment

**Not ready for the described shared-data pilot.** The supplied read path and explicit absence of other enforcement expose a missing team-access check. A local synthetic-data demonstration can continue. Runtime exploitability, other endpoints, deployment, and capacity remain unverified.

## Profile and boundaries

- Intended users: two teams with private notes (user-confirmed).
- Target: 20 simultaneous users (user-confirmed target, not a measured capacity).
- Evidence: one supplied source snippet and owner statements; no repository, UI, running environment, or test output was accessible.
- Sampling: one endpoint only. No claim about the rest of the app.
- Open questions: how users and team membership are authenticated; target response time; data retention and recovery needs.

## Coverage summary

| Area | Coverage | Reason |
| --- | --- | --- |
| Product and business rules | Partially reviewed | Team isolation clarified; other rules unknown |
| Functional behavior | Partially reviewed | Read path inspected; runtime behavior unverified |
| UX and accessibility | Unverified | No UI access |
| Architecture and maintainability | Partially reviewed | One function only |
| Data correctness and lifecycle | Unverified | Database, migrations and recovery evidence absent |
| Identity and access | Partially reviewed | Missing enforcement in the supplied path; other flows unavailable |
| Security and configuration | Partially reviewed | Narrow authorization finding; no broad security conclusion |
| Privacy and consequential use | Unverified | Private notes known; detailed data flows unavailable |
| APIs and integrations | Partially reviewed | One read endpoint; other contracts unknown |
| Money or scarce resources | Not applicable | Owner confirms plain notes only in this synthetic example |
| Performance and scale | Unverified | 20-user target has no measurements |
| Reliability and recovery | Unverified | No outage or recovery evidence |
| Testing and regressions | Unverified | No executed checks supplied |
| Operations and release | Unverified | No deployment artifacts or release evidence |
| Cost and sustainability | Unverified | No constraints or usage evidence |
| AI behavior | Not applicable | Owner confirms no AI feature in this synthetic example |

## Detailed checklist

| ID | Check | Status | Evidence | Impact / priority | Next action and closure evidence |
| --- | --- | --- | --- | --- | --- |
| APP-001 | Team boundary enforced when reading notes | Issue found | Source inspection: supplied notes_api.py lines 1-3; owner says no other enforcement | P1 before shared pilot; another team's private note could be returned | Enforce caller/team access; execute same-team allow and cross-team denial checks with synthetic records |
| APP-002 | Critical workflow succeeds in the intended environment | Needs verification | No running environment or results | Shared pilot cannot be approved from one snippet | Execute create/read/update paths as intended roles |
| APP-003 | Capacity meets the 20-simultaneous-user target | Needs verification | Target is user-reported; workload and measurements absent | Capacity claim cannot be made | Agree workload and response objective; measure in an authorized representative environment |
| APP-004 | UI supports keyboard and supported devices | Blocked | UI unavailable | UX conclusion cannot be drawn | Provide UI access or test artifacts; inspect relevant controls and error states |
| APP-005 | Restore preserves notes and ownership | Needs verification | No recovery evidence | Potential loss or ownership errors remain unassessed | Establish recovery objective and demonstrate restoration in an appropriate environment |
| APP-006 | AI-specific evaluation applies | Not applicable | Synthetic scenario explicitly excludes AI | No AI-specific action required for this scope | Reassess if an AI feature is added |

Each remaining unverified coverage area needs its own checks when evidence becomes available; this source-limited report does not silently certify them.

## Remediation and next step

Before shared pilot: resolve APP-001 and verify the critical role/journey checks. Owner: unassigned. Proposed closure evidence: test output tied to the reviewed revision, including cross-team denial without private fields being returned.

Next: provide an authorized test environment and the relevant authentication/data paths. Continue unaffected source inspection while preparing that access. No production requests, code changes, or external load tests were performed.

## Re-review

Retain APP-001 until remediation is actually inspected and its closure checks are executed. A proposed authorization fix alone does not turn the finding into a pass. Reassess scope and workload if the pilot audience changes.
