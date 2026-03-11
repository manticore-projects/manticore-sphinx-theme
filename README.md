# Manticore Sphinx Theme

A clean, elegant documentation theme for **Sphinx 7+** built on
**Bulma CSS / SASS** — with **zero NPM or Node.js dependencies**.

Designed for corporate software documentation, it provides an RTD-style
layout with a fixed sidebar, on-page table of contents, breadcrumbs,
prev/next navigation, and a fully responsive mobile experience.

---

## Features

- **Bulma-based** — uses Bulma's SASS architecture for consistent, modern styling
- **No NPM required** — compiles with Python `libsass` or standalone `dart-sass`
- **RTD-style layout** — fixed sidebar, scrollable content, right-rail TOC
- **Corporate design** — professional colour palette, clean typography (Source Sans 3 + JetBrains Mono)
- **Fully responsive** — mobile sidebar, touch-friendly, print stylesheet
- **Customisable** — override colours and fonts via `html_theme_options` or SASS variables
- **Accessible** — ARIA landmarks, keyboard navigation, skip links
- **Lightweight JS** — vanilla JavaScript for sidebar toggle, scroll-spy, and keyboard shortcuts
- **Sphinx 7+ / 9.x compatible** — uses the standard theme API

## Quick Start

### Install

```bash
pip install -e .
```

### Use in your Sphinx project

In `conf.py`:

```python
html_theme = "manticore_sphinx_theme"

html_theme_options = {
    "logo": "logo.svg",                  # optional
    "logo_alt": "My Project",
    "color_primary": "#1e3a5f",
    "color_accent": "#0077b6",
    "repo_url": "https://github.com/myorg/myproject",
    "repo_name": "GitHub",
}
```

### Build docs

```bash
make docs          # compiles CSS then builds HTML (requires sphinx)
make docs-live     # live-reload with sphinx-autobuild
```

## Development

### Full dev setup

```bash
make dev           # installs deps, compiles CSS, installs theme
```

### CSS compilation

The default build is **standalone** — no Bulma download required.
All SCSS uses modern `@use` / `@forward` syntax (Dart Sass 2+/3+ compatible).

```bash
make css           # standalone build (no Bulma fetch needed)
make css-min       # minified variant
make css-watch     # watch mode (dart-sass only)
make css-bulma     # optional: compile WITH Bulma utilities layer
```

The `css-bulma` target downloads Bulma 0.9.4 SASS sources and layers them
underneath the theme.  Since Bulma 0.9.x uses `@import` internally, the
Makefile passes `--silence-deprecation=import` to dart-sass automatically.

### Project structure

```
manticore-sphinx-theme/
├── Makefile                    # Build system
├── pyproject.toml              # Package metadata
├── manticore_sphinx_theme/
│   ├── __init__.py             # Sphinx theme registration
│   ├── theme.conf              # Theme configuration
│   ├── layout.html             # Main Jinja2 template
│   └── static/
│       ├── sass/               # SCSS source files
│       │   ├── theme.scss              # Main entry (standalone)
│       │   ├── theme-with-bulma.scss   # Optional Bulma integration
│       │   ├── _variables.scss         # Design tokens
│       │   ├── _base.scss              # Reset & typography
│       │   ├── _layout.scss            # Grid scaffolding
│       │   ├── _sidebar.scss           # Left navigation
│       │   ├── _toc.scss               # On-page TOC
│       │   ├── _code.scss              # Code blocks
│       │   ├── _admonitions.scss       # Notes, warnings, tips
│       │   ├── _content.scss           # Sphinx domains & API docs
│       │   ├── _footer.scss            # Footer & pagination
│       │   └── _responsive.scss        # Breakpoints & print
│       ├── css/
│       │   └── theme.css               # Pre-compiled CSS (shipped)
│       └── js/
│           └── theme.js                # Vanilla JS (sidebar, scroll-spy)
└── docs/                       # Sample documentation
    ├── conf.py
    ├── index.rst
    └── ...
```

## Customisation

### Via `html_theme_options`

| Option | Default | Description |
|---|---|---|
| `color_primary` | `#1e3a5f` | Primary brand colour |
| `color_accent` | `#0077b6` | Accent / link colour |
| `color_sidebar_bg` | `#f5f7fa` | Sidebar background |
| `navigation_depth` | `4` | Sidebar tree depth |
| `show_breadcrumbs` | `True` | Breadcrumb trail |
| `content_max_width` | `52rem` | Content column max width |

### Via SASS

For deeper changes, override `_variables.scss` and recompile:

```bash
make css           # recompile after editing SASS
```

## Requirements

- Python 3.9+
- Sphinx 7.0+ (tested through 9.2)
- For SASS compilation: `dart-sass` 2.x+ (recommended) **or** `libsass` (Python)
- All SCSS uses modern `@use` / `@forward` — fully Dart Sass 3.x compatible
- No NPM, Node.js, or webpack required

## License

MIT
