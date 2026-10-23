"""Distribution checks, not model-behavior tests. Standard library only."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET
import zipfile
import build_plugin

ROOT = Path(__file__).resolve().parents[1]
NAME = 'vibe-coding-kickstart'
GENERATED = ROOT / 'plugins' / NAME


def source_entries():
    paths = [ROOT / 'plugin.json']
    paths += [p for folder in ['skills', 'assets'] for p in (ROOT / folder).rglob('*') if p.is_file()]
    return {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in paths}


class PluginTests(unittest.TestCase):
    def test_manifest_identity_and_listing(self):
        manifest = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['$schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertEqual(manifest['name'], NAME)
        self.assertRegex(manifest['version'], r'^\d+\.\d+\.\d+$')
        self.assertTrue(manifest['author']['name'])
        ui = manifest['extensions']['com.openai']['interface']
        for key, limit in [('displayName', 30), ('shortDescription', 30), ('longDescription', 4000), ('developerName', 80)]:
            self.assertTrue(0 < len(ui[key]) <= limit, key)
        self.assertLessEqual(len(ui['defaultPrompt']), 3)
        self.assertEqual(len(set(ui['defaultPrompt'])), len(ui['defaultPrompt']))
        self.assertTrue(all(0 < len(prompt) <= 128 for prompt in ui['defaultPrompt']))

    def test_compatibility_manifest_parity(self):
        root = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
        compat = json.loads((GENERATED / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        for key in ['name', 'version', 'description', 'author', 'homepage', 'repository']:
            self.assertEqual(root[key], compat[key])
        self.assertEqual(root['extensions']['com.openai']['interface'], compat['interface'])
        self.assertEqual(compat['skills'], './skills/')
        self.assertEqual(root['extensions']['com.openai']['onboardingSkill'], compat['extensions']['com.openai']['onboardingSkill'])
        self.assertNotIn('mcpServers', compat)
        self.assertNotIn('apps', compat)
        self.assertNotIn('hooks', compat)

    def test_catalog_resolves_to_packaged_plugin(self):
        market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
        self.assertEqual(market['name'], NAME + '-community')
        self.assertEqual(len(market['plugins']), 1)
        entry = market['plugins'][0]
        self.assertEqual(entry['name'], NAME)
        self.assertEqual(entry['source']['source'], 'local')
        path = entry['source']['path']
        self.assertTrue(path.startswith('./'))
        self.assertNotIn('..', PurePosixPath(path).parts)
        self.assertEqual((ROOT / path).resolve(), GENERATED.resolve())
        self.assertEqual(entry['policy'], {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'})
        self.assertTrue(entry['category'])

    def test_generated_copy_matches_canonical_source(self):
        for name, content in source_entries().items():
            self.assertEqual((GENERATED / name).read_bytes(), content, name)
        actual = {p.relative_to(GENERATED).as_posix() for p in GENERATED.rglob('*') if p.is_file()}
        self.assertEqual(actual, set(source_entries()) | {'.codex-plugin/plugin.json'})

    def test_plugin_zip_matches_marketplace_snapshot(self):
        with zipfile.ZipFile(ROOT / 'dist' / (NAME + '-codex-plugin.zip')) as z:
            expected = {p.relative_to(GENERATED).as_posix(): p.read_bytes() for p in GENERATED.rglob('*') if p.is_file()}
            self.assertEqual(set(z.namelist()), set(expected))
            for name, data in expected.items():
                self.assertEqual(z.read(name), data, name)

    def test_claude_workflow_is_shared_and_excludes_openai_metadata(self):
        skill = ROOT / 'skills' / NAME
        with zipfile.ZipFile(ROOT / 'dist' / (NAME + '-claude.zip')) as z:
            expected = {NAME + '/' + p.relative_to(skill).as_posix(): p.read_bytes() for p in skill.rglob('*.md')}
            self.assertEqual(set(z.namelist()), set(expected))
            for name, data in expected.items():
                self.assertEqual(z.read(name), data)
            self.assertFalse(any('/agents/' in name for name in z.namelist()))

    def test_archive_integrity_and_paths(self):
        for path in (ROOT / 'dist').glob('*.zip'):
            with self.subTest(path=path.name), zipfile.ZipFile(path) as z:
                self.assertIsNone(z.testzip())
                self.assertEqual(len(z.namelist()), len(set(z.namelist())))
                for name in z.namelist():
                    self.assertFalse(PurePosixPath(name).is_absolute())
                    self.assertNotIn('..', PurePosixPath(name).parts)
                    self.assertNotIn('\\', name)
                    self.assertNotIn(':', name)

    def test_onboarding_and_icons_resolve(self):
        ext = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))['extensions']['com.openai']
        for path in [ext['onboardingSkill'], ext['interface']['logo'], ext['interface']['composerIcon']]:
            self.assertTrue(path.startswith('./'))
            resolved = (GENERATED / path).resolve()
            self.assertTrue(resolved.is_relative_to(GENERATED.resolve()))
            self.assertTrue(resolved.is_file())
        icon = ET.parse(GENERATED / ext['interface']['logo']).getroot()
        self.assertEqual(int(icon.attrib['width']), int(icon.attrib['height']))
        self.assertGreaterEqual(int(icon.attrib['width']), 48)

    def test_local_documentation_links(self):
        for doc in [ROOT / 'README.md', ROOT / 'CODEX-PUBLISHING.md', *(ROOT / 'skills').rglob('*.md')]:
            for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8-sig')):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((doc.parent / target.split('#')[0]).resolve().is_file(), str(doc) + ': ' + target)

    def test_all_distribution_checksums(self):
        sums = json.loads((ROOT / 'dist/sha256.json').read_text(encoding='utf-8'))
        self.assertEqual(set(sums), {p.name for p in (ROOT / 'dist').glob('*.zip')})
        for name, expected in sums.items():
            self.assertEqual(hashlib.sha256((ROOT / 'dist' / name).read_bytes()).hexdigest(), expected)

    def test_rebuild_is_reproducible(self):
        before = {p.name: p.read_bytes() for p in (ROOT / 'dist').glob('*.zip')}
        build_plugin.build()
        after = {p.name: p.read_bytes() for p in (ROOT / 'dist').glob('*.zip')}
        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main(verbosity=2)
