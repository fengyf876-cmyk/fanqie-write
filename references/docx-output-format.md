# DOCX 交付版式

## 默认页面

使用 `jungle_survival_docx_v1`：A4；上、下边距25.4mm；左、右边距31.75mm。正文宋体10.5pt、1.5倍行距、两端对齐、无首行缩进；书名22pt加粗居中；章节标题10.5pt加粗蓝色。

不要复制参考文档的修订颜色、批注、下划线或 tracked changes。

## 正文

三章批次默认一个文件 `《书名 第N-N+2章》.docx`；不足3章按实际范围。章节默认连续排版，不强制每章分页。

## 章纲

按当前审核范围合并，例如 `《书名 第一卷章纲》.docx`。字段名可加粗，不使用复杂表格或花哨配色。

## QA

导出后运行 `scripts/validate_story_docx.py`，再 render → inspect all pages → fix → re-render。检查截断、重叠、乱码、异常换行、标题孤行、大空白和字体替代。通过后再交付。
