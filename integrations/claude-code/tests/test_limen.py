import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'tools' / 'limen.py'
HOOK = Path(__file__).resolve().parents[1] / '.claude' / 'hooks' / 'pretool.py'


class LimenTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.cwd = Path(self.tmp.name)

    def cli(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(SCRIPT), *args], cwd=self.cwd,
                                capture_output=True, text=True, timeout=15)
        if ok:
            self.assertEqual(result.returncode, 0, (result.stdout, result.stderr))
        else:
            self.assertNotEqual(result.returncode, 0, (result.stdout, result.stderr))
        return result

    def create(self, tier='1'):
        self.cli('new', '--id', 'LIM-DEMO', '--objective', 'Build parser', '--tier', tier,
                 '--owner', 'reviewer')

    def test_tier1_success_and_tamper_detection(self):
        self.create()
        self.cli('check', ok=False)
        self.cli('require', '--text', 'Reject bad input', '--acceptance', 'Test malformed input')
        self.cli('decide', '--choice', 'Small parser', '--rationale', 'simple', '--owner', 'reviewer')
        self.cli('run-check', '--label', 'unit', '--', sys.executable, '-c', 'print("PASS")')
        self.cli('encounter', '--text', 'Observed check passed', '--source', 'EV-001')
        res = self.cli('check')
        self.assertIn('READY FOR REVIEW', res.stdout)
        log = self.cwd / '.limen/evidence/EV-001.log'
        log.write_text(log.read_text() + 'tampered', encoding='utf-8')
        out = self.cli('check', ok=False)
        self.assertIn('digest mismatch', out.stdout)

    def test_failure_is_recorded_not_passed(self):
        self.create()
        self.cli('require', '--text', 'Need tests', '--acceptance', 'Exit 0')
        self.cli('decide', '--choice', 'Option', '--rationale', 'Because')
        self.cli('run-check', '--label', 'negative', '--', sys.executable, '-c', 'raise SystemExit(5)', ok=False)
        self.cli('encounter', '--text', 'Observed failure', '--source', 'EV-001')
        self.assertIn('passing tool-executed check required', self.cli('check', ok=False).stdout)

    def test_tier2_requires_dissent_and_assumptions(self):
        self.create('2')
        self.cli('require', '--text', 'Deny unauthorized', '--acceptance', 'Negative test')
        self.cli('decide', '--choice', 'Boundary check', '--rationale', 'Least privilege', '--owner', 'human')
        self.cli('run-check', '--label', 'test', '--', sys.executable, '-c', 'print("PASS")')
        self.cli('encounter', '--text', 'Observed success', '--source', 'EV-001')
        out = self.cli('check', ok=False)
        self.assertIn('two design alternatives', out.stdout)
        self.cli('assume', '--text', 'Trust tokens only after validation', '--source', 'architecture')
        self.cli('branch', '--text', 'Authorize gateway')
        self.cli('branch', '--text', 'Authorize service')
        self.cli('criticize', '--target', 'ALT-002', '--text', 'Service bypass',
                 '--disposition', 'accepted', '--reason', 'Add negative test')
        self.cli('scenario', '--text', 'Tampered roles', '--expected', 'Forbidden')
        self.cli('check')

    def test_tier3_fails_closed(self):
        self.create('3')
        self.assertIn('cannot authorize critical-risk', self.cli('check', ok=False).stdout)

    def test_correction_must_reference_test(self):
        self.create()
        self.cli('correct', '--finding', 'wrong', '--change', 'fixed', '--evidence', 'EV-001', ok=False)

    def test_hook_asks_when_commit_has_no_case(self):
        # 0.2.0: the tool is in the project, so this tests a missing case, not a missing tool.
        (self.cwd / 'tools').mkdir()
        (self.cwd / 'tools' / 'limen.py').write_bytes(SCRIPT.read_bytes())
        payload = {'tool_name': 'Bash', 'tool_input': {'command': 'git commit -m test'}}
        res = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(payload),
                             capture_output=True, text=True, cwd=self.cwd,
                             env={**os.environ, 'CLAUDE_PROJECT_DIR': str(self.cwd)}, timeout=15)
        self.assertEqual(res.returncode, 0, res.stderr)
        out = json.loads(res.stdout)['hookSpecificOutput']
        self.assertEqual(out['permissionDecision'], 'ask')
        self.assertIn('No active Limen case', out['permissionDecisionReason'])


if __name__ == '__main__':
    unittest.main()
