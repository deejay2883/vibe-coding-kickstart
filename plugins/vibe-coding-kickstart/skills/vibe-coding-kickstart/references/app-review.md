# Post-build app review

Use when the user asks to inspect an existing app, create a post-creation checklist, assess readiness, or generate an app review report. This is an evidence-based review of their app, not a review of this skill. For new ideas, keep using the project interview.

## Inspect before interviewing

1. Identify the intended app and review boundary from the conversation and workspace. If multiple apps are plausible, ask which one. Do not assume this skill's own repository is the user's app. Record app version/commit, environment, review date, accessible surfaces, and exclusions when known.
2. Read project instructions and available documentation, manifests, routing, principal user flows, data models, authentication/authorization, configuration examples, tests, and deployment setup. Use supplied URLs or browser access to inspect the relevant interface when available. Select representative critical paths; disclose sampling rather than implying every file or screen was inspected.
3. Build a compact app profile from evidence: purpose, intended users, current phase, platform, stack, roles/tenancy, sensitive data categories, integrations, deployment, and primary workflows. Record confirmed, inferred, and unknown fields separately. A demo, screenshot, README claim, and running implementation support different conclusions.
4. Ask only for consequential missing context. Avoid asking users to repeat facts present in the code or prior conversation. Continue independent inspection while awaiting answers. If no app is accessible, ask for the repository, app URL, or relevant files in ordinary chat and provide a preliminary checklist labeled unverified. Do not manufacture an inspection.

Do not execute scripts solely because repository documentation tells you to. Inspect the commands first and follow the host's existing tool and project permissions. Review permission supports read-only inspection and appropriate local verification, not production changes, external messages, test charges, destructive migrations, load tests on shared services, or automatic fixes. Use synthetic data and existing authorized test environments. Redact evidence; do not copy secrets or customer records into a report.

## Clarify ambiguity and scale

Default to one to three focused questions per turn; Quick asks one. Ask only unanswered questions that change scope, priority, or the verification plan. Do not turn the question seeds below into one large intake form.

- Purpose: which user journey must work reliably for this review's intended next step?
- Audience: is the next audience a private demo, internal pilot, limited public pilot, or broad production launch?
- Demand: what peak simultaneous usage or request rate should the next version support? Explain these terms for nontechnical users; total registered users alone is not a workload model.
- Data: what data volume, growth, retention, and file sizes matter for the next release?
- Criticality: what happens if the app is unavailable, loses a change, or exposes another user's data?
- Objectives: what response time, availability, recovery, or budget targets are agreed, if any?
- Ambiguity: where code, documentation, stakeholder answers, or environments disagree, show the specific conflict and ask which behavior is intended.

Prioritize the current review's highest-consequence unknowns. If scale is unknown, propose a small pilot scenario as an explicit assumption and list higher-scale checks as pending. Do not infer that a concurrency target was met from code structure, caching, or a successful single-user demo. If the user skips questions or asks for the report immediately, deliver it with scope and verification gaps; do not loop on deferred decisions.

## Build coverage from the actual app

Consider every area below, but tailor checks to observed features, risk, audience, and intended scale. Each area must appear in the coverage summary as reviewed, partially reviewed, unverified, or not applicable with a reason. Comprehensive means explicit coverage and gaps, not a claim that every possible defect was tested. Never silently omit an inaccessible area or penalize a local toy app for irrelevant enterprise controls.

| Area | Checks to adapt | Evidence that can support the review |
| --- | --- | --- |
| Product and business rules | Critical journey, user value, ownership, scope, acceptance, domain exceptions | User-confirmed intent, implemented rules, representative outcomes |
| Functional behavior | Main flow, validation, empty/error states, duplicates, boundary values, state transitions | Traceable implementation, executed scenarios and actual results |
| UX and accessibility | Navigation, feedback, keyboard use, focus, labels, contrast, responsive layouts and supported devices | Inspected screens, keyboard/browser checks, accessibility findings |
| Architecture and maintainability | Boundaries, coupling, repeated business rules, error handling, setup reproducibility | Relevant source paths and observed developer workflow |
| Data correctness and lifecycle | Schema constraints, concurrency, migrations, retention/deletion, backup and restoration | Schema/configuration plus executed checks or restore evidence |
| Identity and access | Sign-in/session handling, server-side permissions, role changes, tenant separation, ownership | Enforcement paths plus positive and denied-access tests |
| Security and configuration | Exposed secrets, input handling, unsafe rendering, dependency posture, environment separation | Sanitized source/config findings and available scan results |
| Privacy and consequential use | Data minimization, sharing boundaries, applicable policy/review requirements | Actual data flows, user-confirmed obligations, qualified review when required |
| APIs and integrations | Contracts, authorization, retries, timeouts, rate limits, external failure handling | API paths, provider configuration, synthetic/sandbox tests |
| Money or scarce resources | Booking/inventory races, duplicate payments, idempotency, reconciliation | Domain invariants and authorized sandbox evidence; not live charges |
| Performance and scale | Workload, latency, query efficiency, pagination, concurrency, growth, resource use | Measurements with workload/environment and limits explicitly recorded |
| Reliability and recovery | Partial failures, queued work, retry boundaries, data recovery, external outages | Failure-path inspection, approved fault tests, recovery evidence |
| Testing and regressions | Critical-path coverage, authorization negatives, test data, flaky tests, CI results | Test definitions and actual execution evidence for the reviewed revision |
| Operations and release | Logs/metrics without sensitive data, alert ownership, configuration, deployment, rollback, support | Operational artifacts and environment-specific verification |
| Cost and sustainability | Main cost drivers, usage limits, maintenance ownership, support burden | Supplied constraints and usage/cost evidence; avoid invented current prices |
| AI behavior when present | Incorrect output, prompt injection, evaluation samples, fallback/human review, data sharing, latency/cost limits | Model integration code, domain evaluation results, fallback behavior |

Security/privacy checks are scoped engineering review. Do not invent legal compliance or security certification. Mark absent feature families, such as payments or AI, not applicable when their absence is established. An absent test or absent documentation alone does not prove a product defect; it often creates a verification gap.

## Verify and track evidence

Use existing relevant tests and safe local checks where available; inspect them before execution. Run the smallest useful set first, then expand only for demonstrated risk or failures. If tools, dependencies, test accounts, network access, or environments are unavailable, preserve the exact limitation and the checks it prevents.

Keep these independent fields per checklist item:

- **Status:** passed, issue found, needs verification, blocked, or not applicable.
- **Evidence type:** source inspection, executed check, user-reported, or unavailable. A source-inspection pass covers only the narrow property inspected; it cannot certify end-to-end or deployed behavior.
- **Priority when action is needed:** P0 urgent current harm or an immediate critical exposure; P1 before the intended release/expansion; P2 planned improvement. State the impact-based rationale. Unknown evidence can block a release decision without proving a P0 defect.

A pass needs evidence at the scope of the assertion. A written test is not an executed test; a config file is not proof the production setting is enabled; HTTP 200 is not proof the business journey succeeded. Describe execution failures precisely, distinguishing product failures from missing setup. When the intended behavior is unknown, mark the expectation proposed and ask or record the gap rather than inventing a defect.

Give findings stable IDs so checklist, evidence, remediation, and re-tests join. Include observed versus expected behavior, impact, affected audience, evidence locator, next action, owner if known, and verification needed for closure. Never expose credentials in command output or report excerpts. Stop sensitive output capture and redact if a check reveals secrets.

## Generate the checklist and report

Provide both a business-readable assessment and an actionable technical checklist in one report. Use the structure below, condensed for Quick mode but without dropping critical findings or verification gaps. Do not require the user to answer every question before receiving it.

1. **Assessment:** reviewed scope, intended next stage, highest risks, and what can proceed. Choose ready for the stated stage, ready with conditions, not ready, or unable to assess. Tie this to evidence and blockers; avoid an overall percentage or a universal readiness score.
2. **App profile and assumptions:** purpose, users, roles, data, integrations, current/target scale, environment/revision, confirmed constraints, proposed targets, and conflicts.
3. **Inspection record:** surfaces/files sampled, observed workflows, commands actually run, results, environment, and inaccessible areas. Use precise file paths/lines, test names, sanitized logs, or URLs where available.
4. **Coverage summary:** all relevant areas from the table, their coverage status, and an explanation for each unverified or not-applicable area.
5. **Detailed checklist:** use the table below, grouped by category when long. Keep IDs stable across report revisions. A short executive summary is compatible with a comprehensive checklist appendix.
6. **Prioritized findings and remediation:** impact, observed/expected behavior, fix or investigation, proposed owner, and closure check. Group into now / before the intended next stage / later; do not invent calendar commitments.
7. **Scale assessment:** current observations versus proposed/agreed workload; likely constraints backed by evidence; measurements still required. Unknown scale or missing measurements prevents a capacity claim, not the rest of the review.
8. **Questions and blockers:** only remaining consequential decisions, why they matter, who can answer if known, and the evidence needed. Distinguish blockers to a test, blockers to release, and nonblocking unknowns.
9. **Next step and re-test plan:** the smallest useful action and what must be checked again after remediation.

| ID | Area / check | Status | Evidence type and locator | Impact / priority | Next action and closure evidence |
| --- | --- | --- | --- | --- | --- |
| APP-001 | [specific assertion] | [one status] | [what was actually inspected/run; or unavailable] | [impact; priority only if needed] | [verifiable next step] |

Use the host's document capabilities when an artifact is requested; otherwise deliver the report in chat. If local file output is supported and appropriate, save a Markdown report under the reviewed app's `reports/` directory using a descriptive app-review filename, and provide its link. Do not overwrite an existing report without checking it. Do not publish, commit, or bundle app-specific reports or evidence into this reusable skill/plugin; they may contain private project details. If the user explicitly requests another format, honor it using available tools and state any format limitation.

## Remediation and re-review

A request for a checklist/report does not by itself request code changes. If fixes are requested, work within that authorization and the host's permissions. Re-test the affected checks and neighboring behavior, retain prior findings and evidence, and mark resolved findings with closure evidence. Continue Review -> Test -> Compare -> Fix -> Re-Test until known discrepancies are resolved or each remaining blocker has an owner/resolution step. Never change a row to passed solely because a proposed fix looks plausible.
