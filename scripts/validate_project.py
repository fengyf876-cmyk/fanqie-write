#!/usr/bin/env python3
import argparse
from pathlib import Path

REQUIRED=['project_status.md','project_profile.md','source_worldview.md','story_bible.md','book_rules.md','style_guide.md','planning/book_outline.md','planning/length_plan.md','runtime/current_state.md','runtime/pending_hooks.md','runtime/character_matrix.md','runtime/chapter_summaries.md','runtime/writing_batches.md']

def main():
    p=argparse.ArgumentParser(); p.add_argument('project_root',type=Path); a=p.parse_args()
    missing=[x for x in REQUIRED if not (a.project_root/x).exists()]
    if missing:
        print('缺少项目文件:'); [print('- '+x) for x in missing]; return 1
    print('项目结构校验通过。'); return 0

if __name__=='__main__':
    raise SystemExit(main())
