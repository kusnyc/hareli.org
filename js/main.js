// Hareli Foundation — shared site behaviour (no build step, no framework)
(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
  }

  // Hotlinked photographs: fall back to the honest placeholder treatment if a
  // source image fails to load, instead of showing a broken-image icon.
  document.querySelectorAll(".photo-frame img").forEach(function (img) {
    img.addEventListener("error", function () {
      var frame = img.closest(".photo-frame");
      if (frame) frame.classList.add("photo-error");
    }, { once: true });
  });

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Toast helper
  function showToast(message) {
    var toast = document.querySelector(".toast");
    if (!toast) return;
    toast.querySelector(".toast-message").textContent = message;
    toast.classList.add("show");
    clearTimeout(toast._timer);
    toast._timer = setTimeout(function () { toast.classList.remove("show"); }, 4200);
  }
  window.HareliToast = showToast;

  // Static-site friendly form handling: intercepts submit, shows a receipt-style
  // confirmation. Wire data-endpoint (e.g. Formspree/Cloudflare Worker) to actually send.
  document.querySelectorAll("form[data-static-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      var endpoint = form.getAttribute("data-endpoint");
      if (!endpoint) {
        e.preventDefault();
        var name = form.querySelector("[name='name']");
        showToast("Enquiry recorded. We reply within five working days" + (name && name.value ? ", " + name.value.split(" ")[0] + "." : "."));
        form.reset();
      }
      // If data-endpoint is set, the form submits normally to that endpoint.
    });
  });

  // Active nav link (in case a page forgets aria-current)
  var path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".main-nav a[href]").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.setAttribute("aria-current", "page");
    }
  });

  // Product Atlas: client-side category filter + search, no page reload.
  var grid = document.getElementById("product-grid");
  if (grid) {
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".product-card"));
    var chips = Array.prototype.slice.call(document.querySelectorAll("#product-filter-bar .filter-chip"));
    var searchInput = document.getElementById("product-search-input");
    var resultsCount = document.getElementById("product-results-count");
    var emptyState = document.getElementById("product-empty-state");
    var clearBtn = document.getElementById("product-clear-filters");
    var activeFilter = "all";

    function applyFilters() {
      var query = (searchInput && searchInput.value || "").trim().toLowerCase();
      var visible = 0;
      cards.forEach(function (card) {
        var matchesCategory = activeFilter === "all" || card.getAttribute("data-category") === activeFilter;
        var matchesSearch = !query || (card.getAttribute("data-search") || "").indexOf(query) !== -1;
        var show = matchesCategory && matchesSearch;
        card.classList.toggle("is-hidden", !show);
        if (show) visible++;
      });
      if (resultsCount) {
        resultsCount.textContent = (activeFilter === "all" && !query)
          ? "Showing all " + cards.length + " products"
          : "Showing " + visible + " of " + cards.length + " products";
      }
      if (emptyState) emptyState.hidden = visible !== 0;
      grid.hidden = visible === 0;
    }

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        activeFilter = chip.getAttribute("data-filter");
        applyFilters();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", applyFilters);
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        activeFilter = "all";
        chips.forEach(function (c) { c.classList.toggle("is-active", c.getAttribute("data-filter") === "all"); });
        if (searchInput) searchInput.value = "";
        applyFilters();
      });
    }
  }
})();
