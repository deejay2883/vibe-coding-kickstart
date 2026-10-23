"""Build both distributions and the Git-backed Codex marketplace snapshot."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import zipfile
import build_skill

ROOT = Path(__file__).resolve().parents[1]
NAME = 'vibe-coding-kickstart'
GENERATED = ROOT / 'plugins' / NAME


def build():
    manifest = json.loads((ROOT / 'plugin.json').read_text(encoding='utf-8'))
    if manifest['name'] != NAME:
        raise ValueError('Unexpected plugin identity')
    ext = manifest['extensions']['com.openai']
    compatibility = {key: manifest[key] for key in ['name', 'version', 'description', 'author', 'homepage', 'repository']}
    compatibility['skills'] = './skills/'
    compatibility['interface'] = ext['interface']
    compatibility['extensions'] = {'com.openai': {'onboardingSkill': ext['onboardingSkill']}}
    entries = {
        'plugin.json': (json.dumps(manifest, indent=2) + '\n').encode('utf-8'),
        '.codex-plugin/plugin.json': (json.dumps(compatibility, indent=2) + '\n').encode('utf-8'),
    }
    for directory in ['skills', 'assets']:
        for path in sorted((ROOT / directory).rglob('*')):
            if path.is_file():
                if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
                    raise ValueError('External source path')
                rel = path.relative_to(ROOT).as_posix()
                if any(part.startswith('.') or part == '__pycache__' for part in PurePosixPath(rel).parts):
                    raise ValueError('Unexpected hidden or generated file in source')
                entries[rel] = path.read_bytes()
    existing = {p.relative_to(GENERATED).as_posix() for p in GENERATED.rglob('*') if p.is_file()}
    stale = existing - set(entries)
    if stale:
        raise ValueError('Review obsolete generated files before rebuilding: ' + ', '.join(sorted(stale)))
    for name, content in entries.items():
        target = GENERATED / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    build_skill.main()
    archive = ROOT / 'dist' / (NAME + '-codex-plugin.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 23, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, content)
    with zipfile.ZipFile(archive) as z:
        if set(z.namelist()) != set(entries) or z.testzip() is not None:
            raise ValueError('Plugin archive integrity mismatch')
        for name, content in entries.items():
            if z.read(name) != content:
                raise ValueError('Plugin archive content mismatch: ' + name)
    sums = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT / 'dist').glob('*.zip'))}
    (ROOT / 'dist/sha256.json').write_text(json.dumps(sums, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Built and verified {archive.name}: {len(entries)} entries')
    print('Marketplace snapshot matches the plugin ZIP.')


if __name__ == '__main__':
    build()
