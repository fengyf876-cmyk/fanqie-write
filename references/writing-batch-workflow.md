# 三章批次工作流

正文默认每个用户审核周期最多3章。第一批前建立 `BATCH-000` 基线 checkpoint；以后使用最近 approved checkpoint。

未批准批次只更新 `runtime/batch_working_state.md`，不得写入正式 Current State、Hooks、Summaries。三章按顺序推演，后一章必须读取前一章临时结果。

提交用户时将本批源稿导出为一个 DOCX，状态设为 `awaiting_user_approval` 并停止。

用户全部批准后才把各章依次提交到正式历史，更新 Current State / Hooks / Character Matrix / Summaries，并创建 approved checkpoint。若用户修改某章，从最早受影响章重新推演本批后续。
