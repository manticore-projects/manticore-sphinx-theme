#!/usr/bin/env python3
"""
optimize.py — Post-build HTML/CSS/JS optimization
===================================================

Runs after `sphinx-build` to minify and compress the output.

Usage:
    python optimize.py [build_dir]

Default build_dir: _build/html

What it does:
  1. Minifies HTML files (removes comments, collapses whitespace)
  2. Minifies CSS files (if cssmin/rcssmin available, else basic)
  3. Minifies JS files (basic whitespace compression)
  4. Creates .gz pre-compressed copies for nginx gzip_static
  5. Reports savings

Requires: Python 3.9+ (no external packages needed, but rcssmin
and htmlmin improve results if available).
"""

from __future__ import annotations

import gzip
import os
import re
import sys
from pathlib import Path


# ─── Configuration ───────────────────────────────────────────

EXTENSIONS_MINIFY = {".html", ".css", ".js"}
EXTENSIONS_GZIP   = {".html", ".css", ".js", ".svg", ".json", ".xml", ".txt"}
GZIP_LEVEL        = 9
MIN_GZIP_SIZE     = 256    # don't gzip files smaller than this


# ─── Minifiers ───────────────────────────────────────────────

def minify_html(content: str) -> str:
    """Minify HTML: remove comments, collapse whitespace outside <pre>."""
    # Try htmlmin if available
    try:
        import htmlmin
        return htmlmin.minify(
            content,
            remove_comments=True,
            remove_empty_space=True,
            reduce_boolean_attributes=True,
            remove_optional_attribute_quotes=False,
        )
    except ImportError:
        pass

    # Fallback: basic minification
    # Preserve <pre>, <code>, <script>, <style> contents
    protected = {}
    counter = [0]

    def protect(m):
        key = f"\x00PROTECTED{counter[0]}\x00"
        counter[0] += 1
        protected[key] = m.group(0)
        return key

    # Protect pre/code/script/style blocks
    result = re.sub(
        r"<(pre|code|script|style|textarea)\b[^>]*>.*?</\1>",
        protect, content, flags=re.DOTALL | re.IGNORECASE
    )

    # Remove HTML comments (but keep IE conditionals)
    result = re.sub(r"<!--(?!\[if).*?-->", "", result, flags=re.DOTALL)

    # Collapse whitespace
    result = re.sub(r"\s+", " ", result)

    # Remove space around tags
    result = re.sub(r">\s+<", "><", result)

    # Restore protected blocks
    for key, val in protected.items():
        result = result.replace(key, val)

    return result.strip()


def minify_css(content: str) -> str:
    """Minify CSS: remove comments, collapse whitespace."""
    try:
        import rcssmin
        return rcssmin.cssmin(content)
    except ImportError:
        pass

    # Fallback: basic CSS minification
    # Remove comments
    result = re.sub(r"/\*.*?\*/", "", content, flags=re.DOTALL)
    # Remove whitespace around special chars
    result = re.sub(r"\s*([{}:;,>~+])\s*", r"\1", result)
    # Collapse whitespace
    result = re.sub(r"\s+", " ", result)
    # Remove leading/trailing space in blocks
    result = re.sub(r";\s*}", "}", result)
    # Remove last semicolon before }
    result = result.strip()
    return result


def minify_js(content: str) -> str:
    """Basic JS minification: remove single-line comments, collapse whitespace."""
    # Remove single-line comments (but not URLs with //)
    lines = []
    for line in content.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("//"):
            continue
        lines.append(line)
    result = "\n".join(lines)

    # Remove multi-line comments
    result = re.sub(r"/\*.*?\*/", "", result, flags=re.DOTALL)

    # Collapse multiple blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)

    return result.strip() + "\n"


MINIFIERS = {
    ".html": minify_html,
    ".css":  minify_css,
    ".js":   minify_js,
}


# ─── Gzip pre-compression ───────────────────────────────────

def gzip_file(path: Path) -> int:
    """Create a .gz copy. Returns bytes saved (0 if skipped)."""
    data = path.read_bytes()
    if len(data) < MIN_GZIP_SIZE:
        return 0

    gz_path = path.with_suffix(path.suffix + ".gz")
    with gzip.open(gz_path, "wb", compresslevel=GZIP_LEVEL) as f:
        f.write(data)

    return len(data) - gz_path.stat().st_size


# ─── Main ────────────────────────────────────────────────────

def optimize(build_dir: Path):
    if not build_dir.is_dir():
        print(f"✗  Build directory not found: {build_dir}")
        print(f"   Run 'make docs' or 'python build.py docs' first.")
        sys.exit(1)

    total_original = 0
    total_minified = 0
    total_gzipped  = 0
    files_minified = 0
    files_gzipped  = 0

    print(f"● Optimizing {build_dir}/…\n")

    for path in sorted(build_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix == ".gz":
            continue

        ext = path.suffix.lower()

        # Minify
        if ext in EXTENSIONS_MINIFY:
            original = path.read_text(encoding="utf-8", errors="ignore")
            original_size = len(original.encode("utf-8"))

            minifier = MINIFIERS.get(ext)
            if minifier:
                try:
                    minified = minifier(original)
                    minified_size = len(minified.encode("utf-8"))
                    if minified_size < original_size:
                        path.write_text(minified, encoding="utf-8")
                        total_original += original_size
                        total_minified += minified_size
                        files_minified += 1
                except Exception as e:
                    print(f"  ⚠  Minify failed for {path.name}: {e}")

        # Gzip
        if ext in EXTENSIONS_GZIP:
            saved = gzip_file(path)
            if saved > 0:
                total_gzipped += saved
                files_gzipped += 1

    # Report
    print(f"  Minified:   {files_minified} files")
    if total_original > 0:
        pct = (1 - total_minified / total_original) * 100
        print(f"              {total_original:,} → {total_minified:,} bytes ({pct:.1f}% reduction)")
    print(f"  Gzipped:    {files_gzipped} files ({total_gzipped:,} bytes saved)")
    total_saved = (total_original - total_minified) + total_gzipped
    print(f"  Total saved: {total_saved:,} bytes")
    print(f"\n✓  Optimization complete")


if __name__ == "__main__":
    build_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_build/html")
    optimize(build_dir)
