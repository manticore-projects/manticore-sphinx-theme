# ─────────────────────────────────────────────────────────────
#  Manticore Sphinx Theme — Makefile
#  Build system for SASS compilation, packaging, and docs.
#  No NPM / Node.js required.  Uses dart-sass or Python libsass.
#
#  Tool resolution order:
#    Python     :  .venv/bin/python  →  python3
#    Sphinx     :  .venv/bin/sphinx-build  →  sphinx-build on $PATH
#    Installer  :  pipx (if found)  →  pip with --break-system-packages
#    Sass       :  dart-sass (if found)  →  Python libsass
# ─────────────────────────────────────────────────────────────

SHELL        := /bin/bash
THEME_DIR    := manticore_sphinx_theme
SASS_DIR     := $(THEME_DIR)/static/sass
CSS_DIR      := $(THEME_DIR)/static/css
JS_DIR       := $(THEME_DIR)/static/js
DOCS_DIR     := docs
BUILD_DIR    := _build

BULMA_VER    := 0.9.4
BULMA_URL    := https://github.com/jgthms/bulma/releases/download/$(BULMA_VER)/bulma-$(BULMA_VER).zip

SASS_ENTRY   := $(SASS_DIR)/theme.scss
SASS_BULMA   := $(SASS_DIR)/theme-with-bulma.scss

CSS_OUT      := $(CSS_DIR)/theme.css
CSS_OUT_MIN  := $(CSS_DIR)/theme.min.css

# ─── Python — prefer local .venv, fall back to system ───────
VENV_PYTHON  := $(wildcard .venv/bin/python3)
ifeq ($(VENV_PYTHON),)
  VENV_PYTHON := $(wildcard .venv/bin/python)
endif

ifdef VENV_PYTHON
  PYTHON     ?= $(VENV_PYTHON)
else
  PYTHON     ?= python3
endif

# ─── Sphinx — prefer local .venv, fall back to system ───────
VENV_SPHINX  := $(wildcard .venv/bin/sphinx-build)

ifdef VENV_SPHINX
  SPHINX_BUILD     ?= $(VENV_SPHINX)
else
  SPHINX_BUILD     ?= $(shell command -v sphinx-build 2>/dev/null)
endif

# If still not found, fall back to python -m sphinx
ifeq ($(SPHINX_BUILD),)
  SPHINX_BUILD     := $(PYTHON) -m sphinx
endif

VENV_AUTOBUILD := $(wildcard .venv/bin/sphinx-autobuild)
ifdef VENV_AUTOBUILD
  SPHINX_AUTOBUILD ?= $(VENV_AUTOBUILD)
else
  SPHINX_AUTOBUILD ?= $(shell command -v sphinx-autobuild 2>/dev/null)
endif
ifeq ($(SPHINX_AUTOBUILD),)
  SPHINX_AUTOBUILD := $(PYTHON) -m sphinx_autobuild
endif

# ─── Package installer — prefer pipx, fall back to pip ──────
PIPX         := $(shell command -v pipx 2>/dev/null)
VENV_PIP     := $(wildcard .venv/bin/pip)

ifdef PIPX
  # pipx for CLI tools (sphinx, twine, build), pip for libraries
  PKG_INSTALL_CLI = pipx install
  PKG_INJECT     = pipx inject
  # For libraries that aren't CLI apps, use pip inside .venv or system
  ifdef VENV_PIP
    PKG_INSTALL_LIB = $(VENV_PIP) install
  else
    PKG_INSTALL_LIB = pip3 install --break-system-packages
  endif
else
  ifdef VENV_PIP
    PKG_INSTALL_CLI = $(VENV_PIP) install
    PKG_INSTALL_LIB = $(VENV_PIP) install
  else
    PKG_INSTALL_CLI = pip3 install --break-system-packages
    PKG_INSTALL_LIB = pip3 install --break-system-packages
  endif
endif

# ─── Sass — prefer dart-sass binary ─────────────────────────
DARTSASS     := $(shell command -v sass 2>/dev/null)

# ─── Bulma extracted directory detection ─────────────────────
define find_bulma_sass
$(shell \
  for d in vendor/bulma-$(BULMA_VER)/sass \
           vendor/bulma-$(BULMA_VER)/bulma/sass \
           vendor/bulma/sass \
           vendor/sass; do \
    [ -d "$$d" ] && echo "$$d" && break; \
  done)
endef

# ─── libsass (Python) fallback compiler ──────────────────────
define PYSASS_COMPILE
$(PYTHON) -c "\
import sass, sys; \
css = sass.compile( \
    filename='$(1)', \
    include_paths=[p for p in '$(2)'.split(':') if p], \
    output_style='$(3)' \
); \
open('$(4)', 'w').write(css)"
endef


# ─────────────────────────────────────────────────────────────
#  TARGETS
# ─────────────────────────────────────────────────────────────

.PHONY: help env deps fetch-bulma css css-bulma css-min css-watch \
        docs docs-live install dev clean dist \
        lint check all info

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

info:  ## Show detected tool paths
	@echo "─── Tool Detection ───────────────────────────────"
	@echo "  Python:           $(PYTHON)"
	@echo "  Sphinx build:     $(SPHINX_BUILD)"
	@echo "  Sphinx autobuild: $(SPHINX_AUTOBUILD)"
	@printf "  Installer (CLI):  "; \
	  if [ -n "$(PIPX)" ]; then echo "pipx ($(PIPX))"; \
	  elif [ -n "$(VENV_PIP)" ]; then echo "pip (.venv)"; \
	  else echo "pip3 (system)"; fi
	@printf "  Installer (lib):  "; \
	  if [ -n "$(VENV_PIP)" ]; then echo "pip (.venv)"; \
	  else echo "pip3 (system)"; fi
	@printf "  Sass compiler:    "; \
	  if [ -n "$(DARTSASS)" ]; then echo "dart-sass ($(DARTSASS))"; \
	  else echo "libsass (Python)"; fi
	@printf "  Local .venv:      "; \
	  if [ -d ".venv" ]; then echo "yes"; else echo "no"; fi
	@echo "──────────────────────────────────────────────────"


# ─── Virtual environment ────────────────────────────────────

env:  ## Create local .venv and install Sphinx into it
	@if [ ! -d ".venv" ]; then \
	    echo "● Creating .venv…"; \
	    $(PYTHON) -m venv .venv; \
	fi
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install sphinx>=7.0 sphinx-autobuild
	@echo "✓  .venv ready.  Re-run make to pick it up automatically."
	@echo "   (No need to activate — the Makefile detects .venv/bin/)"


# ─── Dependencies ───────────────────────────────────────────

deps:  ## Install build dependencies (uses pipx if available)
ifdef PIPX
	@echo "● Installing CLI tools via pipx…"
	-$(PKG_INSTALL_CLI) sphinx
	-$(PKG_INSTALL_CLI) sphinx-autobuild
	-$(PKG_INSTALL_CLI) build
	-$(PKG_INSTALL_CLI) twine
	@echo "● Installing library dependencies…"
	-$(PKG_INSTALL_LIB) libsass
else
	@echo "● Installing all dependencies via pip…"
	$(PKG_INSTALL_CLI) libsass sphinx>=7.0 sphinx-autobuild build twine
endif
	@echo "✓  Dependencies installed"


# ─── CSS Compilation (standalone — no Bulma needed) ─────────

fetch-bulma:  ## Download Bulma SASS sources (no NPM required)
	@mkdir -p vendor
	@if [ -z "$(call find_bulma_sass)" ]; then \
	    echo "⬇  Downloading Bulma $(BULMA_VER)…"; \
	    curl -sL $(BULMA_URL) -o vendor/bulma.zip; \
	    unzip -qo vendor/bulma.zip -d vendor/; \
	    rm -f vendor/bulma.zip; \
	    FOUND=$$(for d in vendor/bulma-$(BULMA_VER)/sass \
	                      vendor/bulma-$(BULMA_VER)/bulma/sass \
	                      vendor/bulma/sass \
	                      vendor/sass; do \
	        [ -d "$$d" ] && echo "$$d" && break; \
	    done); \
	    if [ -z "$$FOUND" ]; then \
	        echo "✗  Could not locate sass/ in extracted archive."; \
	        echo "   Contents of vendor/:"; \
	        find vendor -maxdepth 3 -type d | head -20; \
	        exit 1; \
	    fi; \
	    echo "✓  Bulma $(BULMA_VER) SASS found at $$FOUND"; \
	else \
	    echo "✓  Bulma $(BULMA_VER) already present at $(call find_bulma_sass)"; \
	fi

css:  ## Compile SASS → CSS (standalone, no Bulma required)
	@mkdir -p $(CSS_DIR)
ifdef DARTSASS
	@echo "● Compiling with dart-sass (standalone)…"
	$(DARTSASS) \
	    --load-path=$(SASS_DIR) \
	    --style=expanded --no-source-map \
	    $(SASS_ENTRY):$(CSS_OUT)
else
	@echo "● Compiling with libsass (standalone)…"
	$(call PYSASS_COMPILE,$(SASS_ENTRY),$(SASS_DIR),expanded,$(CSS_OUT))
endif
	@echo "✓  $(CSS_OUT) written"

css-min:  ## Compile SASS → minified CSS (standalone)
	@mkdir -p $(CSS_DIR)
ifdef DARTSASS
	$(DARTSASS) \
	    --load-path=$(SASS_DIR) \
	    --style=compressed --no-source-map \
	    $(SASS_ENTRY):$(CSS_OUT_MIN)
else
	$(call PYSASS_COMPILE,$(SASS_ENTRY),$(SASS_DIR),compressed,$(CSS_OUT_MIN))
endif
	@echo "✓  $(CSS_OUT_MIN) written"

css-bulma: fetch-bulma  ## Compile SASS → CSS with Bulma utilities
	@mkdir -p $(CSS_DIR)
	$(eval BULMA_SASS := $(call find_bulma_sass))
	@if [ -z "$(BULMA_SASS)" ]; then \
	    echo "✗  Bulma SASS directory not found. Run: make fetch-bulma"; \
	    exit 1; \
	fi
ifdef DARTSASS
	@echo "● Compiling with dart-sass + Bulma ($(BULMA_SASS))…"
	$(DARTSASS) \
	    --load-path=$(BULMA_SASS) \
	    --load-path=$(SASS_DIR) \
	    --silence-deprecation=import \
	    --silence-deprecation=global-builtin \
	    --silence-deprecation=color-functions \
	    --quiet-deps \
	    --style=expanded --no-source-map \
	    $(SASS_BULMA):$(CSS_OUT)
else
	@echo "● Compiling with libsass + Bulma ($(BULMA_SASS))…"
	$(call PYSASS_COMPILE,$(SASS_BULMA),$(BULMA_SASS):$(SASS_DIR),expanded,$(CSS_OUT))
endif
	@echo "✓  $(CSS_OUT) written (with Bulma)"

css-watch:  ## Watch SASS and recompile on change
ifdef DARTSASS
	$(DARTSASS) --watch \
	    --load-path=$(SASS_DIR) \
	    $(SASS_ENTRY):$(CSS_OUT)
else
	@echo "dart-sass not found; falling back to poll-based rebuild…"
	@echo "(Install dart-sass for proper --watch support)"
	@while true; do \
	    $(MAKE) css 2>/dev/null; \
	    sleep 2; \
	done
endif


# ─── Documentation ───────────────────────────────────────────

docs: css  ## Build HTML documentation
	cd $(DOCS_DIR) && $(SPHINX_BUILD) -b html . ../$(BUILD_DIR)/html

docs-prod: css css-min  ## Build + minify + gzip (production)
	cd $(DOCS_DIR) && $(SPHINX_BUILD) -b html . ../$(BUILD_DIR)/html
	$(PYTHON) optimize.py $(BUILD_DIR)/html

docs-live: css  ## Live-reload docs server
	cd $(DOCS_DIR) && $(SPHINX_AUTOBUILD) . ../$(BUILD_DIR)/html \
	    --port 8080 --open-browser


# ─── Packaging ───────────────────────────────────────────────

install: css  ## Install theme into current environment
ifdef VENV_PIP
	$(VENV_PIP) install -e .
else ifdef PIPX
	@echo "● Installing theme editable (pip fallback)…"
	pip3 install --break-system-packages -e .
else
	pip3 install --break-system-packages -e .
endif

dev: deps css install  ## Full dev setup in one command
	@echo "✓  Dev environment ready.  Run: make docs"

dist: css css-min  ## Build sdist + wheel
	$(PYTHON) -m build
	@echo "✓  Packages in dist/"

publish: dist  ## Upload to PyPI
	$(PYTHON) -m twine upload dist/*


# ─── Quality ─────────────────────────────────────────────────

lint:  ## Lint Python sources
	$(PYTHON) -m py_compile $(THEME_DIR)/__init__.py
	@echo "✓  Python sources OK"

check: lint css  ## Full pre-commit check
	cd $(DOCS_DIR) && $(SPHINX_BUILD) -b linkcheck . ../$(BUILD_DIR)/linkcheck
	@echo "✓  All checks passed"


# ─── Housekeeping ────────────────────────────────────────────

clean:  ## Remove build artifacts
	rm -rf $(BUILD_DIR) dist *.egg-info .eggs
	rm -f $(CSS_DIR)/theme.css $(CSS_DIR)/theme.min.css
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "✓  Cleaned"

clean-vendor:  ## Remove downloaded Bulma sources
	rm -rf vendor
	@echo "✓  Vendor directory removed"

clean-env:  ## Remove local .venv
	rm -rf .venv
	@echo "✓  .venv removed"

all: deps css css-min docs  ## Everything: deps → css → docs
