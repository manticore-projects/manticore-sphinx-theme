/**
 * Bulma Sphinx Theme — client-side behaviour
 *
 * Features:
 *   1. Mobile sidebar toggle
 *   2. Floating on-page TOC with fold/unfold button
 *   3. Scroll-spy for on-page TOC
 *   4. Sidebar scroll-to-current on page load
 *   5. Dark mode: 3-state cycle (system → dark → light → system)
 *   6. Keyboard shortcuts (/, t, Escape)
 *
 * Dark mode architecture:
 *   - An inline <script> in <head> (layout.html) reads localStorage
 *     and sets data-theme BEFORE rendering to prevent flash.
 *   - This file only handles the toggle button and icon updates.
 *   - CSS @media(prefers-color-scheme:dark) handles "system" mode.
 */
(function () {
  "use strict";

  // ── DOM refs ────────────────────────────────────────────
  var sidebar   = document.getElementById("bst-sidebar");
  var sidebarToggle = document.getElementById("bst-sidebar-toggle");
  var overlay   = document.getElementById("bst-overlay");
  var pageToc   = document.getElementById("bst-page-toc");
  var tocToggle = document.getElementById("bst-toc-toggle");
  var tocLinks  = pageToc ? pageToc.querySelectorAll("a") : [];
  var headings  = [];


  // ═══════════════════════════════════════════════════════════
  //  1. MOBILE SIDEBAR TOGGLE
  // ═══════════════════════════════════════════════════════════

  function openSidebar() {
    if (!sidebar) return;
    sidebar.classList.add("is-open");
    if (overlay) overlay.classList.add("is-visible");
    if (sidebarToggle) {
      sidebarToggle.classList.add("is-active");
      sidebarToggle.setAttribute("aria-expanded", "true");
    }
    document.body.style.overflow = "hidden";
  }

  function closeSidebar() {
    if (!sidebar) return;
    sidebar.classList.remove("is-open");
    if (overlay) overlay.classList.remove("is-visible");
    if (sidebarToggle) {
      sidebarToggle.classList.remove("is-active");
      sidebarToggle.setAttribute("aria-expanded", "false");
    }
    document.body.style.overflow = "";
  }

  if (sidebarToggle) {
    sidebarToggle.addEventListener("click", function () {
      sidebar.classList.contains("is-open") ? closeSidebar() : openSidebar();
    });
  }
  if (overlay) {
    overlay.addEventListener("click", closeSidebar);
  }


  // ═══════════════════════════════════════════════════════════
  //  2. FLOATING TOC — FOLD / UNFOLD
  // ═══════════════════════════════════════════════════════════

  function expandToc() {
    if (!pageToc || !tocToggle) return;
    pageToc.classList.remove("is-collapsed");
    tocToggle.setAttribute("aria-expanded", "true");
  }

  function collapseToc() {
    if (!pageToc || !tocToggle) return;
    pageToc.classList.add("is-collapsed");
    tocToggle.setAttribute("aria-expanded", "false");
  }

  function toggleToc() {
    if (!pageToc) return;
    pageToc.classList.contains("is-collapsed") ? expandToc() : collapseToc();
  }

  if (tocToggle) {
    tocToggle.addEventListener("click", toggleToc);
  }

  function setInitialTocState() {
    if (!pageToc) return;

    // Count top-level TOC entries
    var topItems = pageToc.querySelectorAll(":scope > ul > li");
    var totalItems = pageToc.querySelectorAll("li").length;

    // Only expand by default if >5 items AND wide screen
    if (totalItems > 5 && window.innerWidth >= 1280) {
      expandToc();
    } else {
      collapseToc();
    }
  }


  // ═══════════════════════════════════════════════════════════
  //  2b. TOC FILTER — interactive search on keystroke
  // ═══════════════════════════════════════════════════════════

  function initTocFilter() {
    var filterInput = document.getElementById("bst-toc-filter");
    if (!filterInput || !pageToc) return;

    var allItems = pageToc.querySelectorAll("li");

    filterInput.addEventListener("input", function () {
      var query = filterInput.value.toLowerCase().trim();

      if (!query) {
        // Show all items
        allItems.forEach(function (li) {
          li.classList.remove("bst-toc-hidden");
        });
        return;
      }

      allItems.forEach(function (li) {
        var link = li.querySelector("a");
        if (!link) return;
        var text = link.textContent.toLowerCase();
        if (text.indexOf(query) !== -1) {
          li.classList.remove("bst-toc-hidden");
          // Also show all parent <li>s
          var parent = li.parentElement;
          while (parent) {
            if (parent.tagName === "LI") {
              parent.classList.remove("bst-toc-hidden");
            }
            if (parent === pageToc) break;
            parent = parent.parentElement;
          }
        } else {
          li.classList.add("bst-toc-hidden");
        }
      });
    });

    // Clear filter on Escape
    filterInput.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        filterInput.value = "";
        filterInput.dispatchEvent(new Event("input"));
        filterInput.blur();
      }
    });
  }


  // ═══════════════════════════════════════════════════════════
  //  3. SCROLL-SPY FOR ON-PAGE TOC
  // ═══════════════════════════════════════════════════════════

  function initScrollSpy() {
    if (!tocLinks.length) return;

    tocLinks.forEach(function (link) {
      var href = link.getAttribute("href");
      if (!href || href.charAt(0) !== "#") return;
      var heading = document.getElementById(href.slice(1));
      if (heading) headings.push({ el: heading, link: link });
    });

    if (!headings.length) return;

    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var offset = 120;
        var current = null;
        for (var i = 0; i < headings.length; i++) {
          if (headings[i].el.getBoundingClientRect().top <= offset) {
            current = headings[i];
          }
        }
        tocLinks.forEach(function (l) { l.classList.remove("is-active"); });
        if (current) current.link.classList.add("is-active");
        ticking = false;
      });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }


  // ═══════════════════════════════════════════════════════════
  //  4. SMOOTH-SCROLL FOR ANCHOR LINKS
  // ═══════════════════════════════════════════════════════════

  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (!id || id === "#") return;
        var target = document.getElementById(id.slice(1));
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        history.replaceState(null, "", id);
      });
    });
  }


  // ═══════════════════════════════════════════════════════════
  //  5. SIDEBAR: MARK CURRENT + SCROLL INTO VIEW
  // ═══════════════════════════════════════════════════════════

  function syncSidebarToCurrent() {
    if (!sidebar) return;

    var path = window.location.pathname;
    var normPath = path.replace(/index\.html$/, "").replace(/\/$/, "");
    var links = sidebar.querySelectorAll(".bst-sidebar__nav a");
    var currentLink = null;
    var bestLen = -1;

    links.forEach(function (link) {
      var href = link.getAttribute("href");
      if (!href) return;
      var a = document.createElement("a");
      a.href = href;
      var resolved = a.pathname.replace(/index\.html$/, "").replace(/\/$/, "");
      if (resolved === normPath || a.pathname === path) {
        if (resolved.length > bestLen) {
          bestLen = resolved.length;
          currentLink = link;
        }
      }
    });

    if (!currentLink) return;

    currentLink.classList.add("current");
    var li = currentLink.parentElement;
    while (li) {
      if (li.tagName === "LI") li.classList.add("current");
      if (li.classList && li.classList.contains("bst-sidebar__nav")) break;
      li = li.parentElement;
    }

    var scrollContainer = sidebar.querySelector(".bst-sidebar__scroll");
    if (!scrollContainer) return;

    requestAnimationFrame(function () {
      var containerRect = scrollContainer.getBoundingClientRect();
      var linkRect = currentLink.getBoundingClientRect();
      var linkTop = linkRect.top - containerRect.top + scrollContainer.scrollTop;
      var targetScroll = linkTop - (scrollContainer.clientHeight / 3);
      scrollContainer.scrollTo({
        top: Math.max(0, targetScroll),
        behavior: "instant"
      });
    });
  }


  // ═══════════════════════════════════════════════════════════
  //  6. DARK MODE — 3-state toggle
  //
  //  States: "system" (default) → "dark" → "light" → "system"
  //
  //  "system": no data-theme attr on <html>, CSS @media handles it
  //  "dark":   data-theme="dark" on <html>
  //  "light":  data-theme="light" on <html>
  //
  //  localStorage stores: null/"system", "dark", or "light"
  // ═══════════════════════════════════════════════════════════

  var THEME_KEY = "bst-theme";

  function getStoredTheme() {
    try {
      return localStorage.getItem(THEME_KEY);
    } catch (e) {
      return null;
    }
  }

  function getOsPrefersDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  // Returns "system", "dark", or "light"
  function getCurrentMode() {
    var stored = getStoredTheme();
    if (stored === "dark" || stored === "light") return stored;
    return "system";
  }

  function applyMode(mode) {
    if (mode === "dark" || mode === "light") {
      document.documentElement.setAttribute("data-theme", mode);
      try { localStorage.setItem(THEME_KEY, mode); } catch (e) {}
    } else {
      // "system" — remove attribute, let CSS @media decide
      document.documentElement.removeAttribute("data-theme");
      try { localStorage.removeItem(THEME_KEY); } catch (e) {}
    }
    updateThemeIcons(mode);
  }

  function updateThemeIcons(mode) {
    var btn = document.getElementById("bst-theme-toggle");
    if (!btn) return;

    // Determine which icon to show based on effective appearance
    var effective;
    if (mode === "system") {
      effective = getOsPrefersDark() ? "dark" : "light";
    } else {
      effective = mode;
    }

    // Update button state
    btn.setAttribute("data-mode", mode);

    // Labels
    var labels = {
      system: "Colour scheme: System (click to change)",
      dark:   "Colour scheme: Dark (click to change)",
      light:  "Colour scheme: Light (click to change)"
    };
    btn.setAttribute("aria-label", labels[mode] || labels.system);
    btn.title = labels[mode] || labels.system;
  }

  function cycleTheme() {
    var current = getCurrentMode();
    // system → dark → light → system
    var next;
    if (current === "system") next = "dark";
    else if (current === "dark") next = "light";
    else next = "system";
    applyMode(next);
  }

  function initDarkMode() {
    var btn = document.getElementById("bst-theme-toggle");

    // Set initial icon state (the <head> script already set data-theme)
    updateThemeIcons(getCurrentMode());

    if (btn) {
      btn.addEventListener("click", cycleTheme);
    }

    // Listen for OS preference changes
    if (window.matchMedia) {
      window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () {
        // Only update icons if in system mode
        if (getCurrentMode() === "system") {
          updateThemeIcons("system");
        }
      });
    }
  }


  // ═══════════════════════════════════════════════════════════
  //  7. KEYBOARD SHORTCUTS
  // ═══════════════════════════════════════════════════════════

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeSidebar();
      collapseToc();
      return;
    }

    var active = document.activeElement;
    var isInput = active && (active.tagName === "INPUT" ||
                             active.tagName === "TEXTAREA" ||
                             active.isContentEditable);
    if (isInput) return;

    if (e.key === "/" && !e.ctrlKey && !e.metaKey) {
      var search = document.querySelector(".bst-search-field__input");
      if (search) {
        e.preventDefault();
        search.focus();
      }
    }

    if (e.key === "t" && !e.ctrlKey && !e.metaKey && !e.altKey) {
      toggleToc();
    }
  });


  // ═══════════════════════════════════════════════════════════
  //  8. PAGINATION — strip section numbers from titles
  //     Sphinx outputs "2. RISK VBox" with numbered sections.
  //     We strip the leading "N. " or "N.N. " prefix.
  // ═══════════════════════════════════════════════════════════

  function fixPaginationTitles() {
    var titles = document.querySelectorAll(".bst-pagination__title");
    titles.forEach(function (el) {
      // Strip leading section numbers like "2. ", "3.1. ", "12.3.4. "
      el.textContent = el.textContent.replace(/^[\d.]+\s+/, "");
    });
  }


  // ═══════════════════════════════════════════════════════════
  //  INIT
  // ═══════════════════════════════════════════════════════════

  document.addEventListener("DOMContentLoaded", function () {
    setInitialTocState();
    initScrollSpy();
    initSmoothScroll();
    syncSidebarToCurrent();
    initDarkMode();
    initTocFilter();
    fixPaginationTitles();
  });

})();
