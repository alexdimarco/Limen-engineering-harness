# Changelog

## 0.2.0 (24 November 2026)

Four problems in the advisory commit hook, found in a review on 24 November 2026, each now with a test that failed
before the fix:

1. **The reason was empty.** When a case was not ready, the prompt read "Limen case not ready for commit: ." The tool
   prints its error (such as "No active Limen case") on standard error, and the hook read only standard output. It
   now reads both, and says so plainly when the tool itself is missing.
2. **The hook's test proved nothing.** It passed whether or not `tools/limen.py` was present. It now puts the tool in
   place and checks the reason. New tests cover a missing tool, a ready case and the unmet items.
3. **Records were kept in the current folder.** A case started from a subfolder went into that subfolder's `.limen/`,
   while the hook checked the project root. `limen.py` now keeps records at the repository root: the nearest folder
   upwards with `.limen/` or `.git`. An older `.limen/` in a subfolder is still found first. `run-check` runs its
   command in the current folder, which is now recorded in the evidence log.
4. **`git -C <dir> commit` was not caught.** git's own options before the subcommand (`-C`, `-c`, `--git-dir`,
   `--no-pager` and similar) are now recognized. The review also found that `git commit-graph` was wrongly matched
   as a commit, and it no longer is.

The plugin now includes the hook: a byte-for-byte copy of the starter's, kept identical by a test. In the plugin it
acts only in a repository that already keeps a Limen record (`.limen/`). It runs the plugin's own `limen.py`, never
a project's `tools/limen.py`. Tests: 22, on Python 3.9.6 and 3.12.

## 0.1.0 (24 November 2026)

The `/limen` skill and the `limen.py` case recorder as a Claude Code plugin, with this repository as its marketplace.
No hook.
