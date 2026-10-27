# spylang-site

Source of the SPy landing page.

## Build and preview

Requires [uv](https://docs.astral.sh/uv/).

```sh
uv run build.py                 # writes public/
uv run python -m http.server -d public
```

`uv run build.py --inline-css` embeds `style.css` in every page instead of
linking it.

## Writing pages

A page is a Markdown file starting with:

```yaml
---
title: "Page title"
description: Optional, used for the meta description.
---
```

Besides standard Markdown, these `:::` blocks are available (use more colons
on the outer block when nesting):

| Block                | Use                                        |
| -------------------- | ------------------------------------------ |
| `hero`               | centered banner at the top                 |
| `buttons`            | row of links marked `{.btn}` or `{.btn .primary}` |
| `grid` / `card`      | responsive grid of cards                   |
| `split` / `col`      | two columns                                |
| `doc-links`          | list of `[Title](url)\` + description      |
| `status`             | highlighted note                           |

Attributes work on links, `[text](url){.btn}`, and on blocks, with a
`{.lead}` line right before the paragraph. To add a new block type, add its
name to `CONTAINERS` in `build.py` and style it in `static/style.css`.

## Deployment

`.github/workflows/pages.yml` builds the site with uv on every push and pull
request, and deploys it to GitHub Pages from `main`.

This repository only deploys the landing page. The other parts of
spylang.github.io are separate project sites, each deployed from its own
repository:

- `/docs/` from `spylang/docs`
- `/spy/` (the playground) from `spylang/spy`

So do not create `docs/` or `spy/` directories in `content/` or `static/`.
