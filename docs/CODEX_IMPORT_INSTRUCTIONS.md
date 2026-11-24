# Import this package into the local Limen repository using Codex

## Target

`/Users/alex.dimarco/repositories/Limen-engineering-harness`

## Instructions to paste into a **local** Codex session

> Open the target folder locally. Before changes, list the existing files and identify the existing Microsoft Copilot skill/prompt. Do not read secret-bearing files or overwrite any existing work. I have downloaded and extracted `Limen-engineering-harness-import.zip` containing `integrations/claude-code`, `integrations/chatgpt`, `integrations/m365-copilot`, `docs`, `AGENTS.md` and `README.md`. Locate the extracted bundle; if it is not in the target folder, ask me for its location. Compare the bundle against the target, preserve different/newer local Copilot content, merge other files safely (backup any conflict before editing), and keep the research paper, implementation plan and Copilot user guide under `docs/`. Initialize Git only if not already initialized; do not configure a remote or push. Run `python3 -m unittest discover -s integrations/claude-code/tests -v` and `python3 integrations/claude-code/tools/limen.py --help`. Validate both ZIP archives with `unzip -t`. If safe and Git identity is already configured, create a local commit; otherwise leave the modifications uncommitted and report why. Report paths, tests, tracked files, `git status`, `git log -1 --oneline` and `git remote -v`. Do not claim skills are installed into ChatGPT, Claude, or Copilot until separately verified there.

## Manual fallback

1. Copy the extracted package's `integrations/` and `docs/` into the target folder. Merge, never replace existing Copilot content sight unseen.
2. Copy `README.md`, `AGENTS.md`, and `.gitignore` after reviewing any same-named files.
3. Use `git init` only if `.git` does not exist; use `git status` to inspect; stage only reviewed files; commit only when desired; do not create a remote.
4. The Claude Code code is a **template integration** under `integrations/claude-code/`. To enable it in another repository, follow that folder's `README.md` and merge its `.claude/` settings instead of replacing them.

## Limits

A ZIP cannot be installed directly into ChatGPT/Claude/Copilot by Git. Each platform has its own installation path. Nothing here performs local filesystem writes until you extract or instruct Codex to merge it.
