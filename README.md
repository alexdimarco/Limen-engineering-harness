# Limen Engineering Harness

**The Limen method applied to AI-assisted engineering.** By Alex DiMarco. Version 0.1, November 2026.

This is a way of working with an AI assistant on software and infrastructure changes. Requirements are written so
they can be tested, alternatives and criticism are recorded, tests are actually run, corrections are kept, and every
consequential decision has a named human owner. This repository packages that way of working for Claude Code, ChatGPT
and Microsoft 365 Copilot. It also holds the working paper that argues for it and a plan for building it out.

**Status: a working draft.** Whether this produces better engineering is a hypothesis, not a finding. The working
paper says how it could be tested.

## Use it in Claude Code

```sh
claude plugin marketplace add alexdimarco/Limen-engineering-harness
claude plugin install limen-engineering@limen-engineering-harness
```

Then, in a session, type the skill and the task:

```text
/limen-engineering:limen add input validation to the CSV import
```

(`/limen` also works when no other command has that name.) The skill takes the work through the nine moments, picks a
risk tier, and keeps a case record in `.limen/` in your repository. The record holds the requirements, alternatives,
criticism, the decision, the output of every check it ran (with a SHA-256 digest), what was observed, and the
corrections. Its `check` command says whether the record meets the minimum for its tier.

- The skill runs only when you type it.
- From 0.2.0 the plugin also has an advisory hook. It does nothing until a repository keeps a Limen record
  (`.limen/`). In such a repository it asks you before `git commit` while the case is not ready, saying what is
  missing. It always asks before `git push` and other release commands.
- It needs Python 3 and nothing else: standard library only, tested with 3.9.6 and 3.12.
- Add `.limen/` to your `.gitignore` unless you mean to keep the records.
- To stay on one release, add the marketplace at its tag:
  `claude plugin marketplace add alexdimarco/Limen-engineering-harness#limen-engineering-v0.2.0`.

## What is here

| Folder | What it is | How to use it |
|---|---|---|
| `plugins/limen-engineering/` | The Claude Code plugin: the `/limen` skill and the `limen.py` case recorder | Install as above |
| `integrations/claude-code/` | The copy-in starter: the same tool and skill, a `CLAUDE.md`, an advisory commit hook, the tests | Copy into one repository; see its README |
| `integrations/chatgpt/` | The ChatGPT skill (`skill.zip` and its unpacked text) | Upload the zip through ChatGPT's skill settings |
| `integrations/m365-copilot/` | The Microsoft 365 Copilot personal skill | Follow the installation and user guide in `docs/` |
| `docs/` | The working paper v0.1, the implementation plan v0.1, the Copilot guide (PDF), notes on the first import | Read |

## The method in brief

- **Nine moments:** Experience → Model → Imagine → Branch → Simulate → Integrate → Act → Encounter → Update. They
  loop back, and the objective itself can be revised or abandoned.
- **Yes-And is Receive → Build → Judge:** take a contribution seriously and build on it, then judge it. It is never
  automatic agreement.
- **Every claim is marked** observed, inferred, proposed, unverified or verified. A model's claim is not evidence, and
  neither is another model agreeing with it.
- **Six commitments:** Fidelity, Humility, Correction, Engagement, Care, Charity.
- **Risk tiers** set how much evidence a change needs:

| Tier | Examples | Minimum record | Still needed outside the tool |
|---|---|---|---|
| 0 | Documentation, naming | The objective | Review as appropriate |
| 1 | An ordinary feature or refactor | A requirement, a decision, a passing check the tool ran, an observation | Code review, CI |
| 2 | Sign-in, security, networking, data migration | Tier 1, plus assumptions, two alternatives, criticism answered, an adverse scenario, a named risk owner | Human approval, negative tests, protected CI, threat-model review |
| 3 | Safety, money transfers, irreversible or production security changes | The tool never accepts tier 3 | Independent specialists and a protected release process |

The method comes from [Conversations with Limen](https://conversationswithlimen.ca/), a public record of a long
written collaboration between Alex DiMarco and several language models. The working paper is also published there as
[From Better Answers to Better Engineering](https://conversationswithlimen.ca/better-engineering.html).

## What it is not

- **Not a security control.** The hook (in the plugin and in the starter) is an advisory prompt before `git commit`,
  `git push` and a few deployment commands. It is easy to get around. The real gates (branch protection, required CI checks, approvals)
  have to live outside the model.
- **Not tamper-proof evidence.** The model that writes the records can also edit them. The digests catch accidental
  changes, not deliberate ones, and the records are not audit evidence.
- **Not an approval.** "READY FOR REVIEW" means the record is complete for its tier. It does not mean the change is
  safe to release.

## Changes

See [CHANGELOG.md](CHANGELOG.md). Version 0.2.0 fixed four problems in the commit hook found in review, and put the
hook in the plugin.

## Run the tests

```sh
python3 -m unittest discover -s integrations/claude-code/tests -v
```

There are 22 tests, covering:

- the case recorder;
- the hook, with one test for each problem fixed in 0.2.0;
- the plugin's packaging, including checks that the plugin's `limen.py` and hook stay identical to the starter's.

## How this was made

Parts were drafted with AI assistants at Alex DiMarco's request:

- ChatGPT and Microsoft 365 Copilot (each document's provenance line says which);
- Claude (the Claude Code plugin packaging and this page).

`SOURCE_MANIFEST.sha256` holds the digests of the original package as it was imported on 24 November 2026, and
`docs/CODEX_IMPORT_INSTRUCTIONS.md` describes that import.

## Licence

- **MIT:** the code (the Claude Code plugin and starter, the marketplace file, `.gitignore`).
- **CC BY 4.0:** everything else.

Details are in [LICENSING.md](LICENSING.md). Credit the writing as "Limen Engineering Harness by Alex DiMarco, CC BY 4.0,
https://github.com/alexdimarco/Limen-engineering-harness".

Corrections and criticism are welcome as issues.
