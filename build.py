"""Build the site: content/*.md + templates/base.html + static/ -> public/.

Usage:
    uv run build.py [--inline-css]
"""
import argparse
import shutil
from pathlib import Path

import frontmatter
import jinja2
from markdown_it import MarkdownIt
from mdit_py_plugins.attrs import attrs_block_plugin, attrs_plugin
from mdit_py_plugins.container import container_plugin

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "public"

# Names usable as ::: name ... ::: blocks in the Markdown files.
CONTAINERS = ("hero", "buttons", "grid", "card", "split", "col", "doc-links", "status")


def make_parser() -> MarkdownIt:
    md = MarkdownIt("commonmark").enable("table")
    md.use(attrs_plugin)        # [text](url){.btn .primary}
    md.use(attrs_block_plugin)  # {.lead} on the line before a block
    for name in CONTAINERS:
        md.use(container_plugin, name=name, marker=":")
    return md


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inline-css", action="store_true",
                    help="embed style.css in each page instead of linking it")
    args = ap.parse_args()

    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(STATIC, OUT)

    css = (STATIC / "style.css").read_text() if args.inline_css else None
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES),
                             autoescape=False)
    template = env.get_template("base.html")
    md = make_parser()

    for src in sorted(CONTENT.glob("*.md")):
        page = frontmatter.load(src)
        html = template.render(
            title=page["title"],
            description=page.get("description", ""),
            body=md.render(page.content),
            inline_css=css,
        )
        dest = OUT / f"{src.stem}.html"
        dest.write_text(html)
        print(f"{src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
