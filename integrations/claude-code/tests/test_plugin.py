"""Checks for the Claude Code plugin packaging in plugins/limen-engineering/."""
import hashlib
import json
from pathlib import Path
import unittest

REPO = Path(__file__).resolve().parents[3]
STARTER_TOOL = REPO / 'integrations' / 'claude-code' / 'tools' / 'limen.py'
PLUGIN = REPO / 'plugins' / 'limen-engineering'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PluginPackagingTests(unittest.TestCase):
    def test_plugin_tool_is_identical_to_starter_tool(self):
        self.assertEqual(digest(PLUGIN / 'tools' / 'limen.py'), digest(STARTER_TOOL),
                         'plugins/limen-engineering/tools/limen.py must stay a copy of the starter tool')

    def test_plugin_hook_is_identical_to_starter_hook(self):
        starter = REPO / 'integrations' / 'claude-code' / '.claude' / 'hooks' / 'pretool.py'
        self.assertEqual(digest(PLUGIN / 'hooks' / 'pretool.py'), digest(starter),
                         'plugins/limen-engineering/hooks/pretool.py must stay a copy of the starter hook')

    def test_plugin_hook_runs_the_plugins_own_script(self):
        hooks = json.loads((PLUGIN / 'hooks' / 'hooks.json').read_text(encoding='utf-8'))['hooks']
        entries = [h for group in hooks['PreToolUse'] for h in group['hooks']]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['command'], 'python3')
        self.assertEqual(entries[0]['args'], ['${CLAUDE_PLUGIN_ROOT}/hooks/pretool.py'])

    def test_marketplace_entry_matches_plugin_manifest(self):
        market = json.loads((REPO / '.claude-plugin' / 'marketplace.json').read_text(encoding='utf-8'))
        manifest = json.loads((PLUGIN / '.claude-plugin' / 'plugin.json').read_text(encoding='utf-8'))
        entry = next(p for p in market['plugins'] if p['name'] == manifest['name'])
        self.assertEqual((REPO / entry['source']).resolve(), PLUGIN.resolve())

    def test_skill_uses_the_plugins_own_tool(self):
        skill = (PLUGIN / 'skills' / 'limen' / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('"${CLAUDE_PLUGIN_ROOT}/tools/limen.py"', skill)
        # Every call to the tool goes through the plugin root, never a project's own tools/limen.py.
        for line in skill.splitlines():
            if 'limen.py' in line and 'python3' in line:
                self.assertIn('${CLAUDE_PLUGIN_ROOT}/tools/limen.py', line, line)

    def test_skill_runs_only_when_typed(self):
        head = (PLUGIN / 'skills' / 'limen' / 'SKILL.md').read_text(encoding='utf-8').split('---')[1]
        self.assertIn('disable-model-invocation: true', head)


if __name__ == '__main__':
    unittest.main()
