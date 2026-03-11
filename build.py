#!/usr/bin/env python3
"""
Manticore Sphinx Theme — Build Script
==================================

Cross-platform replacement for the Makefile.  Requires only Python 3.9+.

Usage:
    python build.py <command> [command ...]

Commands:
    help          Show this help
    info          Show detected tool paths
    env           Create local .venv with Sphinx
    deps          Install build dependencies (pipx or pip)
    css           Compile SASS → CSS (standalone)
    css-min       Compile minified CSS
    css-bulma     Compile with Bulma utilities
    css-watch     Watch SASS and recompile
    docs          Build HTML documentation
    docs-live     Live-reload docs server
    install       Install theme into current environment
    dev           Full dev setup: deps + css + install
    dist          Build sdist + wheel
    publish       Upload to PyPI
    lint          Lint Python sources
    check         Full pre-commit check (lint + css + linkcheck)
    clean         Remove build artifacts
    clean-vendor  Remove downloaded Bulma sources
    clean-env     Remove local .venv
    all           Everything: deps + css + css-min + docs
    fetch-bulma   Download Bulma SASS sources
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

# ─── Project layout ─────────────────────────────────────────

ROOT         = Path(__file__).resolve().parent
THEME_DIR    = ROOT / "manticore_sphinx_theme"
SASS_DIR     = THEME_DIR / "static" / "sass"
CSS_DIR      = THEME_DIR / "static" / "css"
DOCS_DIR     = ROOT / "docs"
BUILD_DIR    = ROOT / "_build"
VENDOR_DIR   = ROOT / "vendor"

BULMA_VER    = "0.9.4"
BULMA_URL    = f"https://github.com/jgthms/bulma/releases/download/{BULMA_VER}/bulma-{BULMA_VER}.zip"

SASS_ENTRY   = SASS_DIR / "theme.scss"
SASS_BULMA   = SASS_DIR / "theme-with-bulma.scss"
CSS_OUT      = CSS_DIR / "theme.css"
CSS_OUT_MIN  = CSS_DIR / "theme.min.css"

IS_WIN       = platform.system() == "Windows"
VENV_DIR     = ROOT / ".venv"


# ─── Tool detection ─────────────────────────────────────────

def _which(name: str) -> str | None:
    """Find an executable on PATH (or in .venv/bin)."""
    return shutil.which(name)


def _venv_bin(name: str) -> Path | None:
    """Look for a binary inside the local .venv."""
    d = "Scripts" if IS_WIN else "bin"
    p = VENV_DIR / d / name
    if p.exists():
        return p
    # Try with .exe on Windows
    if IS_WIN:
        p = p.with_suffix(".exe")
        if p.exists():
            return p
    return None


def detect_python() -> str:
    venv = _venv_bin("python3") or _venv_bin("python")
    if venv:
        return str(venv)
    return sys.executable


def detect_sphinx_build() -> list[str]:
    venv = _venv_bin("sphinx-build")
    if venv:
        return [str(venv)]
    s = _which("sphinx-build")
    if s:
        return [s]
    return [detect_python(), "-m", "sphinx"]


def detect_sphinx_autobuild() -> list[str]:
    venv = _venv_bin("sphinx-autobuild")
    if venv:
        return [str(venv)]
    s = _which("sphinx-autobuild")
    if s:
        return [s]
    return [detect_python(), "-m", "sphinx_autobuild"]


def detect_dartsass() -> str | None:
    return _which("sass")


def detect_pipx() -> str | None:
    return _which("pipx")


def pip_cmd() -> list[str]:
    """Return the best pip invocation available."""
    venv = _venv_bin("pip") or _venv_bin("pip3")
    if venv:
        return [str(venv), "install"]
    return [detect_python(), "-m", "pip", "install", "--break-system-packages"]


# ─── Helpers ─────────────────────────────────────────────────

GREEN  = "\033[36m"
BOLD   = "\033[1m"
RESET  = "\033[0m"
CHECK  = "✓"
CROSS  = "✗"
BULLET = "●"


def run(cmd: list[str] | str, cwd: Path | None = None, check: bool = True) -> int:
    """Run a command, streaming output."""
    if isinstance(cmd, str):
        cmd = cmd.split()
    result = subprocess.run(cmd, cwd=cwd)
    if check and result.returncode != 0:
        sys.exit(result.returncode)
    return result.returncode


def info_line(label: str, value: str):
    print(f"  {label:24s}{value}")


# ─── Bulma detection ────────────────────────────────────────

def find_bulma_sass() -> Path | None:
    candidates = [
        VENDOR_DIR / f"bulma-{BULMA_VER}" / "sass",
        VENDOR_DIR / f"bulma-{BULMA_VER}" / "bulma" / "sass",
        VENDOR_DIR / "bulma" / "sass",
        VENDOR_DIR / "sass",
    ]
    for d in candidates:
        if d.is_dir():
            return d
    return None


# ═════════════════════════════════════════════════════════════
#  COMMANDS
# ═════════════════════════════════════════════════════════════

def cmd_help():
    """Show this help."""
    print(f"\n{BOLD}Manticore Sphinx Theme — Build Script{RESET}\n")
    print(f"Usage:  python build.py <command> [command ...]\n")
    print(f"Commands:")
    for name, fn in COMMANDS.items():
        doc = (fn.__doc__ or "").strip().split("\n")[0]
        print(f"  {GREEN}{name:16s}{RESET} {doc}")
    print()


def cmd_info():
    """Show detected tool paths."""
    print("─── Tool Detection ───────────────────────────────")
    info_line("Python:", detect_python())
    info_line("Sphinx build:", " ".join(detect_sphinx_build()))
    info_line("Sphinx autobuild:", " ".join(detect_sphinx_autobuild()))

    pipx = detect_pipx()
    if pipx:
        info_line("Installer (CLI):", f"pipx ({pipx})")
    elif _venv_bin("pip"):
        info_line("Installer (CLI):", "pip (.venv)")
    else:
        info_line("Installer (CLI):", "pip3 (system)")

    venv_pip = _venv_bin("pip")
    info_line("Installer (lib):", "pip (.venv)" if venv_pip else "pip3 (system)")

    sass = detect_dartsass()
    info_line("Sass compiler:", f"dart-sass ({sass})" if sass else "libsass (Python)")
    info_line("Local .venv:", "yes" if VENV_DIR.is_dir() else "no")
    print("──────────────────────────────────────────────────")


def cmd_env():
    """Create local .venv and install Sphinx into it."""
    if not VENV_DIR.is_dir():
        print(f"{BULLET} Creating .venv…")
        run([sys.executable, "-m", "venv", str(VENV_DIR)])

    venv_pip = str(VENV_DIR / ("Scripts" if IS_WIN else "bin") / "pip")
    run([venv_pip, "install", "--upgrade", "pip"])
    run([venv_pip, "install", "sphinx>=7.0", "sphinx-autobuild"])
    print(f"{CHECK}  .venv ready.  Re-run build.py to pick it up automatically.")
    print("   (No need to activate — build.py detects .venv/ automatically)")


def cmd_deps():
    """Install build dependencies (pipx for CLI, pip for libs)."""
    pipx = detect_pipx()
    if pipx:
        print(f"{BULLET} Installing CLI tools via pipx…")
        for pkg in ["sphinx", "sphinx-autobuild", "build", "twine"]:
            run([pipx, "install", pkg], check=False)
        print(f"{BULLET} Installing library dependencies…")
        run(pip_cmd() + ["libsass"], check=False)
    else:
        print(f"{BULLET} Installing all dependencies via pip…")
        run(pip_cmd() + ["libsass", "sphinx>=7.0", "sphinx-autobuild", "build", "twine"])
    print(f"{CHECK}  Dependencies installed")


def cmd_fetch_bulma():
    """Download Bulma SASS sources (no NPM required)."""
    VENDOR_DIR.mkdir(exist_ok=True)
    if find_bulma_sass():
        print(f"{CHECK}  Bulma {BULMA_VER} already present at {find_bulma_sass()}")
        return

    print(f"⬇  Downloading Bulma {BULMA_VER}…")
    zip_path = VENDOR_DIR / "bulma.zip"
    urlretrieve(BULMA_URL, zip_path)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(VENDOR_DIR)
    zip_path.unlink()

    found = find_bulma_sass()
    if not found:
        print(f"{CROSS}  Could not locate sass/ in extracted archive.")
        for p in sorted(VENDOR_DIR.rglob("*"))[:20]:
            print(f"   {p.relative_to(ROOT)}")
        sys.exit(1)
    print(f"{CHECK}  Bulma {BULMA_VER} SASS found at {found}")


def cmd_css():
    """Compile SASS → CSS (standalone, no Bulma required)."""
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    sass = detect_dartsass()
    if sass:
        print(f"{BULLET} Compiling with dart-sass (standalone)…")
        run([sass,
             f"--load-path={SASS_DIR}",
             "--style=expanded", "--no-source-map",
             f"{SASS_ENTRY}:{CSS_OUT}"])
    else:
        print(f"{BULLET} Compiling with libsass (standalone)…")
        run([detect_python(), "-c",
             f"import sass; "
             f"css = sass.compile(filename='{SASS_ENTRY}', "
             f"include_paths=['{SASS_DIR}'], output_style='expanded'); "
             f"open('{CSS_OUT}', 'w').write(css)"])
    print(f"{CHECK}  {CSS_OUT.relative_to(ROOT)} written")


def cmd_css_min():
    """Compile SASS → minified CSS."""
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    sass = detect_dartsass()
    if sass:
        run([sass,
             f"--load-path={SASS_DIR}",
             "--style=compressed", "--no-source-map",
             f"{SASS_ENTRY}:{CSS_OUT_MIN}"])
    else:
        run([detect_python(), "-c",
             f"import sass; "
             f"css = sass.compile(filename='{SASS_ENTRY}', "
             f"include_paths=['{SASS_DIR}'], output_style='compressed'); "
             f"open('{CSS_OUT_MIN}', 'w').write(css)"])
    print(f"{CHECK}  {CSS_OUT_MIN.relative_to(ROOT)} written")


def cmd_css_bulma():
    """Compile SASS → CSS with Bulma utilities."""
    cmd_fetch_bulma()
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    bulma = find_bulma_sass()
    if not bulma:
        print(f"{CROSS}  Bulma SASS not found. Run: python build.py fetch-bulma")
        sys.exit(1)

    sass = detect_dartsass()
    if sass:
        print(f"{BULLET} Compiling with dart-sass + Bulma ({bulma})…")
        run([sass,
             f"--load-path={bulma}",
             f"--load-path={SASS_DIR}",
             "--silence-deprecation=import",
             "--silence-deprecation=global-builtin",
             "--silence-deprecation=color-functions",
             "--quiet-deps",
             "--style=expanded", "--no-source-map",
             f"{SASS_BULMA}:{CSS_OUT}"])
    else:
        print(f"{BULLET} Compiling with libsass + Bulma ({bulma})…")
        run([detect_python(), "-c",
             f"import sass; "
             f"css = sass.compile(filename='{SASS_BULMA}', "
             f"include_paths=['{bulma}', '{SASS_DIR}'], output_style='expanded'); "
             f"open('{CSS_OUT}', 'w').write(css)"])
    print(f"{CHECK}  {CSS_OUT.relative_to(ROOT)} written (with Bulma)")


def cmd_css_watch():
    """Watch SASS and recompile on change."""
    sass = detect_dartsass()
    if sass:
        run([sass, "--watch",
             f"--load-path={SASS_DIR}",
             f"{SASS_ENTRY}:{CSS_OUT}"])
    else:
        print("dart-sass not found; falling back to poll-based rebuild…")
        print("(Install dart-sass for proper --watch support.  Ctrl+C to stop.)")
        try:
            while True:
                cmd_css()
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nStopped.")


def cmd_docs():
    """Build HTML documentation."""
    cmd_css()
    sphinx = detect_sphinx_build()
    run(sphinx + ["-b", "html", ".", str(BUILD_DIR / "html")], cwd=DOCS_DIR)


def cmd_docs_prod():
    """Build + minify + gzip (production)."""
    cmd_css()
    cmd_css_min()
    sphinx = detect_sphinx_build()
    run(sphinx + ["-b", "html", ".", str(BUILD_DIR / "html")], cwd=DOCS_DIR)
    run([detect_python(), str(ROOT / "optimize.py"), str(BUILD_DIR / "html")])


def cmd_docs_live():
    """Live-reload docs server."""
    cmd_css()
    autobuild = detect_sphinx_autobuild()
    run(autobuild + [".", str(BUILD_DIR / "html"),
                     "--port", "8080", "--open-browser"], cwd=DOCS_DIR)


def cmd_install():
    """Install theme into current environment."""
    cmd_css()
    run(pip_cmd() + ["-e", "."], cwd=ROOT)


def cmd_dev():
    """Full dev setup: deps + css + install."""
    cmd_deps()
    cmd_css()
    cmd_install()
    print(f"{CHECK}  Dev environment ready.  Run: python build.py docs")


def cmd_dist():
    """Build sdist + wheel."""
    cmd_css()
    cmd_css_min()
    run([detect_python(), "-m", "build"], cwd=ROOT)
    print(f"{CHECK}  Packages in dist/")


def cmd_publish():
    """Upload to PyPI."""
    cmd_dist()
    run([detect_python(), "-m", "twine", "upload", "dist/*"], cwd=ROOT)


def cmd_lint():
    """Lint Python sources."""
    run([detect_python(), "-m", "py_compile", str(THEME_DIR / "__init__.py")])
    print(f"{CHECK}  Python sources OK")


def cmd_check():
    """Full pre-commit check (lint + css + linkcheck)."""
    cmd_lint()
    cmd_css()
    sphinx = detect_sphinx_build()
    run(sphinx + ["-b", "linkcheck", ".", str(BUILD_DIR / "linkcheck")], cwd=DOCS_DIR)
    print(f"{CHECK}  All checks passed")


def cmd_clean():
    """Remove build artifacts."""
    for d in [BUILD_DIR, ROOT / "dist"]:
        if d.is_dir():
            shutil.rmtree(d)
    for pattern in ["*.egg-info", ".eggs"]:
        for p in ROOT.glob(pattern):
            shutil.rmtree(p)
    for f in [CSS_OUT, CSS_OUT_MIN]:
        f.unlink(missing_ok=True)
    for d in ROOT.rglob("__pycache__"):
        shutil.rmtree(d, ignore_errors=True)
    print(f"{CHECK}  Cleaned")


def cmd_clean_vendor():
    """Remove downloaded Bulma sources."""
    if VENDOR_DIR.is_dir():
        shutil.rmtree(VENDOR_DIR)
    print(f"{CHECK}  Vendor directory removed")


def cmd_clean_env():
    """Remove local .venv."""
    if VENV_DIR.is_dir():
        shutil.rmtree(VENV_DIR)
    print(f"{CHECK}  .venv removed")


def cmd_all():
    """Everything: deps + css + css-min + docs."""
    cmd_deps()
    cmd_css()
    cmd_css_min()
    cmd_docs()


# ─── Command registry ───────────────────────────────────────

COMMANDS: dict[str, callable] = {
    "help":         cmd_help,
    "info":         cmd_info,
    "env":          cmd_env,
    "deps":         cmd_deps,
    "fetch-bulma":  cmd_fetch_bulma,
    "css":          cmd_css,
    "css-min":      cmd_css_min,
    "css-bulma":    cmd_css_bulma,
    "css-watch":    cmd_css_watch,
    "docs":         cmd_docs,
    "docs-prod":    cmd_docs_prod,
    "docs-live":    cmd_docs_live,
    "install":      cmd_install,
    "dev":          cmd_dev,
    "dist":         cmd_dist,
    "publish":      cmd_publish,
    "lint":         cmd_lint,
    "check":        cmd_check,
    "clean":        cmd_clean,
    "clean-vendor": cmd_clean_vendor,
    "clean-env":    cmd_clean_env,
    "all":          cmd_all,
}


# ─── Main ────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args:
        cmd_help()
        sys.exit(0)

    for arg in args:
        if arg in COMMANDS:
            COMMANDS[arg]()
        else:
            print(f"{CROSS}  Unknown command: {arg}")
            print(f"   Run 'python build.py help' for available commands.")
            sys.exit(1)


if __name__ == "__main__":
    main()
