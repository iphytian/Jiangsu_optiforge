#!/usr/bin/env python3
"""Validate public notices and milestones before a PR is merged.

Only Python's standard library is used. The checks focus on:
- required fields and date formats;
- public-only content (no internal/restricted markers);
- no personal contact details or personal-name signatures;
- no binary documents in the repository.
"""
import csv
import re
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
NOTICES = DOCS / "notices"

MILESTONE_FIELDS = ["id", "name", "planned_date", "actual_date", "status", "public_deliverable", "owner"]
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
PHONE_RE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ID_RE = re.compile(r"\b\d{17}[\dXx]\b")
# Generic project-code shape; the actual code is intentionally not stored in this repository.
PROJECT_CODE_RE = re.compile(r"\bSBF\d{6,}\b", re.I)
# Detect a personal signature after a role label without hard-coding any name.
SIGNATURE_RE = re.compile(r"(项目负责人|执行负责人|联系人|编制|审核)[：:]\s*[^\s，。；、|]+")
BINARY_SUFFIXES = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".zip", ".7z", ".rar"}
TEXT_SUFFIXES = {".md", ".csv", ".cff", ".txt"}

errors: List[str] = []
warnings: List[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read_milestones() -> List[Dict[str, str]]:
    path = DATA / "milestones.csv"
    if not path.exists():
        err("缺少 data/milestones.csv")
        return []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        if fields != MILESTONE_FIELDS:
            err("milestones.csv 表头不一致\n  期望：{0}\n  实际：{1}".format(MILESTONE_FIELDS, fields))
        return list(reader)


def check_milestones(rows: List[Dict[str, str]]) -> None:
    if not rows:
        err("milestones.csv 没有数据")
        return
    if len(rows) != 6:
        warn("milestones.csv 当前有 {0} 条；公开计划为 6 个节点".format(len(rows)))
    seen = set()
    for i, r in enumerate(rows, start=2):
        where = "milestones.csv:{0} ({1})".format(i, r.get("id"))
        if not r.get("id"):
            err(where + ": id 不能为空")
        if r.get("id") in seen:
            err(where + ": id 重复")
        seen.add(r.get("id"))
        if r.get("status") not in {"completed", "upcoming", "planned"}:
            err(where + ": status 必须是 completed/upcoming/planned")
        for field in ("name", "planned_date", "public_deliverable", "owner"):
            if not (r.get(field) or "").strip():
                err(where + ": {0} 不能为空".format(field))
        for field in ("planned_date", "actual_date"):
            value = (r.get(field) or "").strip()
            if value and not DATE_RE.fullmatch(value):
                err(where + ": {0} 必须是 YYYY、YYYY-MM 或 YYYY-MM-DD".format(field))


def check_notices() -> None:
    if not NOTICES.exists():
        err("缺少 docs/notices/ 目录")
        return
    for path in sorted(NOTICES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            err(path.name + ": 缺少 front matter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            err(path.name + ": front matter 未闭合")
            continue
        meta: Dict[str, str] = {}
        for line in parts[1].splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
        for field in ("title", "date", "category", "summary"):
            if not meta.get(field):
                err(path.name + ": front matter 缺少 {0}".format(field))
        if meta.get("date") and not DATE_RE.fullmatch(meta["date"]):
            err(path.name + ": date 格式错误")
        if not parts[2].strip():
            err(path.name + ": 正文为空")


def check_text_safety() -> None:
    candidates = [ROOT / "README.md"]
    candidates += sorted(DOCS.glob("*.md"))
    candidates += sorted(DOCS.glob("notices/*.md"))
    candidates += [ROOT / "PUBLICATION-POLICY.md", ROOT / "CONTRIBUTING.md", ROOT / "DISCLAIMER.md", ROOT / "CONTENT-LICENSE.md", ROOT / "CITATION.cff", DATA / "milestones.csv"]
    for path in candidates:
        if not path.exists() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if PHONE_RE.search(text):
            err("{0}: 含疑似手机号".format(rel))
        if EMAIL_RE.search(text) and "github-actions[bot]@users.noreply.github.com" not in text:
            err("{0}: 含疑似邮箱".format(rel))
        if ID_RE.search(text):
            err("{0}: 含疑似身份证号".format(rel))
        if PROJECT_CODE_RE.search(text):
            err("{0}: 含疑似项目编号".format(rel))
        for m in SIGNATURE_RE.finditer(text):
            err("{0}: 疑似个人署名“{1}”".format(rel, m.group(0)[:30]))


def check_no_binary_docs() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in BINARY_SUFFIXES:
            err("禁止提交二进制文档：{0}".format(path.relative_to(ROOT)))


def check_readme() -> None:
    path = ROOT / "README.md"
    if not path.exists():
        err("缺少 README.md")
        return
    text = path.read_text(encoding="utf-8")
    for marker in ("STATS", "LATEST_NOTICES", "MILESTONES"):
        if "<!-- {0}:START -->".format(marker) not in text or "<!-- {0}:END -->".format(marker) not in text:
            err("README.md 缺少 {0} 标记".format(marker))


def main() -> None:
    rows = read_milestones()
    check_milestones(rows)
    check_notices()
    check_text_safety()
    check_no_binary_docs()
    check_readme()

    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    print("\n{0} milestones, {1} notices".format(len(rows), len(list(NOTICES.glob("*.md")))))
    if errors:
        print("\nFAILED with {0} error(s)".format(len(errors)))
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
