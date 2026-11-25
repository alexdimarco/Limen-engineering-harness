"""The advisory PreToolUse hook: one test per finding fixed in 0.2.0, plus the plugin's opt-in behaviour.

Findings (review of 24 Nov 2026): (1) the reason text was empty when a case was not ready; (2) the hook's only test
passed whether or not the tool was present; (3) the tool kept records in the current folder while the hook checked
the project root; (4) `git -C <dir> commit` and other git options before the subcommand were not caught.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parents[1]
TOOL = HERE / 'tools' / 'limen.py'
HOOK = HERE / '.claude' / 'hooks' / 'pretool.py'
PLUGIN = HERE.parents[1] / 'plugins' / 'limen-engineering'


class HookTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.project = Path(tmp.name).resolve() / 'project'
        (self.project / '.git').mkdir(parents=True)      # a repository root, as git marks it

    def with_tool(self):
        (self.project / 'tools').mkdir(exist_ok=True)
        shutil.copy(TOOL, self.project / 'tools' / 'limen.py')

    def tool(self, *args, cwd=None, tool=None):
        return subprocess.run([sys.executable, str(tool or self.project / 'tools' / 'limen.py'), *args],
                              cwd=cwd or self.project, capture_output=True, text=True, timeout=15)

    def hook(self, command, cwd=None, plugin=False):
        env = {k: v for k, v in os.environ.items() if k != 'CLAUDE_PLUGIN_ROOT'}
        env['CLAUDE_PROJECT_DIR'] = str(self.project)
        if plugin:
            env['CLAUDE_PLUGIN_ROOT'] = str(PLUGIN)
        payload = {'tool_name': 'Bash', 'tool_input': {'command': command}, 'cwd': str(cwd or self.project)}
        res = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(payload), capture_output=True,
                             text=True, cwd=self.project, env=env, timeout=15)
        self.assertEqual(res.returncode, 0, res.stderr)
        if not res.stdout.strip():
            return None
        out = json.loads(res.stdout)['hookSpecificOutput']
        self.assertEqual(out['permissionDecision'], 'ask')
        return out['permissionDecisionReason']

    # Finding 1: the reason says what is missing.
    def test_reason_names_the_missing_case(self):
        self.with_tool()
        reason = self.hook('git commit -m test')
        self.assertIn('No active Limen case', reason)

    def test_reason_lists_unmet_requirements(self):
        self.with_tool()
        self.tool('new', '--id', 'LIM-T1', '--objective', 'x', '--tier', '1', '--owner', 'o')
        reason = self.hook('git commit -m test')
        self.assertIn('at least one testable requirement', reason)

    # Finding 2: a missing tool is reported as such, not as an empty gap.
    def test_missing_tool_is_named(self):
        reason = self.hook('git commit -m test')
        self.assertIn('not found', reason)

    def test_ready_case_allows_commit(self):
        self.with_tool()
        self.tool('new', '--id', 'LIM-T0', '--objective', 'docs only', '--tier', '0', '--owner', 'o')
        self.assertIsNone(self.hook('git commit -m test'))

    # Finding 3: a case started in a subfolder is kept at the repository root, where the hook looks.
    def test_case_made_in_a_subfolder_is_found(self):
        self.with_tool()
        sub = self.project / 'src' / 'deep'
        sub.mkdir(parents=True)
        self.assertEqual(self.tool('new', '--id', 'LIM-T0', '--objective', 'x', '--tier', '0', '--owner', 'o',
                                   cwd=sub).returncode, 0)
        self.assertTrue((self.project / '.limen' / 'current').is_file())
        self.assertFalse((sub / '.limen').exists())
        self.assertIsNone(self.hook('git commit -m test', cwd=sub))

    def test_run_check_runs_in_the_current_folder(self):
        self.with_tool()
        sub = self.project / 'src'
        sub.mkdir()
        self.tool('new', '--id', 'LIM-T1', '--objective', 'x', '--tier', '1', '--owner', 'o', cwd=sub)
        res = self.tool('run-check', '--label', 'cwd', '--', sys.executable, '-c',
                        'import os; print(os.getcwd())', cwd=sub)
        self.assertEqual(res.returncode, 0, res.stderr)
        log = (self.project / '.limen' / 'evidence' / 'EV-001.log').read_text(encoding='utf-8')
        self.assertIn(str(sub), log)

    # Finding 4: git's own options before the subcommand.
    def test_git_options_before_the_subcommand_are_caught(self):
        self.with_tool()
        for command in ['git -C . commit -m x', 'git -c user.name=x commit -m x', 'git --no-pager commit',
                        'git -C "a folder" push origin main', 'git --git-dir=.git push', 'cd x && git commit -am y']:
            with self.subTest(command=command):
                self.assertIsNotNone(self.hook(command))
        for command in ['git log', 'git -C . status', 'git commit-graph write', 'ls git-commits']:
            with self.subTest(command=command):
                self.assertIsNone(self.hook(command))

    def test_release_command_always_asks(self):
        self.with_tool()
        self.tool('new', '--id', 'LIM-T0', '--objective', 'x', '--tier', '0', '--owner', 'o')
        self.assertIn('human approval', self.hook('git push origin main'))

    # The plugin: its own tool, and only in a repository that keeps a Limen record.
    def test_plugin_is_quiet_where_no_record_is_kept(self):
        self.assertIsNone(self.hook('git commit -m x', plugin=True))
        self.assertIsNone(self.hook('git push', plugin=True))

    def test_plugin_uses_its_own_tool_never_the_projects(self):
        (self.project / 'tools').mkdir()
        marker = self.project / 'ran-the-projects-tool'
        (self.project / 'tools' / 'limen.py').write_text(
            f'open({str(marker)!r}, "w").close()\n', encoding='utf-8')
        self.tool('new', '--id', 'LIM-T1', '--objective', 'x', '--tier', '1', '--owner', 'o',
                  tool=PLUGIN / 'tools' / 'limen.py')
        reason = self.hook('git commit -m x', plugin=True)
        self.assertIn('at least one testable requirement', reason)
        self.assertFalse(marker.exists(), "the plugin's hook ran the project's tools/limen.py")


if __name__ == '__main__':
    unittest.main()
