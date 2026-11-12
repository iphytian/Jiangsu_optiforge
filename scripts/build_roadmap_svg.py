#!/usr/bin/env python3
"""Generate the public roadmap/relationship SVG used by README and Project README.

No third-party dependencies; no personal names or project numbers are included.
"""
import html
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "project-roadmap.svg"

W, H = 1800, 1020
CHART_L, CHART_R = 220, 1720
START, END = date(2026, 7, 1), date(2029, 6, 30)
INK = "#0d1b2e"
PAPER = "#f7f4ec"
MUTED = "#6f6a60"
GOLD = "#b78b4a"
LINE = "#ded6c6"
ARROW = "#7c7466"

COLORS = {
    "C1": "#2f7f7a",
    "C2": "#3f6fa8",
    "C3": "#b07a2a",
    "C4": "#7a5aa6",
    "C5": "#4d7a4a",
}
ROWS = {
    "C1": (390, "协同框架", "决策调度"),
    "C2": (500, "面形检测", "原位检测"),
    "C3": (610, "磨制策略", "全参数优化"),
    "C4": (720, "磨制执行", "健康感知"),
    "C5": (830, "系统集成", "800mm 验证"),
}
GATES = [
    ("G0", "2026-10-21", "启动", "diamond"),
    ("P1", "2026-12-31", "方案冻结", "square"),
    ("G1", "2027-02-25", "方案评审", "diamond"),
    ("M1", "2027-12-24", "中期", "diamond"),
    ("G3", "2028-06-30", "联调", "diamond"),
    ("M2", "2028-12-22", "指标", "diamond"),
    ("G5", "2029-06-27", "验收", "diamond"),
]
NODES = {
    "C1": [
        ("C1-1", "2027-06-30", "重点区域与策略约束"),
        ("C1-2", "2027-12-24", "闭环决策与工艺切换"),
        ("C1-3", "2028-12-22", "协同框架指标"),
    ],
    "C2": [
        ("C2-1", "2027-06-30", "激光视觉与 PMD 融合"),
        ("C2-2", "2027-12-24", "抗扰检测与缺陷巡检"),
        ("C2-3", "2028-12-22", "原位检测指标"),
    ],
    "C3": [
        ("C3-1", "2027-06-30", "瞬态模型与研磨特性"),
        ("C3-2", "2027-12-24", "全参数策略生成"),
        ("C3-3", "2028-12-22", "磨制策略指标"),
    ],
    "C4": [
        ("C4-1", "2027-06-30", "退化感知与量化"),
        ("C4-2", "2027-12-24", "故障定位与自主响应"),
        ("C4-3", "2028-12-22", "执行智能体指标"),
    ],
    "C5": [
        ("C5-1", "2027-12-24", "中期原型集成"),
        ("C5-2", "2028-12-22", "800mm 镜面与指标"),
    ],
}


def x_of(d: str) -> float:
    y, m, day = map(int, d.split("-"))
    cur = date(y, m, day)
    return CHART_L + (cur - START).days / (END - START).days * (CHART_R - CHART_L)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def text(x, y, s, size=12, fill=INK, weight="400", anchor="start", family="sans", extra=""):
    fam = "'Songti SC','Noto Serif SC',serif" if family == "serif" else "'PingFang SC','Noto Sans SC','Microsoft YaHei',sans-serif"
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}" font-family="{fam}" {extra}>{esc(s)}</text>'
    )


def card(cx, cy, node_id, d, title, color):
    w, h = 180, 58
    x, y = cx - w / 2, cy - h / 2
    date_label = d[:7].replace("-", ".")
    return f'''<g class="node">
  <rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="10" fill="#fffdf8" stroke="{color}" stroke-width="1.2" filter="url(#soft)"/>
  <rect x="{x+1:.1f}" y="{y+8:.1f}" width="3.5" height="{h-16}" rx="1.75" fill="{color}"/>
  {text(x+13, y+16, node_id, 9.5, color, "700")}
  {text(x+13, y+34, title, 12.5, INK, "600")}
  {text(x+13, y+49, f"{date_label} · KeyTech", 8.6, MUTED, "400")}
</g>'''


def gate_symbol(x, kind, label):
    if kind == "square":
        shape = f'<rect x="{x-11:.1f}" y="239" width="22" height="22" rx="5" fill="#efe3cf" stroke="{GOLD}" stroke-width="1.4"/>'
    else:
        shape = f'<path d="M {x:.1f} 235 L {x+15:.1f} 250 L {x:.1f} 265 L {x-15:.1f} 250 Z" fill="{INK}" stroke="{GOLD}" stroke-width="1.2"/>'
    return shape


def arrow_line(x1, y1, x2, y2, color=ARROW, width=1.1, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}"{d} marker-end="url(#arrow)"/>'


parts = []
parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="title desc">
<title id="title">研究内容与关键节点关系</title>
<desc id="desc">五项研究内容、关键技术节点与项目 Gate 的公开关系图。实线箭头表示前后依赖，竖向虚线表示 Gate 时间，颜色表示研究方向。</desc>
<defs>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="160%">
    <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0d1b2e" flood-opacity="0.08"/>
  </filter>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="{ARROW}"/>
  </marker>
</defs>
<rect width="{W}" height="{H}" fill="{PAPER}"/>
<g opacity="0.35" stroke="#ffffff" stroke-width="1">
  <path d="M 0 1 H {W} M 0 1019 H {W}"/>
</g>
''')

# Header
parts.append(text(70, 55, "PUBLIC ROADMAP / 2026—2029", 10.5, GOLD, "700", extra='letter-spacing="2.2"'))
parts.append(text(70, 105, "研究内容与关键节点关系", 44, INK, "600", family="serif", extra='letter-spacing="-1"'))
parts.append(text(70, 136, "五项研究内容 · 关键技术节点 · 项目 Gate", 13.5, MUTED))
parts.append(text(70, 156, "实线箭头表示前置/后续；竖向虚线表示 Gate 对齐；颜色表示研究方向", 10, MUTED))
parts.append(f'<line x1="70" y1="172" x2="1730" y2="172" stroke="{LINE}" stroke-width="1"/>')

# Legend
lx = 1270
parts.append(text(lx, 70, "图例 / LEGEND", 9, GOLD, "700", extra='letter-spacing="1.6"'))
parts.append(f'<path d="M {lx} 92 L {lx+10} 102 L {lx} 112 L {lx-10} 102 Z" fill="{INK}" stroke="{GOLD}" stroke-width="1"/>')
parts.append(text(lx+18, 106, "项目 Gate", 10, INK))
parts.append(f'<rect x="{lx-8}" y="124" width="16" height="16" rx="4" fill="#efe3cf" stroke="{GOLD}" stroke-width="1"/>')
parts.append(text(lx+18, 136, "阶段 / Phase", 10, INK))
parts.append(f'<rect x="{lx-8}" y="151" width="16" height="16" rx="4" fill="#fffdf8" stroke="{COLORS["C1"]}" stroke-width="1.2"/>')
parts.append(text(lx+18, 163, "关键节点", 10, INK))

lx2 = 1510
parts.append(f'<line x1="{lx2}" y1="98" x2="{lx2+38}" y2="98" stroke="{ARROW}" stroke-width="1.1" marker-end="url(#arrow)"/>')
parts.append(text(lx2+46, 101, "依赖关系", 10, INK))
parts.append(f'<line x1="{lx2}" y1="126" x2="{lx2+38}" y2="126" stroke="{GOLD}" stroke-width="1" stroke-dasharray="4 4"/>')
parts.append(text(lx2+46, 129, "Gate 对齐", 10, INK))
parts.append(text(lx2, 155, "21 节点 / 5 方向", 10, MUTED, "600"))

# Year grid
for x, label in [(CHART_L, "2026"), (x_of("2027-01-01"), "2027"), (x_of("2028-01-01"), "2028"), (x_of("2029-01-01"), "2029")]:
    parts.append(f'<line x1="{x:.1f}" y1="190" x2="{x:.1f}" y2="885" stroke="#e9e1d2" stroke-width="1"/>')
    parts.append(text(x, 196, label, 9, "#a09888", "600", extra='letter-spacing="1"'))

# Gate verticals (behind cards), gate chain, symbols
for gid, gd, short, kind in GATES:
    gx = x_of(gd)
    parts.append(f'<line x1="{gx:.1f}" y1="266" x2="{gx:.1f}" y2="885" stroke="{GOLD}" stroke-width="1" stroke-dasharray="3 6" opacity="0.38"/>')

for i, (gid, gd, short, kind) in enumerate(GATES):
    gx = x_of(gd)
    if i + 1 < len(GATES):
        nx = x_of(GATES[i + 1][1])
        parts.append(arrow_line(gx + 18, 250, nx - 18, 250, GOLD, 1.2))
    parts.append(gate_symbol(gx, kind, gid))
    parts.append(text(gx, 224, gid, 10, INK, "700", anchor="middle", extra='letter-spacing="1"'))
    parts.append(text(gx, 284, gd[:7].replace("-", "."), 8.2, MUTED, "500", anchor="middle"))

# Row separators and labels
for key, (cy, title, sub) in ROWS.items():
    color = COLORS[key]
    parts.append(f'<line x1="{CHART_L}" y1="{cy+55}" x2="{CHART_R}" y2="{cy+55}" stroke="{LINE}" stroke-width="1"/>')
    parts.append(f'<rect x="70" y="{cy-28}" width="3" height="56" rx="1.5" fill="{color}"/>')
    parts.append(text(82, cy-14, key, 9, color, "700", extra='letter-spacing="1.5"'))
    parts.append(text(82, cy+5, title, 18, INK, "600"))
    parts.append(text(82, cy+23, sub, 9.5, MUTED))

# G1 -> first checkpoints bus
g1x = x_of("2027-02-25")
parts.append(f'<path d="M {g1x:.1f} 266 C {g1x+18:.1f} 266 {600} 280 {600} 310 L 600 830" fill="none" stroke="{ARROW}" stroke-width="1" opacity="0.65"/>')
parts.append(text(608, 326, "G1 后启动", 8.5, MUTED, "500"))
for key, (cy, _, _) in ROWS.items():
    first_x = x_of(NODES[key][0][1])
    left = first_x - 90
    parts.append(f'<circle cx="600" cy="{cy}" r="2" fill="{ARROW}"/>')
    parts.append(arrow_line(600, cy, left, cy, ARROW, 1, "3 3"))

# Row dependency arrows
for key, nodes in NODES.items():
    cy = ROWS[key][0]
    for a, b in zip(nodes, nodes[1:]):
        x1 = x_of(a[1]) + 90
        x2 = x_of(b[1]) - 90
        parts.append(arrow_line(x1, cy, x2, cy, ARROW, 1.1))

# Cards
for key, nodes in NODES.items():
    cy = ROWS[key][0]
    for nid, d, title in nodes:
        parts.append(card(x_of(d), cy, nid, d, title, COLORS[key]))

# Gate labels / footer chain
parts.append(text(70, 922, "主依赖链", 9, GOLD, "700", extra='letter-spacing="1.5"'))
parts.append(text(170, 922, "G0 → P1 → G1 → 关键技术验证 → M1 → G3 → 指标验证 → M2 → G5", 11, INK, "500"))
parts.append(text(70, 955, "G0 启动 · P1 方案与接口冻结 · G1 总体方案评审 · M1 中期里程碑 · G3 集成联调 · M2 指标达成 · G5 项目验收", 9, MUTED))
parts.append(f'<line x1="70" y1="968" x2="1730" y2="968" stroke="{LINE}" stroke-width="1"/>')
parts.append(text(70, 990, "公开版 · 仅含节点、日期与依赖关系 · 不含个人与内部信息", 8.5, MUTED))
parts.append(text(1730, 990, "01 / 01", 8.5, MUTED, "500", anchor="end"))

parts.append("</svg>")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts), encoding="utf-8")
print("wrote", OUT, OUT.stat().st_size, "bytes")
