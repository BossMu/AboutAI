# 工具包总览

本目录是 AboutAI 的工具包本体。已收录工具按**作用分类**（编码 / 图表 / 炒股 / 求职 / 规划 / 自动化）分表维护，每行一个工具，标注**类型**（skill / plugin / mcp / 安装包）、**来源**、**功能**与**说明**（干啥的、特点是什么），一眼就能区分同类工具。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。目录结构见 [Dir.md](../Dir.md)。

## 编码

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| node_repl | mcp | 系统自带（Codex 客户端） | Node.js REPL 执行能力，配合浏览器/桌面控制 | 启用 | 内置的 Node.js 交互执行环境，让模型跑脚本、配合浏览器/桌面控制做自动化；随会话按需启动 |

## 图表

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| diagram-design | plugin | GitHub（[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)） | 打包 Agent Skill（27 种编辑级图表） | 2.3.5；双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 `tools/plugins/diagram-design/` | 编辑级图表设计技能：27 种图表类型，品牌化配色、自包含 HTML/SVG 输出；适合对外展示/文档，可导入 draw.io/Mermaid 重绘；无后台服务 |
| drawio（Next AI Draw.io） | mcp | GitHub / npm（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)） | AI 生成/编辑 draw.io 图表，实时浏览器预览 | 已启用；`npx @next-ai-drawio/mcp-server@latest` | MCP 服务：让 AI 直接创建/编辑 `.drawio` 源文件，带实时浏览器预览；适合需要继续人工编辑的 draw.io 生态图 |
| Next AI Draw.io（桌面客户端） | 安装包 | GitHub（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io/releases)） | AI 增强的 draw.io 桌面绘图（macOS + Windows） | 0.4.16；已收录；位置 `installers/next-ai/`；dmg `c829735a…`、exe `f12a048f…` | 桌面绘图客户端（macOS/Windows 安装包）：AI 增强的 draw.io，可单独手工绘图，也可配合 drawio MCP 使用 |

## 炒股

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| StockWin | skill | 自己创建 | A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先） | 已装 | A 股分析总控：智能选股、持仓深度分析、卖出/止盈止损策略，资金面优先，一套流程走完 |

## 求职

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| offer | skill | 自己创建 | 求职助手：岗位搜索与评估、投递追踪、简历与岗位分析 | 已装 | 求职助手：找岗位、投递追踪、简历与岗位分析评估，从筛选到决策一条龙 |

## 规划

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| grill-me / grilling | skill | GitHub（[mattpocock/skills](https://github.com/mattpocock/skills)） | 追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问） | 已装；同源同流程 | 追问式访谈：把方案/设计按设计树分轮拷问直到达成共识；grill-me 是入口，grilling 是流程实现 |

## 自动化

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| computer-use | mcp | 系统自带（Codex 客户端） | 通过 Computer Use 控制 macOS 桌面应用 | 未启用（enabled=false） | 桌面控制：让 AI 通过 Computer Use 操作 macOS 桌面应用；当前未启用 |

## 维护约定

- 本文件人工维护：每个作用分类一个表格，新增/删除工具在对应分类表加/删一行，并写清"说明"列（干啥的 + 特点，方便同类区分）。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
