# Vibe Coding Kickstart

**From idea to build-ready, one question at a time.**

A reusable workflow for Claude and Codex that asks adaptive business and technical questions, from idea and MVP to build, regression testing, and release, then creates an actionable handoff.

[Download the Claude skill ZIP](https://github.com/deejay2883/vibe-coding-kickstart/raw/refs/heads/main/dist/vibe-coding-kickstart-claude.zip) ? [Download the Codex plugin ZIP](https://github.com/deejay2883/vibe-coding-kickstart/raw/refs/heads/main/dist/vibe-coding-kickstart-codex-plugin.zip) ? [Read the skill](skills/vibe-coding-kickstart/SKILL.md) ? [Report feedback](https://github.com/deejay2883/vibe-coding-kickstart/issues)

## Start with your idea

> I want to build a booking app, but I cannot code. Ask one question at a time and help me choose an MVP.

The skill helps clarify who the product is for, what the first useful version should do, and what technical decisions matter now. It then prepares a brief or coding handoff with scope, acceptance criteria, assumptions, and the next step.

It also works on existing projects:

> We changed user permissions. Interview me about regression testing and prepare a test plan.

## Install

### Codex plugin

```text
codex plugin marketplace add deejay2883/vibe-coding-kickstart --ref main
codex plugin add vibe-coding-kickstart@vibe-coding-kickstart-community
```

Start a new session and ask: **Use $vibe-coding-kickstart to interview me about my project.**

This is a GitHub-backed community marketplace. See [Codex installation and directory publishing](CODEX-PUBLISHING.md) for details and official documentation. No MCP server or external service is required.

### Claude

1. Download **vibe-coding-kickstart-claude.zip** using the link above.
2. Open Claude's custom Skills interface, upload the ZIP, and enable the skill.
3. Start a conversation and ask Claude to use **Vibe Coding Kickstart** for your project.

Use the provided skill ZIP, which contains a single `vibe-coding-kickstart/` folder. GitHub's whole-repository ZIP is a different package. Availability depends on your Claude account and workspace settings. [Official Claude instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### Claude Code

Copy `skills/vibe-coding-kickstart/` into your project's `.claude/skills/` directory:

```text
.claude/
  skills/
    vibe-coding-kickstart/
      SKILL.md
      references/
```

Start Claude Code in that project and invoke:

```text
/vibe-coding-kickstart
```

You can also describe the project interview you need in ordinary language. [Official Claude Code skills guide](https://code.claude.com/docs/en/skills).

## Keep it quick or go deeper

| Say | What happens |
| --- | --- |
| Quick | One decision at a time, focused on the next useful step |
| Guided | A few focused questions per turn; the default mode |
| Deep dive | More follow-up on consequences, alternatives, and edge cases |
| Recommend for me | A practical recommendation with its assumptions and tradeoffs |
| Skip | Defer a decision without repeatedly being asked about it |
| Handoff | Get the best current brief immediately, including open decisions |
| Pause / Resume | Get a checkpoint that you can copy into another conversation |

No command syntax is required for these controls in ordinary conversation.

## Questions change with the project

| Phase | Focus |
| --- | --- |
| Discovery | Users, problems, and a small validation experiment |
| MVP | Smallest valuable journey, exclusions, and success signal |
| Initial build | Implementation constraints, data, access, and acceptance criteria |
| Feature changes | Before/after behavior and what must keep working |
| Regression testing | Risk-ranked scenarios, expected results, and evidence gaps |
| Release | Readiness, rollout, stop conditions, and recovery |
| Maintenance / growth | Incidents, observed problems, and measurable improvements |

The skill follows the current workstream rather than forcing every project through a fixed questionnaire. A live incident gets immediate attention even if the product is still called an MVP.

## What the handoff contains

- Goal, audience, and first end-to-end slice.
- Confirmed decisions, provisional assumptions, and deferred questions.
- Relevant business rules, data, and access boundaries.
- Observable acceptance criteria, with assistant-proposed rules labeled.
- Verification steps and their actual evidence status.
- Blockers and the next concrete action.

This is an interview and planning workflow. It does not itself run tests, deploy software, or establish release readiness. Planned checks are never presented as passed tests.

## Validation status

The original workflow received 30 primary-assistant tabletop scenarios and iterative instruction review. Its parent package passed 11 automated structural checks and the skill frontmatter validator. Those were structural checks and self-reviewed simulations, not independent model runs or human research.

This renamed Claude package has been checked for valid frontmatter, complete references, and source-to-ZIP consistency. Native Claude installation, automatic triggering, and live conversational behavior remain unverified.

To help validate it, run the [live acceptance suite](skills/vibe-coding-kickstart/references/evaluation.md) and share an issue with your project phase, a sanitized prompt, the response, and what you expected. Do not include credentials or private customer data.

## Update the skill and plugin

The source lives in `skills/vibe-coding-kickstart/`. After editing it, rebuild and check the installation package from the repository root:

```text
python tools/build_plugin.py
python tools/test_plugin.py
```

The build uses only Python's standard library. It creates both ZIPs, the marketplace snapshot, and SHA-256 checksums. The tests check metadata, content parity, archive integrity, and paths. The original `tools/build_skill.py` also remains available for a Claude-only rebuild. Python is needed for maintaining the package, not for using the installed skill.

Use the **Review -> Test -> Compare -> Fix -> Re-Test** workflow in the evaluation reference. Retain actual outputs and document unresolved blockers.

This is a community-created workflow, not an official Anthropic or OpenAI product. GitHub publication does not list it automatically in OpenAI's plugin directory.
