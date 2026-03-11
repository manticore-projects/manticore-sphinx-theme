# ─────────────────────────────────────────────────────────────
#  Sphinx configuration — Manticore Sphinx Theme feature showcase
# ─────────────────────────────────────────────────────────────

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Acme Platform"
copyright = "2026, Acme Corp"
author = "Acme Engineering"
version = "3.2"
release = "3.2.1"

# ── Extensions ───────────────────────────────────────────────
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.mathjax",
]

todo_include_todos = True

# ── Theme ────────────────────────────────────────────────────
html_theme = "manticore_sphinx_theme"
html_theme_path = [os.path.abspath("..")]

html_theme_options = {
    "logo": "manticore_logo.png",
    "logo_alt": "Manticore Projects",
    "favicon": "favicon.ico",
    "color_primary": "#030146",
    "color_accent": "#ff420e",
    "color_sidebar_bg": "#f5f6fa",
    "color_sidebar_text": "#2d2d48",
    "navigation_depth": 4,
    "show_breadcrumbs": True,
    "footer_text": "Built with care by Manticore Projects.",
    "repo_url": "https://github.com/manticore-projects",
    "repo_name": "GitHub",
    "landing_page": "index",
}

# ── General ──────────────────────────────────────────────────
templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_static_path = ["_static"]
html_title = "Acme Platform Documentation"

# Turn off the basic theme's "Created using Sphinx" footer
html_show_sphinx = False

# ── Landing page cards ───────────────────────────────────────
# Each card: title (required), url (required), description (optional), icon (optional SVG path)
html_context = {
    "landing_page": {
        "menu": [
            {
                "title": "Quick Start",
                "url": "getting-started",
                "description": "Install, configure, and run your first query in 5 minutes.",
                "icon": "M13 2L3 14h9l-1 8 10-12h-9l1-8z",
            },
            {
                "title": "API Reference",
                "url": "api-reference",
                "description": "Classes, methods, exceptions, and type aliases.",
                "icon": "M16 18l6-6-6-6M8 6l-6 6 6 6",
            },
            {
                "title": "Code Blocks",
                "url": "code-blocks",
                "description": "Syntax highlighting, line numbers, and captions.",
                "icon": "M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2zM22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z",
            },
            {
                "title": "Tables & Figures",
                "url": "tables-figures",
                "description": "Grid tables, list tables, math, and figures.",
            },
            {
                "title": "Admonitions",
                "url": "admonitions",
                "description": "Notes, warnings, tips, and callout boxes.",
            },
            {
                "title": "Special Markup",
                "url": "special-markup",
                "description": "Epigraphs, containers, production lists, and more.",
            },
        ]
    }
}

# ── Intersphinx ──────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# ── Numfig (numbered figures/tables/code-blocks) ────────────
numfig = True
