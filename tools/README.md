# 工具包总览

本目录是 AboutAI 的工具包本体。所有已收录工具维护在一张表中：**类型**（skill / plugin / mcp / 安装包）、**作用分类**（编码 / 图表 / 炒股 / 求职 / 规划 / 自动化）、**来源**与**功能**，看一眼就知道有什么、能干什么。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。目录结构见 [Dir.md](../Dir.md)。

## 工具清单

| 名称 | 类型 | 作用分类 | 版本 | 来源 | 功能 | 备注 | 原理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| node_repl | mcp | 编码 | — | 系统自带（Codex 客户端） | Node.js REPL 执行能力，配合浏览器/桌面控制 | 启用 |  |
| diagram-design | plugin | 图表 | 2.3.5 | GitHub（[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)） | 打包 Agent Skill（27 种编辑级图表） | 双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 `tools/plugins/diagram-design/` | 说明书+模板库：模型按 SKILL.md 规则选型并手写自包含 HTML/SVG；导入 draw.io/Mermaid 时脚本纯文本解析源文件再按品牌风格重绘；无后台服务 |
| drawio（Next AI Draw.io） | mcp | 图表 | — | GitHub / npm（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)） | AI 生成/编辑 draw.io 图表，实时浏览器预览 | 已启用；`npx @next-ai-drawio/mcp-server@latest` | MCP server：按需拉起 stdio 进程，模型调用 create/get/edit 工具改 `.drawio` 源文件，内置 HTTP 实时预览；进程结束后可能残留，需手动清理 |
| Next AI Draw.io（桌面客户端） | 安装包 | 图表 | 0.4.16 | GitHub（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io/releases)） | AI 增强的 draw.io 桌面绘图（macOS + Windows） | 已收录；位置 `installers/next-ai/`；dmg `c829735a…`、exe `f12a048f…` |  |
| StockWin | skill | 炒股 | — | 自己创建 | A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先） | 已装 |  |
| offer | skill | 求职 | — | 自己创建 | 求职助手：岗位搜索与评估、投递追踪、简历与岗位分析 | 已装 |  |
| grill-me / grilling | skill | 规划 | — | GitHub（[mattpocock/skills](https://github.com/mattpocock/skills)） | 追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问） | 已装；同源同流程 |  |
| computer-use | mcp | 自动化 | — | 系统自带（Codex 客户端） | 通过 Computer Use 控制 macOS 桌面应用 | 未启用（enabled=false） |  |

## 维护约定

- 本文件人工维护：新增/删除工具后，在工具清单中加/删一行（填写类型与作用分类）。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
