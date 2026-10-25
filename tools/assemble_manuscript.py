#!/usr/bin/env python3
"""把 content/zh/ 下前言 + 7 章 _index.md 装配成单文件 manuscript.md（供 Pandoc 构建 PDF/EPUB）。

装配规则（对齐《无工之日》的 export 管线）：
- 开头生成扉页：书名（Pandoc 不编号标记 {-}）+ 作者 + 副标题题引。
- 每章标题取自各 _index.md 的 frontmatter title，作为 H1；章内小节（##）保持不动，
  使目录里章、小节分层（--toc-depth=2）；EPUB 用 --split-level=1 按章切分。
- frontmatter 在装配时剥离；本书无配图，无需改写图片路径。

用法：python3 tools/assemble_manuscript.py [输出文件]
默认输出仓库根 manuscript.md。
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "zh"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "manuscript.md"

TITLE = "一个人出海"
SUBTITLE = "独立开发者 App 出海实战——找需求、快速造产品、SEO 增长与商业化实验"
AUTHOR = "Tony Wu"

DOCS = [
    "000-preface",
    "010-finding-demand",
    "020-ship-fast",
    "030-seo-growth",
    "040-experiments",
    "050-product-sense",
    "060-zero-to-one",
    "070-two-week-test",
]


def parse_doc(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"bad frontmatter: {path}")
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    if "title" not in meta:
        raise ValueError(f"missing title: {path}")
    return meta["title"], m.group(2).strip("\n")


def main():
    parts = []
    parts.append(f"# {TITLE} {{-}}\n\n{AUTHOR}\n\n> {SUBTITLE}\n")

    for slug in DOCS:
        path = CONTENT / slug / "_index.md"
        if not path.exists():
            raise SystemExit(f"missing doc: {path}")
        title, body = parse_doc(path)
        parts.append(f"# {title}\n\n{body}\n")

    OUT.write_text("\n".join(parts), encoding="utf-8")
    han = len(re.findall(r"[一-鿿]", OUT.read_text(encoding="utf-8")))
    print(f"assembled -> {OUT} （{len(DOCS)} 篇，汉字约 {han}）")


if __name__ == "__main__":
    main()
