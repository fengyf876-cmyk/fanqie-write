#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--project-root', type=Path)
    p.add_argument('input', type=Path)
    a=p.parse_args()
    text=a.input.read_text(encoding='utf-8')
    issues=[]
    if '【旁白】' in text:
        issues.append('通用话本不应给旁白添加【旁白】标签。')
    if '【音效】' in text:
        issues.append('检测到旧式【音效】标签，请按当前话本配置统一。')
    for i,line in enumerate(text.splitlines(),1):
        s=line.strip()
        if not s: continue
        if re.match(r'^【[^】]+】[:：]', s):
            issues.append(f'第{i}行角色/声效标签后出现冒号。')
        if s.count('【') != s.count('】'):
            issues.append(f'第{i}行标签括号不成对。')
    if issues:
        print('校验未通过:')
        for x in issues: print('- '+x)
        return 1
    print('校验通过。')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
