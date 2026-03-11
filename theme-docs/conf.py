import os, sys
sys.path.insert(0, os.path.abspath(".."))

project = "Manticore Sphinx Theme"
copyright = "2026, Manticore Projects"
author = "Manticore Projects"
version = "1.0"
release = "1.0.0"

extensions = ["sphinx.ext.todo"]
todo_include_todos = True

html_theme = "manticore_sphinx_theme"
html_theme_path = [os.path.abspath("..")]

html_theme_options = {
    "logo": "manticore_logo.png",
    "logo_alt": "Manticore Sphinx Theme",
    "favicon": "favicon.ico",
    "color_primary": "#030146",
    "color_accent": "#ff420e",
    "navigation_depth": 3,
    "show_breadcrumbs": True,
    "footer_text": "Manticore Sphinx Theme — Manticore Projects",
    "repo_url": "https://github.com/manticore-projects/manticore-sphinx-theme",
    "repo_name": "GitHub",
}

templates_path = []
exclude_patterns = ["_build"]
html_static_path = ["_static"]
html_show_sphinx = False
