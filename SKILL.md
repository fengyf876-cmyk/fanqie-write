---
name: fanqie-novel
description: 多受众、多题材的番茄长篇网文与有声书生产系统。用于用户提供世界观、简介、人物设定、已有样稿、人工大纲/章纲或项目规范后，识别并确认受众年龄、内容题材和有声产品形态，再按“Project Profile → 世界观 → 全书大纲 → 用户批准 → 体量/章数锁定 → 全书章纲 → 用户批准 → 每次最多3章有声正文 → 用户审核 → 下一批”的阶段门流程工作。支持成人长篇网文的读者承诺、问题链、情绪牵引和人物魅力增强，支持8–12岁少儿分集/绘本有声化及自定义 Profile，并严格隔离跨受众样本规则；章纲与正文的用户可见交付强制生成 DOCX；正文开始后仍支持修改章纲、影响分析、checkpoint 回滚和重新审批。任何锁定规划不得被静默改写。
---
# Fanqie Audiobook Story Studio
版本：3.7.0

把长篇有声内容视为“先识别产品，再规划，再批准，再分批执行”的状态化生产项目。规划允许版本化修改，但任何修改都必须可追踪、可影响分析、可回滚。
## 1. 核心原则
1. 先解析 `Project Profile`，再进入世界观与大纲生产。
2. Profile 分三层：Audience、Audio Product、Genre；三者不得混成单一题材标签。
3. 用户明确说明受众/年龄/产品形态时直接采用；只有依赖推断时才提交一次识别结果给用户确认。
4. 未批准 Profile，不得进入全书大纲；未批准大纲，不得锁定章数；未批准体量，不得生成正式全书章纲；未批准章纲，不得进入正式正文生产。
5. 正文默认采用三章批次制：一次最多输出3章/集；当前批未得到用户确认，不得自动继续下一批。
6. 用户说“继续”“接着写”只解锁下一批最多3章，不代表允许连续生成更多批次。
7. 当前批正文未批准时，只推进临时 Batch Working State，不污染正式 Current State。
8. 用户批准当前批后，才把三章依次提交到正式历史、Current State、Hooks 和 Character Matrix，并创建 checkpoint。
9. 正文开始后仍允许修改章纲。规划锁定表示“禁止静默修改”，不是“永久不可修改”。
10. 未来未写章纲可局部修改；当前未批准批次可修改并从最早受影响章重新推演；已批准历史修改必须先做影响分析和回滚方案。
11. 正文必须执行当前最新版批准章纲；文笔好但偏离规划仍视为不合格。
12. 不把同一个事实维护在多个真相源中。按 `references/data-governance.md` 读取和写回。
13. 用户当前明确要求优先；Project Profile 和本书 `book_rules.md` 优先于通用 Audience/Genre 参考。
14. 确定性指标尽量使用脚本；语义质量由模型审查。不要把文学判断伪装成精确百分比。
15. 成品默认是可进入配音/后期的话本；具体篇幅、台词/旁白比例、钩子密度由 Profile 决定。
16. 所有向用户交付的章纲与正文必须生成 DOCX。内部 Markdown 是真相源，DOCX 是派生审核/交付物；默认使用 `jungle_survival_docx_v1`，除非用户明确指定另一套版式。
17. 所有项目文件中给人阅读的字段名、说明项、状态项、表格列名和章节元数据必须使用中文标识。稳定 ID 和内部代码可保留英文/数字，但其字段标题必须是中文。读取 `references/chinese-labeling-standard.md`。
18. 对全书大纲、章纲和正文的规划，必须加载 `references/human-editor-story-planning.md`。优先把章纲写成可执行的客观事件链，并检查推进变量、主角能力兑现、推理证据链、冒险必要性、行动型章末钩子、角色不可替代性和有声来源辨识。人工样稿只用于提炼方法，不得照抄人物、情节、谜题或具体台词。
19. 故事结构增强基础层必须贯穿全书大纲、章纲和正文审计：检查价值变化、人物欲望与行动、事件因果、场景转折、高潮选择和不可逆变化。结构判断优先落到“起始状态 → 角色行动/选择 → 结果 → 新压力或新状态”，不能只凭气氛、主题宣言或创作意图判定推进。需要时读取 `references/story-structure-principles.md`。
20. 任何参考样本提炼出的 Audience-specific 方法不得跨 Audience 自动迁移。成人样本不得修改或覆盖少儿 Profile，少儿样本不得限制成人 Profile；只有明确判定为跨受众成立的故事结构原则，才可进入通用审计层。样本学习必须读取 `references/reference-sample-transfer-policy.md`。
21. `受众 = adult` 且属于网文型产品时，加载 `references/adult-webfiction-engagement.md`，追踪读者承诺、当前问题、兑现、新欲望、关系状态和高潮余波；情感与同人模块只能在 Genre/项目形态匹配时加载。
## 2. 启动与任务路由
开始任何项目任务时：

1. 读取 `project_status.md`；存在项目时同时读取 `project_profile.md`。
2. 正文阶段额外读取 `runtime/writing_batches.md`；若当前批未批准，优先恢复当前批，不开启新批。
3. 若项目不存在，执行 `PROFILE` + `INIT`。
4. 根据用户请求选择唯一主模式：
   - `PROFILE`：识别/修改受众、年龄、音频产品形态和题材。
   - `INIT`：保存世界观原始输入并建立 Story Bible。
   - `BOOK_OUTLINE`：生成或修改全书大纲。
   - `BOOK_OUTLINE_AUDIT`：只审核大纲。
   - `LENGTH_LOCK`：确定总字数、总章/集数和分卷预算。
   - `CHAPTER_OUTLINE`：生成或修改章纲。
   - `CHAPTER_OUTLINE_AUDIT`：只审核章纲。
   - `WRITE`：按批准章纲生成下一批最多3章有声正文。
   - `BATCH_REVIEW`：处理当前3章用户反馈、修改、批准或重做。
   - `PLAN_CHANGE`：正文开始后修改章纲/大纲并做影响分析。
   - `REVISE`：修改已有正文。
   - `DRAFT_AUDIT`：只审核正文。
   - `CONTINUITY`：连续性检查。
   - `DETOX`：只做 AI 去味。
   - `COMMERCIAL`：只做商业审查。
   - `DOCX_EXPORT`：把已完成的章纲或正文源文件导出为规定版式 DOCX，并执行结构校验与视觉 QA。
5. 用户要求跳阶段时先检查前置门；缺失时停在正确阶段。
## 2.1 用户可见交付协议：章纲/正文必须 DOCX
读取 `references/docx-output-format.md`。

- 章纲：只要提交给用户审核，就生成 `.docx`；内部 `planning/chapter_outline/*.md` 继续作为唯一规划源。
- 正文：单章或三章批次只要提交给用户审核，就生成 `.docx`；内部 `chapters/*.md` 继续作为正文源稿。
- 默认三章正文合并为一个文件：`《书名 第N-N+2章》.docx`。
- 章纲按当前审核范围合并为一个文件，例如 `《书名 第一卷章纲》.docx` 或 `《书名 章纲 第1-30章》.docx`。
- 不在聊天消息中重复粘贴完整章纲/正文；默认只给简短说明和 DOCX 链接。用户明确要求查看纯文本时才额外展示。
- DOCX 页面和字体固定按 `jungle_survival_docx_v1`：A4；上下边距25.4mm；左右边距31.75mm；正文宋体10.5pt、1.5倍行距、两端对齐、无首行缩进；书名22pt加粗居中；章节标题10.5pt加粗蓝色。
- 不复制参考文档中的修订颜色、下划线、批注边线或 tracked changes。
- 生成后先运行 `scripts/validate_story_docx.py`，再执行 DOCX render → inspect all pages → fix → re-render 的视觉 QA；通过后才交付。
- 修改章纲/正文后，旧 DOCX 视为派生物过期，必须从最新版源文件重新导出。
## 3. Stage 0：Project Profile
读取 `references/project-profile-routing.md`。
### 3.1 三层识别
分别确定：
- Audience：成人 / 8–12岁少儿 / 自定义；
- Audio Product：成人长篇网文有声书 / 少儿分集故事 / 儿童绘本有声化 / 广播剧 / 自定义；
- Genre：悬疑、玄幻、都市、言情、科普冒险、校园、神话、喜剧等，可多选。
### 3.2 明确信息直接采用
如果用户已经明确“8–12岁”“成人悬疑有声书”“儿童绘本有声化”等，不再重复确认这些已知字段。

创建 `project_profile.md`，记录：
- `配置来源 = explicit_user`
- `识别置信度 = high`
- `配置状态 = approved`
### 3.3 推断信息必须确认
如果用户只给世界观/简介，允许推断 Profile，但必须输出简短识别结果：
- 受众；
- 有声产品；
- Genre；
- 置信度；
- 将启用的关键规则。

将阶段置为 `PROFILE_USER_REVIEW`。用户确认后才进入下一阶段。
### 3.4 加载 Profile
- Audio Product → `references/audio-product-profiles.md`
- `children_8_12` → `references/audience-children-8-12.md`
- `adult` → `references/audience-adult.md`
- Genre → `references/genre-profiles.md`
- 所有项目 → `references/audiobook-script-format.md`

不要把某个 Profile 的数值或题材专项规则抄进其他 Profile。成人网文由 `audience-adult.md` 继续按产品形态和 Genre 条件路由；少儿 Profile 不加载这些成人专项。
### 3.5 Reference-manuscript override
当用户提供人工样稿、DOCX、大纲或章纲，并要求参考其写法时：
1. 先读取 `references/reference-sample-transfer-policy.md`，把样稿视为项目级生产证据，不视为必须复刻的模板。
2. DOCX 可运行 `scripts/analyze_reference_docx.py`，分开记录有效内容长度、成品可见长度、话本语法和版式。
3. 先提炼可迁移方法，再决定是否写入项目规则；禁止复制样稿的具体人物、剧情、谜题、台词、专有设定。
4. 标记样本的 Audience、产品形态、Genre、篇幅、叙事模式、证据强度和可迁移范围；无法证明跨受众成立时不得进入通用层。
5. 单样本方法只作为候选策略；多个优秀样本重复方法只能进入匹配的 Audience/产品/Genre reference；跨项目稳定成立后才可考虑通用化。
6. 若样稿匹配内置 Jungle Survival 基准，可选择 `有声产品类型 = children_chaptered_story`、`话本格式配置 = jungle_survival_v1`、`DOCX版式配置 = jungle_survival_docx_v1`；长度只作为提议，仍需用户批准。
### 3.6 Per-unit length option
读取 `references/unit-length-configuration.md`。单集/单章字数是项目选项，不是 Audience 硬规则。

允许模式：
- `user_exact`
- `user_range`
- `reference_sample`
- `skill_recommended`
- `flexible`

规则：
1. 不得仅凭 Audience 或 Audio Product 静默指定600、1800或其他固定字数。
2. 用户明确给单集字数时直接采用，并记录来源。
3. 参考样稿长度只作为提案证据，不自动锁定。
4. 若用户未给长度，在 Profile 或 Length Lock 阶段用一个紧凑问题确认，或给出建议范围后等待批准。
5. 暂定值写入 `project_profile.md`；最终批准值锁定在 `planning/length_plan.md`。
6. 章纲和正文审计必须读取批准的项目值，不使用隐藏默认值。
## 4. Stage 0.5：世界观与项目初始化
Profile 已批准后：

1. 以 `assets/project-template/` 初始化项目。
2. 原样保存用户核心设定到 `source_worldview.md`，不要混入模型补充。
3. 将原始输入结构化为 `story_bible.md`：前提、主题、世界规则、力量/资源体系、势力、地点、历史锚点、硬约束。
4. 建立 `book_rules.md`：本书专属目标、主角锁定、禁忌、篇幅配置、商业目标。
5. 建立 `style_guide.md`：语言、主要人物声音指纹、行为反差依据和本项目有声表达习惯。声音指纹至少覆盖句长、直说/反问/解释习惯、关心与愤怒方式、冲突反应、亲密状态变化、固定称呼和脆弱表达。
6. 将 `project_status.md` 的“项目阶段”切换至 `BOOK_OUTLINE_DRAFTING`。
7. 用户未提供但规划必须用到的信息只能标“建议/暂定”，不能伪装成原设定。
## 5. Stage 1：全书大纲
### 5.1 生成
生成 `planning/book_outline.md`。同时读取 `references/human-editor-story-planning.md`。不要预设四卷、120万字或固定章数。

大纲至少覆盖：
- 核心故事命题与终局；
- 主角目标与阶段目标；
- 主线、主要支线、关系线；
- 反派/阻力层级；
- 世界秘密与信息释放顺序；
- 人物与能力成长；
- 分卷/大型剧情单元；
- 重大反转及铺垫；
- 主要伏笔与回收方向；
- 高潮、回报和结局结构；
- 作品承诺、第一次小兑现、阶段升级、阶段大兑现、终局兑现及兑现后的新动力；
- 长期读者问题、阶段答案、中期再立题和终局答案；
- 与 Project Profile 匹配的内容复杂度、节奏和产品单位；
- 初步体量范围，不锁死章数。

额外强制规划：
1. 每个卷/大型剧情单元写明其“推进变量”：本单元改变的核心问题是什么，例如规则认知、目标、队伍结构、资源、敌人能力、地图条件、代价、人物关系或世界信息。
2. 相邻大型单元不得只换场景重复同一种危机；至少有一个推进变量发生实质变化。
3. 核心队伍按“能力 / 信息来源 / 明确短板 / 不可替代任务”规划。若删掉某核心角色主线几乎不受影响，必须重做角色功能。
4. 智斗/规则/悬疑型长线优先使用“未知 → 观察 → 假设 → 验证 → 利用 → 升级/反转 → 新问题”的认知推进，而不是连续重复追逃。
5. 成人网文型项目加载 `references/adult-webfiction-engagement.md`，规划承诺—兑现与读者问题链；关系驱动项目再规划情绪债、关系阶段变化和高潮后余波；同人/衍生项目建立 Canon Anchor。

8–12岁少儿项目的大纲同时考虑听觉理解、角色可辨识度、每集独立看点、知识内容戏剧化和年龄适配；成人项目不得套用少儿短集规则。
### 5.2 内部审计
读取 `references/book-outline-audit.md`，生成/更新 `planning/book_outline_review.md`。

按 Profile 条件检查作品承诺、阶段兑现、读者长期问题链和高潮后余波。成人网文型项目加载 `adult-webfiction-engagement.md` 及其匹配专项；不得跨 Audience 套用。

同时读取 `references/book-outline-audit-3.6.1.md`，执行故事结构增强审计：
- 核心故事成立性：核心命题、主角欲望、主要阻力、终局回答是否构成可持续的因果链；主角的选择是否真正决定关键结果。
- 主角故事弧：检查初始欲望/缺陷或错误信念、阶段性选择、代价、能力与认知变化，以及终局选择如何完成或反转故事弧；不得用旁白宣称成长代替行动证据。
- 分卷价值变化：每卷/大型剧情单元必须改变至少一项目标、知识、规则认知、队伍关系、资源、能力、位置、代价、风险或承诺；只换地图、敌人或场景而不改变价值的单元视为重复。
- 事件必要性与因果：对重大事件追问“没有它，后续哪一项事实或选择无法成立”；检查触发、行动、结果和下一压力，避免巧合直接解决核心问题。
- 场景与高潮：规划关键场景的入口状态、转折和出口状态；高潮必须由已铺垫的选择、明确代价和主角行动解决核心困境，不得主要依赖外援、偶然或新能力空降。
- 不可逆变化：标记死亡/伤残、身份暴露、关系破裂、资源损失、规则公开、地点封锁和重大承诺等变化，并追踪其对后续规划的约束。

优先修复 Critical/Major，直到 `READY_FOR_USER_REVIEW`。
### 5.3 用户批准门
用户未明确批准前不得进入 Length Lock。批准后记录版本，将 `book_outline.status = approved`。
## 6. Stage 1.5：体量与章数锁定
章数最终确定在“大纲批准后、章纲生成前”。
### 6.1 三种输入模式
- 用户指定章数：视为强约束，先做承载力检查。
- 用户指定总字数：结合项目目标单位和大纲结构提出章数范围。
- 用户未指定：根据大纲剧情单元、分卷、人物弧线、支线和 Profile 提出建议。
### 6.2 Profile 对体量的影响
- 成人长篇：章长和总量由 `book_rules` + `length_plan` 决定。
- 少儿分集：若确认“一章=一集”，按项目批准的单集字数规划；未配置则先确认。
- 绘本有声化：按绘本页/故事单元和有声交付要求规划。

生成 `planning/length_plan.md`：目标总字数、目标章/集数、软范围、硬上限、各卷预算、单章/单集目标。

用户批准后 `length_plan.status = approved`，解锁章纲。
## 7. Stage 2：全书章纲
### 7.1 生成方式
概念上规划全书，执行上按卷/大型剧情单元生成：
1. 读取批准的 `project_profile.md`、`book_outline.md`、`length_plan.md`。
2. 加载 `references/human-editor-story-planning.md`。
3. 按卷生成 `planning/chapter_outline/volume_XX.md`。
4. 每卷局部审计并做跨卷衔接。
5. 全部完成后更新 `master_index.md`，执行全书章纲总审。

每章/集章纲至少写明：
- 章节编号、所属卷、类型、POV；
- 本章功能/目标；
- 承接状态；
- 当前核心问题与人物为什么现在必须行动；
- 本章客观核心事件链；
- 本章推进变量；
- 核心冲突；
- 信息释放；
- 人物/关系推进；
- 主角主动行为与能力兑现点；
- 当前读者问题、本章答案/兑现、兑现后的新问题或新欲望；
- 回报/看点；
- Hook 开启、推进、回收；
- 物品、能力、位置、关系变化；
- 本章收尾客观事件；
- 章末行动型钩子；
- 禁止提前发生；
- 有声化设计；
- Profile 约束。

条件字段：
- 智斗/推理/规则章节：写明“证据 → 假设 → 验证 → 结论 → 实战兑现”的推理链；证据不足时不得让主角直接跳到正确答案。
- 高风险冒险章节：写明“为何更安全的方案更差、已失效或来不及”，让冒险成为受约束下的最优解，而非作者强行作死。
- 团队章节：写明本章由谁提供信息、谁决策、谁执行、谁承担不可替代任务。
- 多声源章节：写明现实人物、系统、直播/弹幕、内心、远端通讯等切换时的听觉辨识方式。
- 关系驱动章节：写明关系入口/出口状态、情绪债阶段，以及外部事件具体改变的信任、依赖、距离、控制权、认知、承诺、公开程度或关系身份。
- 高潮/终局章节：写明高潮选择与代价，以及高潮后用什么可观察场景证明变化生效。
- 同人/衍生章节：写明关键行为对应的 Canon Anchor 与偏离依据。

禁止把“营造紧张气氛”“突出主角聪明”“加深关系”“增强危机感”单独当作核心事件。必须落到谁做了什么、导致什么、信息/资源/关系如何改变。

相邻章节检查：连续两章不得只更换危险场面而不改变任何推进变量。至少改变规则认知、任务目标、队伍结构、资源、敌人能力、地图条件、代价、关系或信息中的一项。

少儿分集额外规划：
- 本集目标字数；
- 前5集的早期钩子/看点；
- 本集核心看点或笑点/剧情卡点；
- 主角首次台词、首次主动决策、首次能力展示、首次外部反馈是否被过长环境/路人描写挤掉；
- 结尾留存钩子；
- 旁白压缩与对话承载方案；
- 难懂视觉/知识信息的听觉转译。
### 7.2 章纲审计
读取 `references/chapter-outline-audit.md`。除规划一致性、因果、信息边界、伏笔、重复、高潮、体量和 Profile 适配外，必须检查：
- 章纲是否是客观事件施工图，而不是创作意图清单；
- 推进变量是否真实变化；
- 主角是否在早期通过行动兑现核心能力；
- 智斗推理是否有证据和验证；
- 高风险行为是否有必要性；
- 章末是否优先形成“现在必须处理什么”的行动型钩子；
- 核心队员是否有不可替代贡献；
- 有声来源切换是否只靠听也能辨识。
- 当前 Reader Question 是否清晰，本章是否真实兑现承诺，兑现后是否产生新的故事动力。
- 关系驱动章节的情绪债阶段与关系入口/出口状态是否由具体信息、动作和选择支撑。
- 重大外部事件是否改变主线或内部关系，高潮后是否有余波验证。
- 同时读取 `references/chapter-outline-audit-3.6.1.md`：检查事件链是否写成“承接状态 → 人物行动/选择 → 结果 → 新压力/新状态”。
- 本章起始状态与收尾状态是否有真实价值变化；至少有一项目标、知识、关系、资源、规则、位置、能力、代价、风险或承诺发生可追踪改变。
- 每个关键事件是否由角色欲望、已知信息和当时能力共同解释；角色是否因选择而不是作者安排进入下一事件。
- 每个场景是否具备目标/阻力/转折/出口状态；场景切换是否带来新信息、新限制、新选择或新后果，而非只更换背景。
- 章末或本章高潮的解决是否来自主角或关键角色的有代价选择；是否留下明确的不可逆变化及其后续影响。
### 7.3 用户批准门与 DOCX 交付
1. 内部章纲审计通过后，保留 Markdown 源文件。
2. 按当前审核范围调用 `scripts/export_story_docx.py --mode chapter-outline` 导出章纲 DOCX。
3. 调用 `scripts/validate_story_docx.py` 做结构校验，并按 `references/docx-output-format.md` 完成逐页视觉 QA。
4. 向用户交付 DOCX，等待审核；不要在聊天中再贴整份章纲。
5. 用户未明确批准全书章纲前，不得进入正式正文生产。批准后锁定 Markdown 规划版本并切换至 `WRITING`。
6. DOCX 是审核派生物；若用户修改章纲，更新 Markdown 后必须重新导出 DOCX。
## 8. Stage 3：三章批次正文生产
正文阶段必须加载 `references/writing-batch-workflow.md` 和 `references/human-editor-story-planning.md`。
### 8.1 固定批次规则
- 默认 `writing_batch_size = 3`。
- 每个用户审核周期最多输出3章/集。
- 若全书剩余不足3章，则输出剩余部分。
- 用户可以要求本批少于3章；不要主动扩大到4章以上。
- 当前批未获用户确认，不得开始下一批。
### 8.2 写前加载
写下一批时至少读取：
- `project_profile.md`；
- 对应 Audience Profile；
- `story_bible.md`；
- `book_rules.md`；
- `style_guide.md`；
- 已批准大纲对应单元；
- 本批3章最新版批准章纲；
- `runtime/current_state.md`；
- `runtime/pending_hooks.md`；
- `runtime/character_matrix.md`；
- 最近章节摘要；
- `runtime/writing_batches.md`；
- 对应 Genre/专项 reference。

第一批开始前创建 `BATCH-000` 基线 checkpoint。以后每批以最近 approved checkpoint 为 base。
### 8.3 批次内写作状态
批次未批准时：
- 正式 Current State 保持不变；
- 通过 `runtime/batch_working_state.md` 临时推演章1→章2→章3；
- 三章文件使用同一 `批次编号`；
- 三章 `正文状态 = awaiting_user_approval` 后提交用户。
### 8.4 成品语法
加载 `references/audiobook-script-format.md`。

默认标准：
- 旁白：无 `【旁白】` 标签；
- 台词：`【角色】“台词。”`；
- 情绪/声音状态：`【角色 情绪】“台词。”`；
- 内心：`【角色 内心】“内容。”`；
- 多人同声：`【角色A、角色B】“台词。”`；
- 声效：`【声效】具体可听声音`；
- 角色标签后不加冒号；
- 纯动作不能塞进角色标签；
- 台词后不添加不会录制的解释性括号。

多声源切换强制要求：现实人物、系统、直播/弹幕、远端通讯、内心OS、回忆等来源切换时，必须通过旁白、声效、固定播报语法或角色标签形成听觉提示。不得依赖屏幕排版、颜色、用户名位置或视觉框让听众猜来源。
### 8.4A Reference-sample production
若 `话本格式配置 = jungle_survival_v1`，加载 `references/reference-benchmark-jungle-survival.md`，执行样本提炼出的长度窗口和段落布局。此 profile 可使用 `【描述 声效】` 语法；通用 profile 仍使用 `【声效】描述`。
### 8.5 Profile 化写作
#### 8–12岁少儿
加载 `references/audience-children-8-12.md`：
- 只靠听也能理解；
- 语言简单具体；
- 对话主导、旁白克制；
- 单集字数读取项目配置；
- 前5集尽早出现主角可感知的主动行为或能力兑现，不让大量环境、系统、路人反应占满开场；
- 每集至少一个有效看点；
- 结尾有留存钩子；
- 对话/旁白比例按项目 Profile 执行；
- 单段旁白避免过长；
- 场景来源必须听觉可辨。
#### 成人
加载 `references/audience-adult.md`：
- 不继承少儿短集硬参数；
- 章长按本书体量计划；
- 旁白/对话由题材与场景决定；
- 保留成人作品需要的悬疑、心理、氛围和叙事深度，同时保证可听性。
- 成人网文型内容再加载 `references/adult-webfiction-engagement.md`；按其路由加载开篇、承诺、问题链与人物魅力，情感/同人专项仅在项目匹配时加载。
### 8.6 正文与批次审计
读取 `references/draft-audit.md`。

同时读取 `references/draft-audit-3.6.1.md`，执行场景变化、因果连续性、主角成长、高潮选择、有声化和 AI 去味审核。

每章检查：
- 最新章纲执行一致性；
- Profile 执行一致性；
- 字数/单集长度；
- 有声格式与可听性；
- AI味；
- 因果链；
- 行为/规则；
- 时间/空间/资源；
- 对话/旁白风险；
- 专项场景质量；
- 主角能力是否通过行动而不是旁白吹嘘兑现；
- 智斗结论是否由足够证据和验证得到；
- 高风险行动前是否交代安全选项为何不可行；
- 章末是否形成明确的下一步压力、期限、选择或危险；
- 多声源切换是否只靠听也能理解；
- 团队成员是否各有本章贡献，避免长期工具人化。
- 场景变化审核：每个场景是否从明确入口状态推进到不同出口状态；新场景是否改变目标、信息、限制、关系、资源或风险，删掉后是否会损失有效推进。
- 因果连续性审核：重大事件是否能由前文触发、人物行动和可获得信息解释；是否出现无铺垫的动机、能力、情绪转向或结果。
- 主角成长审核：成长是否通过更困难的选择、行动结果和代价可听见/可看见；是否避免只靠升级、旁白夸赞或他人评价证明成长。
- 高潮选择审核：高潮是否迫使角色在核心欲望/价值冲突中作出选择，并产生代价或不可逆后果；不得用巧合、外援或突然新增规则替代选择。
- AI 去味审核：检查模板化段落、机械排比、同义重复、过度解释、空泛情绪、无对象的“震撼/紧张”宣告和场景只换名词不换功能；修改后必须保留人物具体欲望、行动和因果。
- 有声化结构审核：场景、来源、时间跳转、高潮转折和不可逆后果是否仅靠旁白、台词、声效或固定语法即可理解，不依赖屏幕排版或视觉提示。
- 吸引力审核：成人网文是否尽快进入当前问题，是否存在核心吸引力出现前独立运行的背景说明；不设置跨项目固定字数阈值。
- 承诺与问题链审核：本章兑现了什么、给出什么答案、又产生什么新欲望；避免连续开题不回答或只重复提醒。
- 人物与情绪审核：魅力是否由行为证明，人物声音是否可辨，情绪强度是否有压力/缓冲/升级/余波变化，已经被行为证明的情绪是否又被旁白重复解释。
- 关系/同人条件审核：关系驱动项目检查情绪债和关系出口状态；同人/衍生项目检查 Canon Anchor 与 OOC 风险。不得对不匹配的 Audience/Genre 启用。

三章完成后再做批次连续性审计。确定性指标/交付工具可调用：
- `scripts/analyze_chapter.py`
- `scripts/validate_audiobook_script.py --project-root <项目目录> <章节文件>`
- `scripts/validate_writing_batch.py <项目目录>`
- `scripts/export_story_docx.py --mode manuscript|chapter-outline ...`
- `scripts/validate_story_docx.py <output.docx>`
### 8.7 用户审核门与 DOCX 批次交付
内部审计完成后：
1. 保留本批1–3章 Markdown 源稿与临时 Batch Working State；
2. 将本批最多3章合并导出为一个 DOCX；
3. 使用 `scripts/validate_story_docx.py` 做结构校验，并完成逐页 render/视觉 QA；
4. 向用户只交付当前批 DOCX + 简短说明；
5. 将 `正文批次状态 = awaiting_user_approval`；
6. 停止，不生成下一批。

用户反馈处理：
- 全部OK → 正式 commit 本批、创建 checkpoint、解锁下一批；
- 要改某章 → 当前批保持未批准，从最早受影响章重做/复核；
- 不要因为其中1章看似通过就自动写第4章。
### 8.8 正式提交
只有用户明确批准当前批后才更新：
- `runtime/chapter_summaries.md`
- `runtime/current_state.md`
- `runtime/pending_hooks.md`
- 必要时 `runtime/character_matrix.md` / `story_bible.md`
- `runtime/writing_batches.md`

创建对应 approved checkpoint，更新 `last_approved_chapter`、`last_consistent_chapter`。

`handoff_current.md`、`progress_tracker.md` 仍为派生文件。
## 9. 正文开始后的章纲修改
加载 `references/revision-and-rollback.md`。
### 9.1 Future-only：未来未写章节
用户明确要求修改尚未生成正文的章纲时：
- 可直接按用户要求修改；
- 升级章纲版本；
- 局部重审受影响区间和后续 Hook/人物弧线/体量；
- 不回滚已批准历史正文。

若修改触及宏观大纲重大节点，创建 Change ID 并同步 Book Outline。
### 9.2 Current-batch：当前3章未批准
用户要求修改当前批章纲时：
1. 修改对应章纲；
2. 找出本批最早受影响章节；
3. 从 batch base checkpoint 重建临时工作状态；
4. 从最早受影响章开始重写/复核后续章节；
5. 再次提交同一批审核；
6. 修改后的章纲 DOCX与正文 DOCX都重新导出；
7. 未通过前仍不得进入下一批。
### 9.3 Approved-past：已批准历史
如果用户要修改已经批准的历史章节对应章纲/正文，而且可能改变既成事实：
1. 创建 `CHANGE-XXX`；
2. 分析最早/最晚受影响章节；
3. 判断后续正文是 `current / revalidate / stale / superseded`；
4. 给出最小重写方案和 checkpoint 回滚点；
5. 等用户确认影响方案；
6. 从适当 checkpoint 恢复逻辑状态；
7. 按新章纲重新生成受影响内容；
8. 仍按每批最多3章逐批提交用户确认；
9. 所有受影响章纲/正文 DOCX均从最新版 Markdown 源重新导出并重新执行视觉 QA。

不要默认重写全部后文；优先寻找状态重新收敛的位置。
## 10. 计划变更协议
已批准的 Profile、受众年龄、产品形态、大纲、体量或重大章纲变化：

1. 不静默改批准文件。
2. 在 `planning/plan_change_log.md` 创建 Change ID 或记录用户直接授权的局部版本变更。
3. 写明原计划、建议修改、原因、受影响章节/Profile/Hook/Character/Item/Rule、体量和正文影响。
4. 对大范围已批准历史影响先提交用户确认。
5. 批准后升级版本，同步受影响规划并重新审计。

纯措辞、局部表演、声效细节不属于重大 Plan Change；改变人物命运、核心反转、揭示时点、卷目标、核心伏笔、结局、世界规则或大量已批准正文必须走影响协议。
## 11. 数据与规则优先级
读取 `references/data-governance.md`。

关键原则：
- `project_profile.md` 是受众/年龄/产品形态唯一真相源；
- `source_worldview.md` 是用户原始设定证据层；
- `story_bible.md` 是世界正典；
- `book_rules.md` 是本书创作宪法；
- Book/Chapter Outline 是未来规划；
- 未批准批次正文只是候选实现；
- Current State / Summaries 只记录用户批准后的实际历史；
- `batch_working_state.md` 是临时派生状态；
- `checkpoints/` 是只读回滚档案；
- 派生文件不能反向覆盖源文件。
## 12. 参考文件加载导航
按需加载，不要全部塞入上下文：
- 人工编辑规划方法：`references/human-editor-story-planning.md`
- 样本迁移与 Audience 防污染（使用参考样本时）：`references/reference-sample-transfer-policy.md`
- Profile 路由：`references/project-profile-routing.md`
- Audio Product：`references/audio-product-profiles.md`
- 单元字数：`references/unit-length-configuration.md`
- 8–12岁少儿：`references/audience-children-8-12.md`
- 成人：`references/audience-adult.md`
- 成人网文吸引力总路由（仅 adult + 网文型产品）：`references/adult-webfiction-engagement.md`
- 成人网文开篇：`references/adult-webfiction-opening.md`
- 故事承诺与兑现：`references/story-promise-and-payoff.md`
- 读者问题链：`references/reader-question-chain.md`
- 成人情感故事引擎（仅匹配题材）：`references/emotional-story-engine.md`
- 人物魅力与反差：`references/character-appeal-and-contrast.md`
- 同人/衍生一致性（仅已有 IP 二创）：`references/derivative-fiction-character-consistency.md`
- 有声成品语法：`references/audiobook-script-format.md`
- Jungle Survival 基准：`references/reference-benchmark-jungle-survival.md`
- DOCX交付版式：`references/docx-output-format.md`
- Genre：`references/genre-profiles.md`
- 大纲审计：`references/book-outline-audit.md`
- 大纲结构增强审计：`references/book-outline-audit-3.6.1.md`
- 章纲审计：`references/chapter-outline-audit.md`
- 章纲结构增强审计：`references/chapter-outline-audit-3.6.1.md`
- 正文审计：`references/draft-audit.md`
- 正文结构增强审计：`references/draft-audit-3.6.1.md`
- 故事结构原理：`references/story-structure-principles.md`
- 三章批次：`references/writing-batch-workflow.md`
- 章纲修改/回滚：`references/revision-and-rollback.md`
- 数据治理：`references/data-governance.md`
- 中文标识：`references/chinese-labeling-standard.md`
- AI去味：`references/ai-detox-guide.md`
- 战斗/动作：`references/battle-scene-guide.md`
- 对话风险：`references/dialogue-monitor.md`
- 循环模式：`references/pattern-detection.md`
- 商业：`references/commercial-review.md`
- 平台：`references/fanqie-platform-rules.md`
