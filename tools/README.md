# 工具包总览

本目录是 AboutAI 的工具包本体。所有已收录工具维护在一张表中：**作用分类**（编码 / 图表 / 炒股 / 求职 / 规划 / 自动化）在左并合并同类单元格，每行一个工具，标注**类型**（skill / plugin / mcp / 安装包）、**来源**与**功能**，看一眼就知道有什么、能干什么。

> 提示：`tools/INDEX.md` 是 `sync.py` 自动生成的机械索引；本文件是人工维护的总览，两者互补。目录结构见 [Dir.md](../Dir.md)。

## 工具清单

<table>
  <thead>
    <tr><th>作用分类</th><th>名称</th><th>类型</th><th>版本</th><th>来源</th><th>功能</th><th>备注</th><th>原理</th></tr>
  </thead>
  <tbody>
    <tr><td>编码</td><td>node_repl</td><td>mcp</td><td>—</td><td>系统自带（Codex 客户端）</td><td>Node.js REPL 执行能力，配合浏览器/桌面控制</td><td>启用</td><td></td></tr>
    <tr><td rowspan="3">图表</td><td>diagram-design</td><td>plugin</td><td>2.3.5</td><td>GitHub（<a href="https://github.com/cathrynlavery/diagram-design">cathrynlavery/diagram-design</a>）</td><td>打包 Agent Skill（27 种编辑级图表）</td><td>双端已装；支持 draw.io/Mermaid 导入重绘、品牌化配色；内容包快照 <code>tools/plugins/diagram-design/</code></td><td>说明书+模板库：模型按 SKILL.md 规则选型并手写自包含 HTML/SVG；导入 draw.io/Mermaid 时脚本纯文本解析源文件再按品牌风格重绘；无后台服务</td></tr>
    <tr><td>drawio（Next AI Draw.io）</td><td>mcp</td><td>—</td><td>GitHub / npm（<a href="https://github.com/DayuanJiang/next-ai-draw-io">DayuanJiang/next-ai-draw-io</a>）</td><td>AI 生成/编辑 draw.io 图表，实时浏览器预览</td><td>已启用；<code>npx @next-ai-drawio/mcp-server@latest</code></td><td>MCP server：按需拉起 stdio 进程，模型调用 create/get/edit 工具改 <code>.drawio</code> 源文件，内置 HTTP 实时预览；进程结束后可能残留，需手动清理</td></tr>
    <tr><td>Next AI Draw.io（桌面客户端）</td><td>安装包</td><td>0.4.16</td><td>GitHub（<a href="https://github.com/DayuanJiang/next-ai-draw-io/releases">DayuanJiang/next-ai-draw-io</a>）</td><td>AI 增强的 draw.io 桌面绘图（macOS + Windows）</td><td>已收录；位置 <code>installers/next-ai/</code>；dmg <code>c829735a…</code>、exe <code>f12a048f…</code></td><td></td></tr>
    <tr><td>炒股</td><td>StockWin</td><td>skill</td><td>—</td><td>自己创建</td><td>A 股专业分析：智能选股、持仓深度分析、卖出/止盈止损策略（资金面优先）</td><td>已装</td><td></td></tr>
    <tr><td>求职</td><td>offer</td><td>skill</td><td>—</td><td>自己创建</td><td>求职助手：岗位搜索与评估、投递追踪、简历与岗位分析</td><td>已装</td><td></td></tr>
    <tr><td>规划</td><td>grill-me / grilling</td><td>skill</td><td>—</td><td>GitHub（<a href="https://github.com/mattpocock/skills">mattpocock/skills</a>）</td><td>追问式访谈打磨方案：grill-me 是入口，grilling 是具体会话流程（按设计树分轮拷问）</td><td>已装；同源同流程</td><td></td></tr>
    <tr><td>自动化</td><td>computer-use</td><td>mcp</td><td>—</td><td>系统自带（Codex 客户端）</td><td>通过 Computer Use 控制 macOS 桌面应用</td><td>未启用（enabled=false）</td><td></td></tr>
  </tbody>
</table>

## 维护约定

- 本文件人工维护：新增/删除工具后，在工具清单中加/删一行；同作用分类的多行共享一个合并分类单元格。
- `tools/INDEX.md` 由 `sync.py` 自动生成，只做机械索引；本文件才是给人看的"有什么、能干嘛"。
- 机器生成区（`skills/`、`agents/`、`mcp/`）勿手改；手写心得放 `tools/docs/`。
