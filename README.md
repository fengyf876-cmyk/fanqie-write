# Fanqie Audiobook Story Studio 3.7.0

面向番茄长篇网文的分阶段规划、审核与正文生产系统。

## 核心流程

```text
世界观输入
→ 结构化 Story Bible
→ 全书大纲
→ 大纲内部审计
→ 用户批准
→ 体量/章数锁定
→ 用户批准
→ 全书章纲（按卷生产）
→ 章纲内部审计
→ 导出章纲 DOCX → 用户批准
→ 每次最多3章正文
→ 正文审计
→ 导出三章批次 DOCX → 用户审核
→ 状态回写
```

核心原则：**先规划，后批准，再执行。**

## 章数什么时候确定

- 用户可以一开始提供目标章数或总字数，但此时只作为规划约束。
- 用户未提供时，Skill 在大纲阶段给出预计范围。
- **最终章数在全书大纲批准后、全书章纲生成前锁定。**
- 章数锁定包含目标章数、软浮动范围、硬上限和各卷预算。

## 主要能力

- 世界观原始输入与结构化正典分离
- 全书大纲生成、审计、版本锁定
- 体量与章节预算
- 全书章纲按“第X章：标题 + 连贯剧情梗概”分卷生成与总审，并强制以 DOCX 交付用户审核
- 正文按章纲执行，每次最多3章并合并导出 DOCX
- AI去味、因果、时间线、人物、知识边界、对话、动作/战斗审计
- 伏笔生命周期与人物知识图谱
- 长篇循环/节奏/高潮趋势检查
- 跨会话 Handoff
- 规划变更记录
- 章纲/正文 DOCX 派生交付：A4、宋体10.5pt、1.5倍行距、丛林求生参考版式
- DOCX结构校验 + render逐页视觉QA
- 番茄平台与商业审查参考
- 成人网文吸引力：当前问题、读者问题链、作品承诺与分层兑现
- 成人关系驱动作品的情绪债、关系状态变化、情绪强度与高潮余波
- 人物行为魅力、声音指纹及同人/衍生角色一致性
- 参考样本按 Audience、产品和 Genre 隔离，成人规则不污染 8–12 岁少儿 Profile

## 项目中的唯一真相源

| 内容 | 文件 |
|---|---|
| 用户原始设定 | `source_worldview.md` |
| 世界正典 | `story_bible.md` |
| 本书创作规则 | `book_rules.md` |
| 宏观未来规划 | `planning/book_outline.md` |
| 逐章未来规划 | `planning/chapter_outline/volume_XX.md` |
| 当前实际状态 | `runtime/current_state.md` |
| 伏笔 | `runtime/pending_hooks.md` |
| 人物关系与知识边界 | `runtime/character_matrix.md` |
| 已发生历史 | `runtime/chapter_summaries.md` |

`handoff_current.md` 和 `progress_tracker.md` 是派生视图，不得反向覆盖上述源文件。

## 审计层级

1. Book Outline Audit：这本书整体能不能成立。
2. Chapter Outline Audit：逐章安排会不会在写之前已经崩掉。
3. Draft Audit：实际正文是否执行批准章纲并保持质量和连续性。

3.7.0 在三级审计中继续追问：作品持续给读者什么、为什么不会跳过这一章、正文是否真正形成吸引力与兑现。

## 版本

当前版本：3.7.0


## Reference-sample imitation

When a user supplies a benchmark manuscript, the Skill can measure its chapter size and layout instead of guessing. The bundled Jungle Survival benchmark can propose a long-chapter length/layout, but no numeric per-unit length is auto-locked. Every project may use an exact target, a range, a reference-derived proposal, a Skill recommendation, or flexible length.

## Configurable per-episode/per-chapter length

Per-unit length is a project option, not a global Audience rule. The user may specify any target/range, follow a reference manuscript, ask the Skill to recommend after outline design, or keep the unit length flexible. Final length values are approved during Length Lock.


## DOCX delivery contract

Chapter outlines and manuscript drafts are stored internally as Markdown for versioning and rollback, but every user-facing chapter-outline or manuscript delivery must be a DOCX. The default Word layout follows the supplied Jungle Survival reference: A4, 25.4 mm top/bottom margins, 31.75 mm left/right margins, Songti 10.5 pt body, 1.5 line spacing, centered 22 pt book title, and bold blue 10.5 pt chapter headings. Tracked-change markup from the reference is intentionally not copied.

## 中文字段标识

新项目的字段名、状态项、表格列名和章节元数据默认使用中文标识。CH-001、CHAR-001、HOOK-001、BATCH-001 等稳定 ID 值保留。详见 `references/chinese-labeling-standard.md`。


## 章纲交付格式

用户可见章纲统一使用逐章剧情梗概：`第X章：标题` 后直接用完整中文叙述这一章从开头到结尾的主要内容。内部的功能、伏笔、状态、POV、有声化等字段只作为派生执行元数据，不默认出现在章纲 DOCX。
