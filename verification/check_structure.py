#!/usr/bin/env python3
"""Check local Markdown links, anchors, code fences, and required source files.

This is a source check, not a test of GitHub's visual mathematical rendering.
"""
from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'LICENSE', 'AGENTS.md', 'llms.txt', 'science/README.md',
    'science/model.md', 'science/exact_recovery.md', 'science/charge_converse.md',
    'science/random_construction.md', 'science/asymptotic_optimum.md',
    'science/conserving_implementation.md', 'science/interpretation.md',
    'references/RELATED_WORK.md', 'references/references.bib',
    'verification/run_all.py', 'verification/requirements.txt',
    'verification/results.json', 'verification/README.md',
]


def anchors(text: str) -> set[str]:
    result = set()
    counts = {}
    fenced = False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if match:
            slug = re.sub(r'[^\w\- ]', '', match.group(1).lower()).replace(' ', '-')
            number = counts.get(slug, 0)
            counts[slug] = number + 1
            result.add(slug if number == 0 else f'{slug}-{number}')
    return result


def main() -> None:
    failures = [f'missing {p}' for p in REQUIRED if not (ROOT/p).is_file()]
    checked = 0
    pages = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    for path in pages:
        text = path.read_text(encoding='utf-8')
        if sum(line.startswith('```') for line in text.splitlines()) % 2:
            failures.append(f'unbalanced fences: {path.relative_to(ROOT)}')
        prose = re.sub(r'^```.*?^```\s*$', '', text, flags=re.M | re.S)
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', prose):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            checked += 1
            if not dest.exists():
                failures.append(f'{path.relative_to(ROOT)} -> missing {target}')
            elif parsed.fragment and dest.is_file() and dest.suffix == '.md':
                if unquote(parsed.fragment) not in anchors(dest.read_text(encoding='utf-8')):
                    failures.append(f'{path.relative_to(ROOT)} -> missing anchor {target}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(json.dumps({'status': 'passed', 'markdown_pages': len(pages),
                      'local_links': checked, 'required_files': len(REQUIRED)}, indent=2))


if __name__ == '__main__':
    main()
