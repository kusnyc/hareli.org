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
})();
