#!/usr/bin/env python3
"""Build the public notice index, milestone page and README summary.

Only Python's standard library is used so the workflow has no extra dependencies.
"""
import csv
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
NOTICES = DOCS / "notices"

GENERATED = "<!-- 本文件由 scripts/build_docs.py 自动生成；请修改 data/ 或 docs/notices/ 后重新运行。 -->\n"
STATUS_LABEL = {"completed": "✅ 已完成", "upcoming": "🔜 下一节点", "planned": "○ 计划"}


def read_milestones() -> List[Dict[str, str]]:
    with (DATA / "milestones.csv").open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def md_cell(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ").strip()


def parse_notice(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    meta: Dict[str, str] = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            for line in parts[1].splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip().strip('"').strip("'")
            body = parts[2].lstrip("\n")
    meta["body"] = body
    meta["path"] = path.name
    return meta


def notice_date(meta: Dict[str, str]) -> str:
    return meta.get("date", "1970-01-01")


def build_notices(notices: List[Dict[str, str]]) -> str:
    lines = [
        GENERATED,
        "# 项目动态\n",
        f"> 共 **{len(notices)}** 条公开通知。这里只发布可公开的信息；不宜公开的资料和个人信息不在本仓库。\n",
    ]
    for n in notices:
        title = md_cell(n.get("title", n["path"]))
        category = md_cell(n.get("category", "通知"))
        summary = md_cell(n.get("summary", ""))
        lines.append(f"\n## {n['date']} · {category}\n")
        lines.append(f"### [{title}](notices/{n['path']})\n")
        if summary:
            lines.append(summary)
    return "\n".join(lines).rstrip() + "\n"


def build_milestones(milestones: List[Dict[str, str]]) -> str:
    lines = [
        GENERATED,
        "# 关键节点\n",
        "> 仅公开六个阶段门/里程碑的日期、状态与交付物类型。任务明细、风险和评审细节不在本仓库。\n",
        "> 日期为公开计划；实际情况以项目组公告为准。\n",
        "",
        "| 节点 | 名称 | 计划日期 | 实际日期 | 状态 | 公开交付物 |",
        "|---|---|---|---|---|---|",
    ]
    for m in milestones:
        lines.append(
            "| {id} | {name} | {planned} | {actual} | {status} | {deliverable} |".format(
                id=m["id"],
                name=md_cell(m["name"]),
                planned=m["planned_date"],
                actual=m["actual_date"] or "—",
                status=STATUS_LABEL.get(m["status"], m["status"]),
                deliverable=md_cell(m["public_deliverable"]),
            )
        )
    return "\n".join(lines).rstrip() + "\n"


def replace_marker(text: str, marker: str, value: str) -> str:
    pattern = re.compile(r"<!-- {0}:START -->.*?<!-- {0}:END -->".format(marker), re.S)
    replacement = "<!-- {0}:START -->\n{1}\n<!-- {0}:END -->".format(marker, value.strip())
    if not pattern.search(text):
        raise SystemExit("README.md 缺少 {0} 标记".format(marker))
    return pattern.sub(replacement, text)


def build_readme(notices: List[Dict[str, str]], milestones: List[Dict[str, str]]) -> str:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    latest = sorted(notices, key=notice_date, reverse=True)[:3]
    latest_date = max((notice_date(n) for n in notices), default="—")

    stats = (
        f"- 公开节点：**{len(milestones)}** 个\n"
        f"- 公开通知：**{len(notices)}** 条\n"
        f"- 最近更新：**{latest_date}**"
    )
    text = replace_marker(text, "STATS", stats)

    notice_lines = []
    for n in latest:
        notice_lines.append(
            "- **{0}** · [{1}](docs/notices/{2})".format(
                n["date"], md_cell(n.get("title", n["path"])), n["path"]
            )
        )
    text = replace_marker(text, "LATEST_NOTICES", "\n".join(notice_lines))

    ms_lines = ["| 节点 | 名称 | 计划日期 | 状态 |", "|---|---|---|---|"]
    for m in milestones:
        ms_lines.append(
            "| {0} | {1} | {2} | {3} |".format(
                m["id"], md_cell(m["name"]), m["planned_date"], STATUS_LABEL.get(m["status"], m["status"])
            )
        )
    text = replace_marker(text, "MILESTONES", "\n".join(ms_lines))
    return text


def main() -> None:
    milestones = read_milestones()
    notices = [parse_notice(p) for p in sorted(NOTICES.glob("*.md"))]
    notices.sort(key=notice_date, reverse=True)

    changed = []
    for path, text in [
        (DOCS / "notices.md", build_notices(notices)),
        (DOCS / "milestones.md", build_milestones(milestones)),
        (ROOT / "README.md", build_readme(notices, milestones)),
    ]:
        if write_if_changed(path, text):
            changed.append(str(path.relative_to(ROOT)))

    print("notices={0} milestones={1}".format(len(notices), len(milestones)))
    print("changed:", ", ".join(changed) if changed else "none")


if __name__ == "__main__":
    main()
