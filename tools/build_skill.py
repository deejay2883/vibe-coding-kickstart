"""Build and validate the Claude installation ZIP. Standard library only."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'vibe-coding-kickstart'
SKILL = ROOT / 'skills' / NAME
DIST = ROOT / 'dist'
ARCHIVE = DIST / (NAME + '-claude.zip')


def main():
    files = sorted(p for p in SKILL.rglob('*') if p.is_file() and 'agents' not in p.relative_to(SKILL).parts)
    if not (SKILL / 'SKILL.md').is_file():
        raise ValueError('Missing skill entrypoint')
    for doc in [ROOT / 'README.md', *SKILL.rglob('*.md')]:
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            resolved = (doc.parent / target.split('#')[0]).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                raise ValueError(f'Invalid local link in {doc.name}: {target}')
    DIST.mkdir(exist_ok=True)
    expected = {}
    for path in files:
        relative = path.relative_to(SKILL)
        if path.is_symlink() or not path.resolve().is_relative_to(SKILL.resolve()):
            raise ValueError('Source must not contain symlinks or external paths')
        if any(part.startswith('.') or part == '__pycache__' for part in relative.parts):
            raise ValueError('Unexpected hidden or generated source file')
        if path.suffix != '.md':
            raise ValueError('This instructions-only skill should contain Markdown files only')
        expected[NAME + '/' + relative.as_posix()] = path.read_bytes()
    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, content in sorted(expected.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 23, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, content)
    with zipfile.ZipFile(ARCHIVE) as z:
        if z.testzip() is not None or set(z.namelist()) != set(expected):
            raise ValueError('Archive integrity or membership mismatch')
        for name, content in expected.items():
            if '..' in PurePosixPath(name).parts or z.read(name) != content:
                raise ValueError('Archive path or content mismatch')
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    (DIST / 'sha256.json').write_text(json.dumps({p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DIST.glob('*.zip'))}, indent=2) + '\n', encoding='utf-8')
    print(f'Built and verified {ARCHIVE.name}: {len(expected)} source files')
    print(f'SHA256: {digest}')
    print('All local documentation links resolved. Native Claude behavior remains unverified.')


if __name__ == '__main__':
    main()
