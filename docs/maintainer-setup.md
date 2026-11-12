# 维护者配置清单

本文件用于配置 `Jiangsu_optiforge` 公开仓库和公开看板。仓库管理员操作一次即可。

## 1. 仓库基本信息

Settings → General：

- Description：`基于多智能体的大口径光学镜面精密制造与检测技术研发`
- Website：暂时留空
- Topics：`astronomical-optics`, `optical-fabrication`, `metrology`, `multi-agent`, `jiangsu`
- Features：
  - Issues：开启
  - Projects：开启
  - Discussions：可选
  - Wiki：关闭
- Pages：暂时关闭

## 2. 标签

Settings → Labels，保留或创建：

| 标签 | 用途 |
|---|---|
| `submission` | 新提交，待审核 |
| `notice` | 公开通知 |
| `correction` | 更正 |
| `needs-review` | 待维护者审核 |
| `approved` | 审核通过，待合并 |
| `published` | 已合并发布 |
| `blocked` | 缺少公开依据或不宜公开 |

Issue 表单引用了 `submission`、`notice` 和 `correction`；如果标签不存在，GitHub 不会自动创建。

## 3. 公开 Projects 看板

当前公开看板：

- 名称：`OptiForge_Public_Roadmap`
- 地址：https://github.com/users/iphytian/projects/1
- 可见性：Public

建议字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| Gate | Text | G0/G1/M1/G3/M2/G5；研究节点可留空 |
| Workstream | Text | 协同框架 / 面形检测 / 磨制策略 / 磨制执行 / 系统集成 / 项目管理 |
| NodeType | Text | Gate / Phase / KeyTech |
| Phase | Text | P1—P6 |
| Target date | Date | 计划日期 |
| Status | Single select | Planned / Next / Done |
| Deliverable | Text | 公开交付物类型 |

6 个 Gate 条目：

| Gate | 名称 | 日期 | 状态 |
|---|---|---|---|
| G0 | 项目启动 | 2026-10-21 | Done |
| G1 | 总体方案评审 | 2027-02-25 | Next |
| M1 | 中期里程碑 | 2027-12-24 | Planned |
| G3 | 集成联调完成 | 2028-06-30 | Planned |
| M2 | 主要指标达成 | 2028-12-22 | Planned |
| G5 | 项目验收 | 2029-06-27 | Planned |

研究内容节点见 `docs/research-milestones.md`。看板建议按 `Workstream` 增加 14—16 个研究节点和 1 个 P1 方案冻结节点。

如果看板未关联仓库：

`...` → **Settings** → **Linked repositories** → **Link a repository** → 选 `iphytian/Jiangsu_optiforge`。

Projects 的可见性独立于仓库。以后如果仓库转私有，必须单独把 Project 改为 private。

## 4. 分支保护

Settings → Branches → Add branch protection rule：

- Branch name pattern：`main`
- Require a pull request before merging
- Required approvals：1
- Require status checks to pass before merging
  - `Validate public data`
  - `Verify generated docs are current`
- Require conversation resolution before merging
- Do not allow bypassing the above settings
- 禁止 force push

`build-docs` 只在 PR 中校验，不向 `main` 直推，因此不会被分支保护阻塞。

## 5. Actions 权限

Settings → Actions → General：

- Actions permissions：Allow all actions and reusable workflows
- Workflow permissions：Read and write permissions
- 不勾选 Allow GitHub Actions to create and approve pull requests

工作流：

- `validate.yml`：在 PR 和 main push 时校验节点与通知
- `build-docs.yml`：在 PR 中重建索引，检查生成文件是否最新
- `release-snapshot.yml`：每月 1 日生成公开快照 Release，也可手动触发

## 6. CODEOWNERS

复制 `CODEOWNERS.example` 为 `.github/CODEOWNERS`，把占位账号替换成实际维护者或团队。

CODEOWNERS 只负责 review 请求，不等于访问控制。

## 7. 安全检查

Settings → Code security：

- 开启 Secret scanning
- 开启 Push protection（如可用）
- 开启 Dependabot alerts

公开仓库允许外部提 Issue；维护者及时关闭偏离主题或含不宜公开信息的 Issue。

## 8. 发布前检查

- [ ] 仓库是 public
- [ ] 没有个人姓名、联系方式、照片或身份信息
- [ ] 没有不宜公开的资料或编号
- [ ] `python3 scripts/validate_data.py` 通过
- [ ] `python3 scripts/build_docs.py` 后 README/索引已更新
- [ ] 6 个 Gate 已加入公开看板，G1 日期为 2027-02-25
- [ ] 分支保护已开启
- [ ] `CITATION.cff` 的组织占位符已替换

## 9. 替换占位符

发布前替换：

- `CITATION.cff` 中的 `REPLACE-WITH-ORG`
- `CODEOWNERS.example` 中的占位账号
- README 中的维护者说明（如需要）
- `docs/about.md` 中的联系说明（如单位有统一公开联系方式）
