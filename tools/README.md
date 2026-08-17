# 工具包总览

本目录是 AboutAI 的工具包本体。已收录工具按**作用分类**（编码 / 图表 / 视频剪辑 / 炒股 / 求职 / 规划 / 自动化）分表维护，每行一个工具，标注**类型**（skill / plugin / mcp / 安装包）、**来源**、**功能**与**说明**（"要什么"的选型提示），一眼就能区分同类工具。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。目录结构见 [Dir.md](../Dir.md)。

## 编码

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| node_repl | mcp | 系统自带（Codex 客户端） | Node.js REPL 执行能力，配合浏览器/桌面控制 | 启用 | 要跑 Node 脚本/做自动化 |

## 图表

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| diagram-design | plugin | GitHub（[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)） | 打包 Agent Skill（27 种编辑级图表） | 2.4.0；双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 `tools/plugins/diagram-design/` | 要好看、能直接发出去的图 |
| archify | skill | GitHub（[tt-a1i/archify](https://github.com/tt-a1i/archify)） | 把代码库/系统描述变成可交互的系统架构图 | v2.14.0；已装（Codex）；快照 tools/skills/archify/ | 要摸清代码库/评审架构/讲解系统 |
| drawio（Next AI Draw.io） | mcp | GitHub / npm（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)） | AI 生成/编辑 draw.io 图表，实时浏览器预览 | 已启用；`npx @next-ai-drawio/mcp-server@latest` | 要 draw.io 源文件、之后自己改 |
| Next AI Draw.io（桌面客户端） | 安装包 | GitHub（[DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io/releases)） | AI 增强的 draw.io 桌面绘图（macOS + Windows） | 0.4.16；已收录；位置 `installers/next-ai/`；dmg `c829735a…`、exe `f12a048f…` | 要离线手工画 draw.io 图 |

## 视频剪辑

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| video-editing-skill | skill | GitHub（[6missedcalls/video-editing-skill](https://github.com/6missedcalls/video-editing-skill)） | 自然语言剪辑视频：裁剪、去静音、字幕、变速（ffmpeg + Whisper） | 已装；快照 `tools/skills/video-editing-skill/` | 要剪视频/去静音/加字幕 |

## 炒股

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| StockWin | skill | 自己创建 | A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先） | 已装 | 要选股/分析持仓/定卖出策略 |

## 求职

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| offer | skill | 自己创建 | 求职助手：岗位搜索与评估、投递追踪、简历与岗位分析 | 已装 | 要找岗位/追踪投递/分析简历 |

## 规划

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| grill-me / grilling | skill | GitHub（[mattpocock/skills](https://github.com/mattpocock/skills)） | 追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问） | 已装；同源同流程 | 要打磨方案或设计 |

## 自动化

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| computer-use | mcp | 系统自带（Codex 客户端） | 通过 Computer Use 控制 macOS 桌面应用 | 未启用（enabled=false） | 要控制 macOS 桌面应用（当前未启用） |

## 识图

| 名称 | 类型 | 来源 | 功能 | 备注 | 说明 |
| --- | --- | --- | --- | --- | --- |
| vision-assist | skill | GitHub（[pudy/harness_skills](https://github.com/pudy/harness_skills)） | 图片/PDF 识别与 OCR：免费智谱 GLM 视觉 API 优先，Windows 内置 OCR 兜底，为纯文本模型（DeepSeek）补视觉 | 已装；Key 只存本地 `config.json`（不入库）；快照 `tools/skills/vision-assist/` | 要识别图片文字/读截图/解析图表或扫描 PDF |

## 维护约定

- 本文件人工维护：每个作用分类一个表格，新增/删除工具在对应分类表加/删一行，"说明"列按"要什么"的选型风格写。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
