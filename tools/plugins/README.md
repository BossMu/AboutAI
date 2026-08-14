# 插件登记

Codex / Claude Code 的插件在这里登记。插件是"安装/分发单元"，内部可能打包 Agent Skill、MCP 或其他组件（与 `tools/skills/` 里直接放置的 skill 区分）。

| 名称 | 版本 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- |
| diagram-design | 2.3.5 | GitHub（[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)） | 打包 Agent Skill（27 种编辑级图表） | 双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 `tools/plugins/diagram-design/` | 说明书+模板库：模型按 SKILL.md 规则选型并手写自包含 HTML/SVG；导入 draw.io/Mermaid 时脚本纯文本解析源文件再按品牌风格重绘；无后台服务 |

内容包快照：`tools/plugins/diagram-design/`（版本 2.3.5，不含 `.git`）。插件升级后需重新同步快照。
