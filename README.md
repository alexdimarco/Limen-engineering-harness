# Limen Engineering Harness — source repository starter

**Package prepared 2026-11-24.** This is a local Git repository *import package*, not a repository already installed or committed on your Mac. It contains three genuine previously created skill implementations and the two existing Limen research papers. Nothing in the ZIP installs plugins, modifies a live project, enables production releases, or grants an AI additional access.

## Contents

| Path | Content | Source status |
|---|---|---|
| `integrations/claude-code/` | Claude Code project instructions, `/limen` skill, Python evidence case recorder, advisory tool hook, six unit tests | Previously created starter, source preserved |
| `integrations/chatgpt/` | ChatGPT Limen Engineering skill, metadata, references and original `skill.zip` | Previously created ChatGPT skill, source preserved |
| `integrations/m365-copilot/` | Microsoft 365 Copilot personal Limen skill, references and original `skill.zip` | Recovered from the earlier Nov 24 Copilot skill artifact, source preserved |
| `docs/` | Working research paper v0.1, implementation plan v0.1, Microsoft 365 Copilot installation/user guide PDF, Codex import instructions | Previously created docs, source preserved |
| `AGENTS.md` | Modest project guidance for Codex while maintaining this repository | New repository scaffolding |
| `SOURCE_MANIFEST.sha256` | Content digests of the files in this ZIP before packaging | New integrity reference, not an authenticity guarantee |

## Install into the local Git repository (Codex)

1. Download this ZIP onto your Mac and extract it to a temporary location.
2. Open **Codex / Local** and choose `/Users/alex.dimarco/repositories/Limen-engineering-harness` as the project folder.
3. Give Codex `docs/CODEX_IMPORT_INSTRUCTIONS.md`, or copy those instructions into the conversation.
4. Inspect any existing files, especially the Copilot prompt or skill that is already in the ChatGPT Project or the local directory. **Do not overwrite it automatically.** Compare the archived Copilot skill in this ZIP against any local/current version and preserve both when different.
5. Ask Codex to copy/merge the integrations and `docs/` into the local repository, run the tests, initialize Git (if needed), and make a local commit. There must be no remote and no push.

You can also extract this package directly as a new repository if the destination is empty. Be careful not to nest `Limen-engineering-harness/Limen-engineering-harness`.

## Validate this package

From this repository root:

```sh
python3 -m unittest discover -s integrations/claude-code/tests -v
python3 integrations/claude-code/tools/limen.py --help
```

The Copilot and ChatGPT ZIPs are installation packages. Their reasoning instructions are **not** security or production deployment gates. Read each integration's instructions for how to install it into its own platform. Claude hooks are advisory; actual access controls, tests, protected CI and human approval must remain independent of the LLM.

## Evidence and scope

The Limen method follows **Experience → Model → Imagine → Branch → Simulate → Integrate → Act → Encounter → Update**, with Yes-And as Receive → Build → Judge. Model-generated descriptions and cross-model agreement are not independent verification. The research papers make a hypothesis about improved engineering quality, not a proven claim of reduced defects.

**Privacy:** Do not put private keys, client-sensitive logs or credentials into the repository. Source package contents were inspected for structure and validated as described; this is not a penetration test or a review of your Mac's existing files.

**Licensing:** No licence is assumed or asserted by this starter package. Review ownership and licensing before distributing it publicly.
