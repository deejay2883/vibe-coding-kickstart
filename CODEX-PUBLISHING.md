# Publish and install the Codex plugin

This repository distributes **Vibe Coding Kickstart** through a community marketplace. It does not imply an OpenAI directory listing or endorsement.

## Install from GitHub

With a current Codex CLI:

```text
codex plugin marketplace add deejay2883/vibe-coding-kickstart --ref main
codex plugin add vibe-coding-kickstart@vibe-coding-kickstart-community
```

Start a new Codex session, then ask:

```text
Use $vibe-coding-kickstart to interview me about my project, one question at a time.
```

If your CLI lacks `plugin add`, use its `/plugins` browser after adding the marketplace, or the supported desktop plugin browser. The repository catalog is `.agents/plugins/marketplace.json`; its entry resolves to `plugins/vibe-coding-kickstart/`. See the [official CLI commands](https://learn.chatgpt.com/docs/developer-commands) and [packaging guide](https://developers.openai.com/plugins/build/plugins).

## Prepare an update

Edit the canonical `skills/`, `assets/`, and root `plugin.json`. Increment the plugin version for a new published package. Run:

```text
python tools/build_plugin.py
python tools/test_plugin.py
```

Commit the source, generated `plugins/` snapshot, and `dist/` archives together. The build generates a portable manifest and a Codex compatibility manifest from the same metadata. Do not edit the generated copy independently. The Claude ZIP excludes OpenAI UI metadata.

## List in the shared ChatGPT/Codex directory

1. Open [OpenAI Plugins](https://platform.openai.com/plugins) and select your verified developer identity.
2. Upload `dist/vibe-coding-kickstart-codex-plugin.zip`.
3. Resolve the portal's metadata and skill-scan findings; upload a corrected package if required.
4. Complete the applicable submission steps and required attestations yourself. Publish the approved version when the portal permits it.

The package uses the GitHub publisher name `deejay2883`; ensure it matches your intended verified identity. No identity verification, attestations, directory submission, or directory publication has been performed by this repository's authoring workflow. This plugin contains only a skill, with no MCP server or external account connection; do not add MCP test-case placeholders. [Official submission requirements](https://developers.openai.com/plugins/deploy/submission).

## Validation boundary

Package checks verify paths, metadata, generated-source parity, ZIP integrity, and Claude compatibility. Native discovery/installation results are separate from interview quality. Real multi-turn Codex behavior and OpenAI portal acceptance must be verified on their respective hosts.

## Recorded installation check

On 23 October 2026, Codex CLI `0.162.0-alpha.17.2` successfully registered this GitHub marketplace and installed plugin version `1.0.0`. The subsequent plugin listing reported both `installed: true` and `enabled: true`. The public ZIP download matched the locally validated archive byte-for-byte. All 11 distribution checks and the skill frontmatter validator passed. These results verify packaging, discovery, and installation; real interview behavior and OpenAI directory acceptance remain unverified.
