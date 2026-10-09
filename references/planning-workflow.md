# 规划工作流与阶段状态机

## 状态顺序

```text
PROFILE_RESOLUTION
→ PROFILE_USER_REVIEW（仅推断时）
→ WORLDVIEW_INTAKE
→ BOOK_OUTLINE_DRAFTING
→ BOOK_OUTLINE_INTERNAL_REVIEW
→ BOOK_OUTLINE_USER_REVIEW
→ LENGTH_LOCK
→ CHAPTER_OUTLINE_DRAFTING
→ CHAPTER_OUTLINE_INTERNAL_REVIEW
→ CHAPTER_OUTLINE_USER_REVIEW
→ WRITING
→ COMPLETED
```

## Profile 门

### 用户明确提供
直接生成 `project_profile.md` 并标 `approved`，无需重复确认。

### Skill 推断
生成识别结果，进入 `PROFILE_USER_REVIEW`。用户确认后才可继续。

### Profile 改变
改变受众、年龄或有声产品形态会影响整套写作规则，属于重大变更，必须走 Plan Change。

## 大纲门

只有 Profile 已批准且用户明确批准大纲，才能把 `book_outline.status` 改为 `approved`。

## 体量门

大纲批准后确定目标字数、目标章/集数、软范围、硬上限和各卷预算。体量要结合 Profile：
- 成人长篇按本书规划；
- 少儿分集若一章=一集，按 Profile 单集目标校准；
- 绘本有声化按绘本/故事单元规划。

用户批准后章纲才能启动。

## 章纲门

章纲先完成分卷审计和全书总审。用户明确批准后才能写正式正文。

## 章数确定

### Profile 阶段
只确定“单位是什么”和可能的单元长度，不确定总章数。

### 世界观/大纲阶段
给预计体量范围，不锁定。

### 大纲批准后
正式提交：
- target_chapters / target_episodes
- soft_min
- soft_max
- hard_max
- volume_budgets

### 正文阶段
软范围允许自然波动；突破硬上限或导致结构变化，必须走变更协议。

## 用户主动给章数

视为强规划约束，但仍做承载力检查。若明显不合理，给“保持用户章数的结构方案”和“更合理的建议方案”，不擅自违背。
