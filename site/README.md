# 项目网站

基于 [Scholar-Lite](https://github.com/fjd2004711/scholar-lite) 模板改造的项目公开网站，使用 Astro 5 + Tailwind CSS 4。

- 中文 / English 双语切换，入口在页面右上角
- 首页、项目简介（含五项研究方向）、项目进展、文章、专利、封面图片
- 文章/专利只发布立项后的公开成果；当前为空状态
- 中文标题使用系统黑体，中文正文使用系统宋体；英文使用 MiSans
- 图片来源与许可见 `/credits/`

## 本地运行

```bash
npm install
npm run dev
```

生产构建：

```bash
npm run build
npm run preview
```

构建输出在 `dist/`。

## 内容维护

| 内容 | 位置 |
|---|---|
| 项目名称、Hero、导航 | `src/config.ts` |
| 中文/英文正文 | `src/i18n/content.ts`、`src/content/` |
| 项目简介中的研究方向 | `src/content/research/` |
| 项目动态 | `src/content/activities/` |
| 项目节点 | `src/content/news/` |
| 文章 | `src/content/publications/` |
| 专利 | `src/content/patents/` |
| 图片来源 | `src/pages/credits.astro` |

文章、专利页面当前没有条目，新增 Markdown 后会自动进入列表。

## 语言

- 支持 `zh` / `en`
- 右上角 `中文 / EN` 按钮切换
- `?lang=zh`、`?lang=en` 可用于直接打开对应语言
- 页面标题、导航、正文、详情页和页脚都会切换

## 字体

- 中文标题：系统黑体（SimHei / PingFang SC / Heiti SC）
- 中文正文：系统宋体（STZhongsong / Songti SC / SimSun）
- 英文：自托管 MiSans 子集（Apache License 2.0）

详见 [FONT-NOTICE.md](FONT-NOTICE.md)。

## 模板与许可

- 模板：Scholar-Lite，MIT
- 页面版式参考 Academic Project Page
- 代码许可见 [LICENSE](LICENSE)
- 项目文字和自有图片的使用规则由项目组另行说明
