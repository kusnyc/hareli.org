#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates products.html (catalogue index) and products/<slug>.html (100
individual product detail pages) for the Hareli site, from
data/products.json. Plain static HTML, no build step needed at deploy
time -- this script is a one-off authoring tool, not part of the site.
"""
import json, re, html, os

ROOT = "/home/claude/hareli-site"
with open(f"{ROOT}/data/products.json", encoding="utf-8") as f:
    PRODUCTS = json.load(f)

CATEGORY_ORDER = [
    "Spices, Aromatics & Dried Foods",
    "Tea Gardens",
    "Rice, Millets & Pulses",
    "Preserved & Fermented Foods",
    "Handloom Textiles",
    "Embroidery & Needlecraft",
    "Fibre, Grass & Cane Craft",
    "Tribal & Folk Art",
    "Pottery & Natural-Fibre Goods",
]
CATEGORY_SLUG = {c: re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-") for c in CATEGORY_ORDER}
CATEGORY_BADGE = {
    "Spices, Aromatics & Dried Foods": "badge--warning",
    "Tea Gardens": "badge--success",
    "Rice, Millets & Pulses": "badge--warning",
    "Preserved & Fermented Foods": "badge--info",
    "Handloom Textiles": "badge--success",
    "Embroidery & Needlecraft": "badge--success",
    "Fibre, Grass & Cane Craft": "badge--info",
    "Tribal & Folk Art": "badge--danger",
    "Pottery & Natural-Fibre Goods": "badge--danger",
}

def esc(s):
    return html.escape(s, quote=True)

def header(prefix, active):
    items = [
        ("index.html", "Home"),
        ("about.html", "About"),
        ("programmes.html", "Programmes"),
        ("products.html", "Products"),
        ("impact.html", "Model &amp; impact"),
        ("get-involved.html", "Get involved"),
        ("governance.html", "Governance"),
        ("contact.html", "Contact"),
    ]
    links = []
    for href, label in items:
        cur = ' aria-current="page"' if href == active else ""
        links.append(f'      <a href="{prefix}{href}"{cur}>{label}</a>')
    nav = "\n".join(links)
    return f"""<header class="site-header">
  <div class="container container--xl">
    <a class="brand" href="{prefix}index.html">
      <svg class="brand-mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <circle cx="20" cy="20" r="19" stroke="#2C4E29" stroke-width="1.4"/>
        <path d="M20 10c-3 4-3 8 0 12 3-4 3-8 0-12z" fill="#2C4E29"/>
        <path d="M11 24c4-2 7-1 9 2-4 2-7 1-9-2z" fill="#B5602F"/>
        <path d="M29 24c-4-2-7-1-9 2 4 2 7 1 9-2z" fill="#C1932C"/>
      </svg>
      <span class="brand-word">Hareli<small>Foundation</small></span>
    </a>
    <nav class="main-nav" aria-label="Primary">
{nav}
      <a class="btn btn-primary btn-sm" href="{prefix}get-involved.html#partner">Partner with us</a>
    </nav>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
      <svg class="icon" viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>"""

def footer(prefix):
    return f"""<footer class="site-footer">
  <div class="container container--xl">
    <div class="footer-grid">
      <div>
        <span class="brand" style="display:inline-flex;">
          <svg class="brand-mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <circle cx="20" cy="20" r="19" stroke="#FBF6EC" stroke-width="1.2" opacity="0.5"/>
            <path d="M20 10c-3 4-3 8 0 12 3-4 3-8 0-12z" fill="#FBF6EC"/>
            <path d="M11 24c4-2 7-1 9 2-4 2-7 1-9-2z" fill="#E0BE68"/>
            <path d="M29 24c-4-2-7-1-9 2 4 2 7 1 9-2z" fill="#D9A47C"/>
          </svg>
          <span class="brand-word on-inverse">Hareli<small style="color:var(--brass-300);">Foundation</small></span>
        </span>
        <p class="on-inverse-muted" style="max-width:38ch;margin-top:16px;">Hareli builds a women-owned federation of tribal producer collectives across Jharkhand, Odisha and Chhattisgarh — turning self-help groups into an industrial-scale, community-owned manufacturing institution.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="{prefix}about.html">About Hareli</a>
        <a href="{prefix}programmes.html">Programmes</a>
        <a href="{prefix}products.html">Product atlas</a>
        <a href="{prefix}impact.html">Model &amp; impact</a>
        <a href="{prefix}governance.html">Governance</a>
      </div>
      <div>
        <h4>Get involved</h4>
        <a href="{prefix}get-involved.html#donate">Make a gift</a>
        <a href="{prefix}get-involved.html#partner">Become a partner</a>
        <a href="{prefix}get-involved.html#csr">CSR collaboration</a>
        <a href="{prefix}contact.html">Contact the founder's office</a>
      </div>
      <div>
        <h4>Offices</h4>
        <p class="on-inverse-muted">NFPC Limited (Hareli Federation)<br>Raipur, Chhattisgarh, India</p>
        <a href="{prefix}contact.html#offices">All office locations →</a>
        <a href="mailto:connect@hareli.org">connect@hareli.org</a>
      </div>
    </div>
    <hr class="divider divider--inverse">
    <div class="footer-bottom">
      <span>&copy; <span data-year></span> Hareli Foundation. All rights reserved.</span>
      <span>Hareli.org is the philanthropic and social-capital arm of the Hareli initiative.</span>
    </div>
  </div>
</footer>"""

def head(prefix, title, description):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="{prefix}images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/tokens.css?v=3">
<link rel="stylesheet" href="{prefix}css/styles.css?v=3">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

FOOT_SCRIPT = """
<script src="{prefix}js/main.js"></script>
</body>
</html>
"""

# ---------------------------------------------------------------
# Photo-frame media block (real hotlinked Commons image + honest fallback)
# ---------------------------------------------------------------
def photo_frame_media(p, extra_class, link_credit=True):
    # link_credit=False MUST be used whenever this media block will sit
    # inside another <a> (e.g. a product-card that links to the detail
    # page) -- a nested <a> inside an <a> is invalid HTML and browsers
    # will silently close the outer link early, splitting the card's
    # image and text into two separate elements and wrecking the grid.
    img = p["image"]
    file_url = img["file"].replace(" ", "%20")
    img_src = f"https://commons.wikimedia.org/wiki/Special:FilePath/File:{file_url}?width=900"
    note = "" if img["match"] == "exact" else " (representative photograph)"
    if link_credit:
        credit = f'<a class="photo-credit" href="{img["commons_url"]}" target="_blank" rel="noopener">Wikimedia Commons &#8599;</a>'
    else:
        credit = f'<span class="photo-credit photo-credit--static">Wikimedia Commons</span>'
    return (
        f'<div class="photo-frame img-slot--sq {extra_class}">\n'
        f'          <img src="{img_src}" alt="{esc(img["alt"])}" loading="lazy">\n'
        f'          <span class="img-slot-label photo-fallback"><span>Photograph — {esc(img["alt"])}{note}. '
        f'Source image unavailable; caption preserved.</span></span>\n'
        f'          {credit}\n'
        f'        </div>'
    )

# ---------------------------------------------------------------
# Product card partial (used on the index + related-products blocks)
# ---------------------------------------------------------------
def product_card(p, prefix, filterable=False):
    media = photo_frame_media(p, "product-card-media", link_credit=False)
    attrs = ""
    if filterable:
        search_key = f"{p['name']} {p['state']} {p['category']}".lower()
        attrs = f' data-category="{CATEGORY_SLUG[p["category"]]}" data-search="{esc(search_key)}"'
    return f"""      <a class="product-card"{attrs} href="{prefix}products/{p['slug']}.html">
        {media}
        <div class="product-card-body">
          <span class="product-card-cat">{esc(p['category'])}</span>
          <h3 class="product-card-name">{esc(p['name'])}</h3>
          <span class="product-card-state">{esc(p['state'])}</span>
          <div class="product-card-meta">
            <span class="badge {CATEGORY_BADGE.get(p['category'],'badge--info')}">GI-linked</span>
            <span class="badge badge--success">Long shelf life</span>
          </div>
        </div>
      </a>"""

# ---------------------------------------------------------------
# Build products.html (index)
# ---------------------------------------------------------------
def build_index():
    by_cat = {c: [] for c in CATEGORY_ORDER}
    for p in PRODUCTS:
        by_cat.setdefault(p["category"], []).append(p)

    chips = ['        <button type="button" class="filter-chip is-active" data-filter="all">All <span class="count">(100)</span></button>']
    for c in CATEGORY_ORDER:
        items = by_cat.get(c, [])
        if not items:
            continue
        chips.append(
            f'        <button type="button" class="filter-chip" data-filter="{CATEGORY_SLUG[c]}">'
            f'{esc(c)} <span class="count">({len(items)})</span></button>'
        )
    chips_html = "\n".join(chips)

    # Stable order: grouped by category (so browsing "All" still reads as
    # organised), but every card carries data-category/data-search so the
    # toolbar can filter/search client-side without a page reload.
    ordered = [p for c in CATEGORY_ORDER for p in by_cat.get(c, [])]
    cards_html = "\n".join(product_card(p, "", filterable=True) for p in ordered)

    body = f"""{head("", "Product Atlas — 100 GI-tagged, women-led Indian products | Hareli Foundation",
        "A curated atlas of 100 famous, GI-tagged ethnic Indian products from predominantly women-led production sectors, weighted toward long-shelf-life goods that protect SHG inventory from wastage.")}
{header("", "products.html")}

<main id="main">

  <section class="section">
    <div class="container container--xl">
      <span class="eyebrow">Reference catalogue · Not yet Hareli's own product line</span>
      <h1 class="display-lg" style="margin-top:14px;max-width:22ch;">A Product Atlas: 100 GI-tagged products from India's women-led producer sectors.</h1>
      <p class="lede" style="margin-top:20px;max-width:68ch;">This atlas documents 100 of India's most famous Geographical Indication (GI) tagged products, drawn overwhelmingly from sectors where women — spice sorters and graders, tea pluckers, silk reelers, embroiderers, tribal weavers and painters — do the majority of the skilled, income-generating work. Every entry is weighted toward <strong>long shelf life</strong>: dried spices, tea, rice and pulses that store for a year or more, and finished handloom, embroidery and craft goods that do not spoil at all. That bias is deliberate — it mirrors the manufacturing thesis in Hareli's <a href="impact.html">model &amp; impact</a> plan, where extended inventory carry-over must never become a source of financial loss for the SHGs behind a product.</p>
      <p class="lede" style="margin-top:16px;max-width:68ch;">This is a research and inspiration library, not a live storefront: Hareli does not yet manufacture or sell these specific branded GI products, most of which are the protected output of their own named producer regions and collectives. It exists so the federation — and its partners — can study proven, women-led, low-wastage product categories when designing what Hareli's own units will make. See the <a href="PRODUCT-ATLAS-METHODOLOGY.md">methodology &amp; sourcing notes</a> for how this list was compiled and what should be re-verified before any public or fundraising claim is made from it.</p>

      <div class="cluster gap-3" style="margin-top:32px;">
        <div class="stat-tile">
          <span class="stat-value">100</span>
          <span class="stat-label">GI-linked products catalogued</span>
        </div>
        <div class="stat-tile">
          <span class="stat-value">9</span>
          <span class="stat-label">categories, 20 states &amp; UTs</span>
        </div>
        <div class="stat-tile">
          <span class="stat-value">0</span>
          <span class="stat-label">spoilage risk on ~70% of entries (non-perishable finished goods)</span>
        </div>
      </div>

    </div>
  </section>

  <section class="section section--sm" style="padding-top:0;">
    <div class="container container--xl">
      <div class="product-toolbar">
        <div class="product-filter-bar" role="tablist" aria-label="Filter by category" id="product-filter-bar">
{chips_html}
        </div>
        <div class="product-search">
          <input type="search" id="product-search-input" placeholder="Search by product, state or community…" aria-label="Search products">
        </div>
      </div>

      <p class="product-results-count" id="product-results-count">Showing all 100 products</p>

      <div class="product-grid" id="product-grid">
{cards_html}
      </div>

      <p class="product-empty-state" id="product-empty-state" hidden>No products match your filters. <button type="button" class="btn-ghost" id="product-clear-filters">Clear filters</button></p>

      <div class="wastage-note" style="margin-top:48px;max-width:74ch;">
        <svg class="icon icon--lg" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/></svg>
        <p>Why long shelf life matters here: an SHG that pre-finances raw material and labour for a perishable product carries real risk of loss if a sale is delayed even by a few weeks. Every product in this atlas was chosen to minimise that risk — either because the raw material is naturally durable when dried (spice, tea, rice, jaggery), or because the product itself is a finished, non-perishable good (a woven textile, an embroidered panel, a fired pot) that can be held in inventory indefinitely without loss of value.</p>
      </div>

      <div class="card" style="margin-top:40px;max-width:74ch;">
        <h3 style="margin-top:0;">Interested in helping Hareli build product lines like these?</h3>
        <p style="margin-top:10px;">Partners, CSR teams and impact investors can help Hareli's own federation members develop GI-quality, low-wastage product lines rooted in Jharkhand, Odisha and Chhattisgarh.</p>
        <a class="btn btn-primary" style="margin-top:16px;" href="get-involved.html">Partner with Hareli</a>
      </div>
    </div>
  </section>

</main>

{footer("")}
{FOOT_SCRIPT.format(prefix="")}"""
    with open(f"{ROOT}/products.html", "w", encoding="utf-8") as f:
        f.write(body)


# ---------------------------------------------------------------
# Build one product detail page
# ---------------------------------------------------------------
def build_detail(p, all_by_cat):
    prefix = "../"
    related = [x for x in all_by_cat[p["category"]] if x["slug"] != p["slug"]][:3]
    if len(related) < 3:
        # top up from the overall list, excluding self and already-picked
        pool = [x for x in PRODUCTS if x["slug"] != p["slug"] and x not in related]
        related += pool[: 3 - len(related)]
    related_html = "\n".join(product_card(r, prefix) for r in related)

    title = f"{p['name']} — Product Atlas | Hareli Foundation"
    desc = p["description"][:155]

    body = f"""{head(prefix, title, desc)}
{header(prefix, "")}

<main id="main">

  <section class="section section--sm">
    <div class="container container--xl">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="{prefix}index.html">Home</a>
        <span aria-hidden="true">/</span>
        <a href="{prefix}products.html">Products</a>
        <span aria-hidden="true">/</span>
        <a href="{prefix}products.html#{CATEGORY_SLUG[p['category']]}">{esc(p['category'])}</a>
        <span aria-hidden="true">/</span>
        <span class="current">{esc(p['name'])}</span>
      </nav>

      <div class="product-hero-grid">
        {photo_frame_media(p, "product-hero-media")}
        <div>
          <span class="eyebrow">{esc(p['category'])} · {esc(p['state'])}</span>
          <h1 class="display-md" style="margin-top:12px;">{esc(p['name'])}</h1>
          <p class="lede" style="margin-top:18px;">{esc(p['description'])}</p>

          <div class="product-badges">
            <span class="badge badge--success">GI status: {esc(p['gi'])}</span>
            <span class="badge badge--warning">Shelf life: {esc(p['shelf'])}</span>
            <span class="badge badge--info">Women-led sector</span>
          </div>

          <table class="product-info-table">
            <tbody>
              <tr><th>Category</th><td>{esc(p['category'])}</td></tr>
              <tr><th>Region</th><td>{esc(p['state'])}</td></tr>
              <tr><th>GI status</th><td>{esc(p['gi'])}</td></tr>
              <tr><th>Typical shelf life</th><td>{esc(p['shelf'])}</td></tr>
              <tr><th>Women's role in production</th><td>{esc(p['women_led'])}</td></tr>
            </tbody>
          </table>

          <div class="wastage-note">
            <svg class="icon" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/></svg>
            <p><strong>Why this fits a low-wastage SHG model:</strong> {esc(p['fit'])}</p>
          </div>

          <div class="cluster gap-2" style="margin-top:28px;">
            <a class="btn btn-outline" href="{prefix}products.html">&larr; Back to the Product Atlas</a>
            <a class="btn btn-primary" href="{prefix}get-involved.html">Partner with Hareli</a>
          </div>
        </div>
      </div>

      <h2 class="display-sm" style="margin-top:64px;">Related products</h2>
      <div class="related-grid">
{related_html}
      </div>
    </div>
  </section>

</main>

{footer(prefix)}
{FOOT_SCRIPT.format(prefix=prefix)}"""
    os.makedirs(f"{ROOT}/products", exist_ok=True)
    with open(f"{ROOT}/products/{p['slug']}.html", "w", encoding="utf-8") as f:
        f.write(body)


def main():
    build_index()
    by_cat = {c: [] for c in CATEGORY_ORDER}
    for p in PRODUCTS:
        by_cat.setdefault(p["category"], []).append(p)
    for p in PRODUCTS:
        build_detail(p, by_cat)
    print(f"Built products.html + {len(PRODUCTS)} detail pages.")

if __name__ == "__main__":
    main()
