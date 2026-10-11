# Godwin C. Umeobi — Quarto Academic Website Starter

## Requirements
- Quarto CLI: https://quarto.org/docs/get-started/
- Git: https://git-scm.com/
- VS Code recommended

## Preview
Run `quarto preview` from this directory.

## Build
Run `quarto render` (creates `docs/`).

## Publish
1. Create a public GitHub repository named `YOUR-USERNAME.github.io`.
2. Replace `YOUR-USERNAME` in `_quarto.yml` and the placeholder email throughout.
3. Run `quarto render`.
4. Run `git init`, `git add .`, `git commit -m "Launch academic website"`.
5. Set the GitHub remote and push to `main`.
6. In GitHub Settings > Pages, deploy from `main` and `/docs`.

## Customize before publishing
- Replace placeholder email and site URL.
- Review all biography, research, and teaching claims.
- Replace both illustrative blog posts with your own writing.
- Add only authorized research findings, slides, and images.
- Add your own photograph under `images/` and reference it in a page.
- Add verified publications and conference details.

## Content
- `index.qmd`: homepage
- `research.qmd`: portfolio
- `blog/index.qmd`: searchable post listing
- `blog/posts/*/index.qmd`: posts
- `styles.css`: design
- `_quarto.yml`: navigation, theme, and site settings
