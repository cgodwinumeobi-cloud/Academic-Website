# Homepage updates

- The homepage now includes a navy welcome banner with live visitor-local date/time, About Me portrait and summary, a 2-column highlights grid, and collaboration links.
- **Important:** The original current working `index.qmd` was not provided; this homepage is reconstructed from the agreed layout, so back up your existing `index.qmd` and compare before replacing.
- The package does NOT contain your real photographs. Preserve your existing `images/` folder, especially `images/profile.jpg`.
- Featured items are chosen randomly from **published** blog posts and podcast episodes. The two bundled sample research posts are marked `published: false` and do not appear as genuine publications.
- To publish an item, set `published: true` in its YAML header, include title, date, and description; place it under `blog/posts/<slug>/index.qmd`, `blogs/faith-lifestyle/posts/<slug>/index.qmd`, `blogs/leadership/posts/<slug>/index.qmd`, or `podcast/episodes/<slug>/index.qmd`.
- Run `python update-homepage-feed.py` from the project folder before `quarto render` or `quarto preview`. The script refreshes `homepage-highlights.js`; browser JavaScript randomly selects up to 4 entries each page load.
- Avoid deleting your existing posts or images when copying this package.
