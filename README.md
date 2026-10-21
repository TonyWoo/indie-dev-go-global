# 《一个人出海》

**独立开发者 App 出海实战——找需求、快速造产品、SEO 增长与商业化实验**

作者：Tony Wu ｜ 联系：tonywoo@outlook.com

这是一本写给想做出海独立产品、或正在做的开发者的实战书：独立开发者做 App 出海，
要具备的不是某一项单点技能，而是一条完整的能力链——找得到海外需求，
用 AI Coding 一个人把产品快速做出来，懂 SEO 和增长，靠一轮轮实验做商业化，
同时有产品 Sense 和商业判断，最后攒出一段从 0 到 1 的完整经验。

贯穿全书的案例是 **陈屿**：一位前大厂后端工程师，业余时间做出面向海外用户的
截图美化工具 SnapPolish，从找需求、上线、SEO 增长、定价实验，一路走到给自己
出"两周测试"题。你会跟着他走完从 0 到 1 的全程。
（案例人物与产品为虚构，数字为示意，方法都是真实可用的。）

## 章节大纲（前言 + 7 章）

| 章 | 目录 | 主题 |
|---|---|---|
| 前言 | `content/zh/000-preface/` | 写在前面：先看懂这张能力地图 |
| 1 | `content/zh/010-finding-demand/` | 找需求：去海外用户的抱怨里挖金子 |
| 2 | `content/zh/020-ship-fast/` | 快速造产品：用 AI Coding 一个人走完从想法到上线 |
| 3 | `content/zh/030-seo-growth/` | SEO 与增长：让 Google 把用户送到你门口 |
| 4 | `content/zh/040-experiments/` | 实验驱动：把增长拆成一轮轮小实验 |
| 5 | `content/zh/050-product-sense/` | 产品 Sense：动手之前先想清楚四件事 |
| 6 | `content/zh/060-zero-to-one/` | 从 0 到 1：攒一段能说服人的独立经验 |
| 7 | `content/zh/070-two-week-test/` | 两周测试：给自己一场无人指派的实战 |

每章体例：白话讲解 + 贯穿案例推进 + 本章要点 + 动手 Kata + 翻车现场。
全书写作规范与案例数据口径见 `WRITING.md`。

## 书站

本站用 Astro + Nimbus 构建，源码在 `site/`，push 到 main 后由 GitHub Actions
自动部署到 GitHub Pages：https://tonywoo.github.io/indie-dev-go-global/

本地预览：

```bash
cd site
npm ci
npm run dev   # prebuild 会自动把 content/zh/ 书稿导入站点
```
