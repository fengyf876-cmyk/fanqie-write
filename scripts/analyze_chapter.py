#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def visible_len(text):
    return len(re.sub(r'\s+', '', text))

def main():
    p=argparse.ArgumentParser()
    p.add_argument('input', type=Path)
    a=p.parse_args()
    text=a.input.read_text(encoding='utf-8')
    lines=[x.strip() for x in text.splitlines() if x.strip()]
    dialogue=[x for x in lines if re.match(r'^【[^】]+】', x) and not x.startswith('【声效】')]
    sfx=[x for x in lines if x.startswith('【声效】') or re.match(r'^【[^】]+ 声效】', x)]
    narration=[x for x in lines if x not in dialogue and x not in sfx and not re.match(r'^#{1,6}\s', x)]
    total=visible_len(text)
    d=visible_len(''.join(dialogue))
    n=visible_len(''.join(narration))
    print(f'可见字符数: {total}')
    print(f'台词单元: {len(dialogue)}')
    print(f'旁白单元: {len(narration)}')
    print(f'声效单元: {len(sfx)}')
    if d+n:
        print(f'台词内容占比估算: {d/(d+n):.1%}')
        print(f'旁白内容占比估算: {n/(d+n):.1%}')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
