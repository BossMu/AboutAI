#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AboutAI 同步脚本。

导出 ~/.agents/skills、~/.agents/agents 到 tools/，提取并脱敏 MCP 配置，
重建 tools/INDEX.md，可选打包 zip。

用法:
    python3 scripts/sync.py            # 同步 + 重建索引
    python3 scripts/sync.py --zip      # 同步并打包
"""

import argparse
import datetime
import fnmatch
import re
import shutil
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AGENTS_DIR = Path.home() / ".agents"
CODEX_CONFIG = Path.home() / ".codex" / "config.toml"

TOOLKIT = BASE / "tools"
INDEX_PATH = TOOLKIT / "INDEX.md"
MCP_DIR = TOOLKIT / "mcp"

SECRET_KEYS = ("key", "token", "secret", "password", "authorization", "bearer")
SECTION_RE = re.compile(r"^\[([^\]]+)\]")
KV_RE = re.compile(r'^([A-Za-z0-9_.\-]+)\s*=\s*(.*)$')


def load_ignore():
    rules = []
    path = BASE / ".syncignore"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                rules.append(line)
    return rules


def ignored(rel, rules):
    text = rel.as_posix()
    return any(
        fnmatch.fnmatch(text, rule) or fnmatch.fnmatch(rel.name, rule)
        for rule in rules
    )


def copytree_filtered(src, dst, base_rel, rules):
    dst.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in sorted(src.iterdir()):
        rel = base_rel / item.name
        if item.name == ".DS_Store" or ignored(rel, rules):
            print(f"[排除] {rel.as_posix()}")
            continue
        if item.is_dir():
            count += copytree_filtered(item, dst / item.name, rel, rules)
        else:
            shutil.copy2(item, dst / item.name)
            count += 1
    return count


def export_agents_dir(name, rules):
    """整目录导出 ~/.agents/<name> 到 tools/<name>，先清空生成区再镜像。"""
    src = AGENTS_DIR / name
    dst = TOOLKIT / name
    dst.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        print(f"[跳过] {name}/ 不存在（{src}），保留空目录")
        return 0
    for item in dst.iterdir():
        if item.name == ".DS_Store":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    count = copytree_filtered(src, dst, Path(name), rules)
    print(f"[完成] {name}/: 导出 {count} 项")
    return count


def redact(line):
    m = KV_RE.match(line.strip())
    if not m:
        return line
    key = m.group(1).lower()
    if any(s in key for s in SECRET_KEYS):
        return f'{m.group(1)} = "<redacted>"'
    return line


def extract_mcp(config_path):
    """从 config.toml 提取 [mcp_servers.*] 片段并脱敏。"""
    servers = {}
    current = None
    if not config_path.exists():
        print(f"[跳过] 未找到 {config_path}")
        return servers
    for raw in config_path.read_text(encoding="utf-8").splitlines():
        stripped = raw.strip()
        m = SECTION_RE.match(stripped)
        if m:
            name = m.group(1)
            if name.startswith("mcp_servers.") and name.count(".") == 1:
                current = name.split(".", 1)[1]
                servers.setdefault(current, [])
                servers[current].append(f"[mcp_servers.{current}]")
            elif current and name.startswith("mcp_servers."):
                servers[current].append(raw)  # 子表头，如 env
            else:
                current = None
            continue
        if current:
            servers[current].append(redact(raw))
    return servers


def write_mcp(servers):
    MCP_DIR.mkdir(parents=True, exist_ok=True)
    for item in MCP_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    for name, lines in sorted(servers.items()):
        (MCP_DIR / f"{name}.toml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[完成] mcp/: 导出 {len(servers)} 个 server（已脱敏）")


def build_index():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# AboutAI 工具包索引",
        "",
        f"> 由 scripts/sync.py 自动生成（{now}），请勿手改。手写内容请放 tools/docs/ 等目录。",
        "",
    ]
    sections = [
        ("skills", "Skills"),
        ("agents", "Agents"),
        ("mcp", "MCP 服务器"),
        ("prompts", "提示词"),
        ("scripts", "脚本 / 工作流"),
        ("configs", "配置模板"),
        ("installers", "安装包"),
    ]
    for folder, title in sections:
        lines.append(f"## {title}")
        lines.append("")
        d = TOOLKIT / folder
        entries = sorted(p for p in d.iterdir() if not p.name.startswith(".")) if d.exists() else []
        if not entries:
            lines.append("- （暂无，预留）")
        else:
            for item in entries:
                link = item.relative_to(BASE).as_posix()
                if item.is_dir():
                    lines.append(f"- {item.name}/ — [{link}/]({link}/)")
                else:
                    lines.append(f"- {item.name} — [{link}]({link})")
        lines.append("")
    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")
    print("[完成] INDEX.md 已重建")


def make_zip():
    out = BASE.parent / f"AboutAI-export-{datetime.date.today().isoformat()}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(BASE.rglob("*")):
            if ".git" in p.parts or p.name == ".DS_Store" or p.suffix == ".zip":
                continue
            if p.is_file():
                zf.write(p, p.relative_to(BASE.parent))
    print(f"[打包] {out}")


def main():
    parser = argparse.ArgumentParser(description="AboutAI 同步脚本")
    parser.add_argument("--zip", action="store_true", help="同步后打包为 zip")
    args = parser.parse_args()

    rules = load_ignore()
    total = 0
    for name in ("skills", "agents"):
        total += export_agents_dir(name, rules)
    servers = extract_mcp(CODEX_CONFIG)
    write_mcp(servers)
    build_index()
    print(f"[完成] 导出 {total} 项，MCP {len(servers)} 个，索引已重建。")
    if args.zip:
        make_zip()


if __name__ == "__main__":
    main()
