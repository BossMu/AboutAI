#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AboutAI 安装脚本：在新机器上从资料包恢复工具。

用法:
    python3 scripts/install.py             # 预览并执行恢复
    python3 scripts/install.py --dry-run   # 只预览不执行
"""

import argparse
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AGENTS_DIR = Path.home() / ".agents"

PAIRS = [
    ("tools/skills", "skills"),
    ("tools/agents", "agents"),
]


def main():
    parser = argparse.ArgumentParser(description="AboutAI 安装脚本")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不执行")
    args = parser.parse_args()

    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for src_rel, dst_name in PAIRS:
        src = BASE / src_rel
        dst = AGENTS_DIR / dst_name
        if not src.exists() or not any(p for p in src.iterdir() if not p.name.startswith(".")):
            print(f"[跳过] {src_rel}/ 为空或不存在")
            continue
        dst.mkdir(parents=True, exist_ok=True)
        for item in sorted(src.iterdir()):
            if item.name.startswith("."):
                continue
            target = dst / item.name
            if target.exists():
                print(f"[跳过] {item.name} 已存在：{target}")
                continue
            if args.dry_run:
                print(f"[预览] {item.name} -> {target}")
                continue
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)
            print(f"[安装] {item.name} -> {target}")

    print("")
    print("MCP 合并指南：tools/mcp/ 下的 .toml 片段需要手动合并进 ~/.codex/config.toml。")
    print("步骤：打开 ~/.codex/config.toml，把对应 [mcp_servers.*] 片段粘贴进去；")
    print("      片段中的 <redacted> 占位符需填入真实 token/key 后再启用。")


if __name__ == "__main__":
    main()
