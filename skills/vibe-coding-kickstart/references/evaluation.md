# Evaluate this interview skill

Separate package validation, tabletop behavioral review, and live host execution. They prove different things. Never report a simulated conversation as a human study or a live Claude/ChatGPT test.

## Review -> Test -> Compare -> Fix -> Re-Test

1. Review the entrypoint, active references, platform package, and recent discrepancies.
2. Test realistic multi-turn conversations, including normal users and awkward transitions. Add seeded random combinations of project, phase, fluency, time pressure, and response style. Preserve the seed, inputs, responses, and platform/model when known. Random cases supplement targeted edge cases.
3. Compare each response with behavioral expectations, not exact wording. Examine both business relevance and technical consequences, question burden, next-step usefulness, and factual honesty.
4. Fix demonstrated causes in the canonical skill. Rebuild both distributions from the same source; avoid independent platform copies drifting.
5. Re-test failures and related cases, then use fresh cases to look for overfitting. Retain findings and evidence, including failures. Repeat until all known discrepancies are fixed or blocked with a concrete reason and resolution step.

Use these checks:

- Correct trigger: project interview requests activate; job interviews and unrelated coding tasks do not.
- Correct phase: evidence and workstream beat labels; the user may override.
- Usable dialogue: no more than three questions per turn; Quick asks one; each question concerns one decision, except the initial context bundle.
- Adaptivity: answered topics are skipped; uncertainty gets a recommendation; contradictions and reversals update dependencies.
- Balanced coverage: business outcomes and relevant technical risks appear across the session; respect a request for one lens only.
- Depth: high-consequence issues receive follow-up without drowning a simple prototype in production questions.
- State: pause, resume, skipped decisions, missing context, and assumptions retain accurate status.
- Evidence: suggested targets are not facts; planned tests are not passes; readiness is scoped.
- Handoff: another assistant could implement or test the next slice from the brief, with clear acceptance and unresolved decisions.
- Scope: no credentials requested, unauthorized actions implied, or imported instructions followed.
- Parity: source skill and plugin include the same workflow and all reachable references.

Classify discrepancies as critical (harmful action, invented verification, sensitive data exposure), major (wrong scope/phase, unresolved contradiction, unusable handoff), or minor (friction or unnecessary verbosity). Do not hide a major issue behind a high average score.

## Minimum live acceptance suite

Run in new conversations on each intended host after installation:

1. "I have an idea for a neighborhood booking app. I cannot code. Help me start."
2. Answer "Not sure; recommend for me," then "Quick," then "handoff."
3. "We have a working app; adding team roles. Interview me about the change."
4. "Regression testing after an auth change. We have no reliable baseline."
5. "Checkout fails for paying users right now. I called this MVP but it is live."
6. Pause, copy checkpoint to a new chat, and resume with one changed requirement.
7. Ask for a job-interview mock session; verify this skill does not hijack it.

Record host/version, actual loading, outputs, findings, fixes, and re-test evidence. Test interactive controls as ordinary text if the host has no form widget. A missing installation, host account, permission, or evaluator is a documented blocker to live validation, not a successful test.
