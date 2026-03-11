"""
Manticore Sphinx Theme
~~~~~~~~~~~~~~~~~~

A clean, corporate documentation theme for Sphinx built on Bulma/SASS.
No NPM or Node.js required.
"""

from pathlib import Path

__version__ = "1.0.0"


def get_html_theme_path() -> str:
    """Return the directory containing this theme."""
    return str(Path(__file__).resolve().parent)


def setup(app):
    """Register the theme with Sphinx."""
    app.add_html_theme("manticore_sphinx_theme", get_html_theme_path())

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
