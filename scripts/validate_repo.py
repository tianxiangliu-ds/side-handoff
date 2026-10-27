"""Dependency-free structural checks; does not evaluate model behavior."""
from pathlib import Path
import re
import struct

root = Path(__file__).resolve().parents[1]
skill = (root / 'SKILL.md').read_text(encoding='utf-8-sig')
assert skill.startswith('---\nname: side-handoff\n'), 'Invalid skill name/frontmatter'
assert re.search(r'^description: .+', skill, re.M), 'Missing description'
assert skill.split('---', 2)[1].count('name:') == 1
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8-sig')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        local = target.split('#', 1)[0]
        assert (path.parent / local).exists(), f'{path}: missing {target}'
for name in ('01-extract', '02-merge', '03-confirm'):
    assert (root / 'docs/demos' / f'{name}.html').is_file()
    png = (root / 'docs/images' / f'{name}.png').read_bytes()
    assert png[:8] == b'\x89PNG\r\n\x1a\n'
    width, height = struct.unpack('>II', png[16:24])
    assert width >= 1000 and height >= 600
print('PASS: metadata, local Markdown links, 3 HTML demos and 3 PNG screenshots')
