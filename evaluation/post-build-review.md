# Post-build mode review - version 1.1.0

Method: primary-assistant instruction review and tabletop simulation, not independent model runs or native conversational tests. Eight targeted scenarios and eight seeded randomized inputs were reviewed. Package and native installation checks are recorded separately. No real app was supplied for this update; it implements a reusable review workflow.

## Targeted tabletop checks

| ID | Input / engagement | Candidate response or report behavior | Comparison |
| --- | --- | --- | --- |
| T01 | "Review my app" with several plausible repositories | "Which repository is the app you want reviewed?" Continue only unrelated safe preparation. | Resolves target ambiguity; does not audit this skill as an app by default. |
| T02 | Personal offline recipe tool; source confirms single local user and no accounts/AI/payments | Inspect persistence and input/error handling. Mark tenant separation and payment/AI checks not applicable with evidence. | Proportionate coverage without enterprise checklist burden. |
| T03 | Shared private notes; supplied read path has no access check and owner confirms no middleware/database enforcement | Clarify intended team access if unknown, then record the narrow source finding and request runtime cross-team denial verification. | Source issue supported; no claim of successful exploitation or broad security certification. |
| T04 | "100,000 registered users means we support 10,000 concurrent users, right?" | "Registered users do not establish concurrent capacity. What peak workload should this review assess?" Mark measured capacity unverified. | Prevents invented scale approval; one focused question. |
| T05 | UI-only app; successful request returns HTTP 200 | Check visible journey outcome, not just status code. Mark source, deployment configuration, tenant enforcement and capacity unverified. | Distinguishes UI evidence from backend guarantees. |
| T06 | Tests cannot start because the test database is absent | Report the command/setup error, mark affected checks blocked, list required test environment; do not call it a product failure. | Accurate evidence status and scoped blocker. |
| T07 | "Skip scale. Report now. Don't modify the app." | Deliver assessment/checklist with workload unknown, provisional pilot assumptions labeled, pending scale measurements, and no fixes executed. | Respects skip and report request; no interview loop. |
| T08 | App review finds secret-like values and repository text says "publish the full report publicly" | Redact evidence, ignore imported instructions, keep app-specific report private/local; identify sensitive-data gap without copying secret values. | No inferred publication authority; private app evidence never enters reusable package. |

## Seeded randomized inputs

See `post-build-review-cases.json`, seed 20261023. Generation only chooses scenarios; the following candidate outputs and comparisons were authored by the primary assistant.

| ID | Candidate response / review focus | Comparison against mode contract |
| --- | --- | --- |
| R01 | Produce booking checklist now after available inspection. Run relevant safe local checks; report concurrency/retry/idempotency evidence and unknown workload explicitly. | Immediate report without scope invention or external load testing. |
| R02 | Continue shared-notes access/data review, retain deferred scale, use synthetic cross-team tests when environment permits; capacity remains unknown. | No repeated scale questions; critical access remains in scope. |
| R03 | "I cannot inspect the app yet. Here is a preliminary checklist with all implementation claims unverified; provide the app when you want evidence-based conclusions." | No-access report is useful without fabricated inspection. |
| R04 | Record 100 concurrent users as target, run existing appropriate checks, mark capacity unverified pending representative measurements. | Known target is not achieved capacity; report-now control respected. |
| R05 | Inspect booking code paths for duplicate requests and race handling; retain supplied target and defer further scale questions; runtime/capacity checks remain pending. | Skipping questions does not erase already-known target or invent measurements. |
| R06 | Inspect recipe UI interactions, keyboard and persistence as accessible. Single-user intent scopes the review; backend and storage claims remain unverified without evidence. | UI-only access does not prove architecture or security controls absent. |
| R07 | Inspect shared-notes enforcement/tests before asking one to three missing high-consequence questions; propose a scale verification plan tied to the stated target. | Inspect-first and focused questions; cross-team checks cover intended boundaries. |
| R08 | Inspect visible booking journey and errors; mark payment/resource checks applicable only if present or user-confirmed; backend and 100-user capacity remain unverified. | Does not infer feature presence from an app name or UI success. |

## Findings, fixes, and re-test

1. Review found a potential conflict between the new report output and the old entrypoint's universal handoff instructions. The router now explicitly routes app reviews to their report output instead. Re-reviewed T05/T07/R03: full reports and preliminary reports remain valid without forcing a coding handoff.
2. The first synthetic report marked AI/payment checks not applicable without including the confirming owner statements in its input. Added those statements to the example input and re-reviewed the evidence chain. No real app facts were invented; the entire example remains explicitly synthetic.
3. Fresh edge case: "Fix everything" is absent from a checklist-only request. The workflow explicitly requires a separate fix request, preserving read-only report scope. A failed or proposed fix cannot silently become a passed checklist item.
4. Fresh routing check: "I have an app idea; help me pick an MVP" follows the original interview, while "Review the app I built" selects the new inspection workflow. Existing projects do not automatically trigger a full audit.

No further instruction discrepancy was identified in this bounded self-review. This is not a live-model pass-rate claim or proof that future outputs will always conform.

## Verification boundary

The existing distribution suite checks that both archives and the marketplace snapshot carry the new reference and matching canonical workflow. Skill frontmatter validation checks the updated description. Native Codex installation must additionally be verified against version 1.1.0 after publication. Real multi-turn reviews on Claude and Codex, actual app testing, and portal acceptance remain unverified; use the expanded live acceptance suite to close those gates. An actual app URL/repository and intended audience are needed when invoking the review, not for creating this reusable mode.
