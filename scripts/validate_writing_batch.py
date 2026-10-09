#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('project_root', type=Path)
    a=p.parse_args()
    root=a.project_root
    batch=root/'runtime'/'writing_batches.md'
    if not batch.exists():
        print('缺少 runtime/writing_batches.md')
        return 1
    text=batch.read_text(encoding='utf-8')
    chapter_tokens=re.findall(r'CH-\d+|第\s*\d+\s*章', text)
    if len(set(chapter_tokens))>3:
        print('当前批次记录超过3章。')
        return 1
    print('批次结构校验通过。')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
