# 参与与提交

本仓库只接受**可公开的通知和节点信息**。提交前请先读 [PUBLICATION-POLICY.md](PUBLICATION-POLICY.md)。

## 项目组成员

### 提交一条公开通知

1. 打开 Issues → New issue → **提交公开通知**。
2. 填写标题、日期、分类、摘要和正文。
3. 勾选“可公开”“无个人/内部信息”两项确认。
4. 维护者审核后，在 `docs/notices/` 新建 Markdown 文件，合并到 `main`。
5. 合并前运行 `python3 scripts/build_docs.py`，把更新后的 `README.md`、`docs/notices.md` 一起提交；PR 会校验生成文件是否最新。

通知文件格式：

```markdown
---
title: 标题
date: 2026-11-11
category: 项目动态
summary: 一句话摘要
---

正文，使用 Markdown。
```

### 更正

Issues → New issue → **更正/补充**，写清页面、错误点和依据。不要直接改别人的条目。

## 维护者

### 本地检查

```bash
python3 scripts/validate_data.py
python3 scripts/build_docs.py
```

提交前确保两个脚本都通过，并且 `git diff` 只包含预期变更。

### 更新节点

编辑 `data/milestones.csv`：

| 字段 | 说明 |
|---|---|
| `id` | G0/G1/M1/G3/M2/G5 |
| `name` | 节点名称 |
| `planned_date` | 计划日期，`YYYY-MM-DD` 或 `YYYY-MM` |
| `actual_date` | 实际日期，未发生留空 |
| `status` | `completed` / `upcoming` / `planned` |
| `public_deliverable` | 可公开的交付物类型 |
| `owner` | 项目组 / 技术工作组，不写个人姓名 |

### 提交信息

建议使用：

- `docs: add notice 2026-11-11`
- `docs: update G1 date`
- `docs: rebuild public index`

### PR 检查

- [ ] `python3 scripts/validate_data.py` 通过
- [ ] `python3 scripts/build_docs.py` 后无意外 diff
- [ ] 没有个人姓名、联系方式、照片或身份信息
- [ ] 没有内部资料或不宜公开的编号
- [ ] 日期、分类和正文一致

## 外部公众

欢迎指出错误或失效链接：

- 使用 **更正/补充** Issue；
- 不要提交个人隐私或内部资料；
- 维护者会核实，但不承诺采纳所有建议。

## 行为规范

- 只讨论公开信息，不猜测未公开事项。
- 不发布他人个人信息、不引战、不进行商业推广。
- 维护者可以关闭偏离主题或包含不宜公开信息的 Issue。
