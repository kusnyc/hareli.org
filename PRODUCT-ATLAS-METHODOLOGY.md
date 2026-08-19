# Product Atlas — methodology, sourcing notes and caveats

`products.html` and the 100 pages under `/products/` are a **reference
catalogue**, not Hareli's own product line. Nothing on these pages claims
Hareli manufactures, sells or holds rights to any of these items — each
one remains the protected output of its own named producer region and
collective. The atlas exists so Hareli, its partners and its funders can
study proven, women-led, low-wastage product categories from across India
when designing what the federation's own units in Jharkhand, Odisha and
Chhattisgarh will actually make and sell.

## Selection brief

Every entry was chosen against three criteria, in this priority order:

1. **Carries a Geographical Indication (GI) tag**, or is very close to one
   (a handful of entries are flagged below as GI-adjacent rather than
   confirmed-registered).
2. **Produced by a predominantly women-led sector** — the harvesting,
   grading, spinning, weaving, embroidery, painting or potting step that
   defines the product's quality and value is documented as majority- or
   exclusively-women's work in that community.
3. **Long shelf life**, to minimise the financial risk of inventory
   carry-over for a self-help group. Roughly 30% of the catalogue is dried
   spices, tea, rice, pulses and preserved foods that keep for a year or
   more; the remaining ~70% is finished handloom, embroidery, natural-fibre
   and craft goods that are effectively non-perishable — the strongest
   possible answer to a wastage concern, since a finished textile or a
   fired pot does not spoil at all.

Highly perishable GI products with strong women-led credentials — fresh
mangoes, citrus, bananas, fresh flowers and similar — were deliberately
**excluded** even where famous, because they don't fit the shelf-life
brief this catalogue was built to serve.

## Standing caveat — please verify before any public or fundraising claim

This catalogue was compiled from general reference knowledge of India's
GI Registry and documented craft traditions, cross-checked against a
handful of web searches during drafting (see the citations used in the
conversation this site was built in). It was **not** verified item-by-item
against the official Geographical Indications Registry
(https://ipindiaservices.gov.in/GIRPUBLIC/) or against state handloom,
handicraft and horticulture department sources. Before this page is used
in a pitch deck, grant application or press material, please:

- Re-confirm each product's **GI registration status and year** against
  the official registry. A few entries are intentionally worded as
  "GI-documented," "GI-recognised," or "GI-registered (cluster)" rather
  than citing an exact year, where the underlying record could not be
  confidently pinned down during drafting — these are flagged in the data
  file (`data/products.json`, field `gi`) and should be checked first.
- Re-confirm the **gender composition** of each production step locally.
  General craft-sector documentation was used (news reporting, NGO and
  government livelihood-programme material, academic craft studies), but
  gender roles can vary by village, cooperative and generation, and a
  craft that is women-led in one cluster may not be everywhere.
- One entry, **Warli-style tribal painting**, is included as a well-known
  reference craft rather than a confirmed GI product — its GI status is
  explicitly marked as unconfirmed on its own page and should either be
  verified or removed before launch.

## Product photography

Every product card and detail page now uses the site's `.photo-frame`
pattern — a real photograph hotlinked from Wikimedia Commons (via
`Special:FilePath`, so no image bytes are copied into this repository),
with the same JavaScript error-fallback used elsewhere on the site: if a
Commons file is ever renamed or removed, the frame automatically reverts
to a dashed placeholder showing the same caption instead of a broken-image
icon.

**Two honesty labels are used, and they matter:**

- **16 of the 100** images are of the *specific* product/region — e.g. a
  black-pepper vine photographed in Kerala for Malabar Pepper, a makhana
  (fox nut) photograph from Nawada district, Bihar, for Bihar Makhana, a
  Chikankari embroidery close-up from Lucknow itself.
- **84 of the 100** are honestly labelled **"representative photograph"**
  on the page (and flagged `"match": "approx"` in
  `data/products.json` → `image.match`). These are real, correctly
  identified photographs of the same *general subject* — a dried red
  chilli for a chilli GI, a woman hand-embroidering for an embroidery GI,
  a handloom weaver at work for a textile GI — but they are **not**
  confirmed to be the exact GI-registered region, tribe or variety named
  on that page. This was unavoidable at this scale: dozens of the 100
  products (individual Naga tribal shawls, Mizo textile subtypes, several
  Manipuri and Arunachali weaves) are specific enough that no
  freely-licensed photograph of that *exact* textile could be confirmed to
  exist on Wikimedia Commons during drafting, in an environment with no
  network access to visually verify what a link actually loads.

**Before this atlas is used publicly, the single highest-priority task is
replacing the 84 "representative photograph" entries** — ideally with real
photography or licensed stock imagery sourced directly from each named
producer collective, state handicrafts/handloom board, or GI facilitator.
That would also remove the one deliberately weaker case in the set,
`kashmir-pashmina` / `kashmiri-sozni-embroidery` / `kashida-embroidery-of-kashmir`
/ `aari-embroidery-of-kashmir`, which currently reuse an 1867 historic
engraving rather than a modern photograph — clearly labelled as such on
the page, but worth swapping first.

To swap any single image: edit `data/products.json` → that product's
`image.file` / `image.alt` / `image.match` / `image.commons_url` fields,
then either hand-edit the corresponding `<img>`/`.photo-credit` tags in
`products.html` and `products/<slug>.html` directly, or re-run the
generation script referenced below.

## How this was built

- `data/products.json` — the structured dataset (name, category, state,
  GI status, shelf life, women's-role note, description, and the
  low-wastage "fit" rationale) for all 100 products.
- `products.html` — the category-grouped index/landing page.
- `products/<slug>.html` — one page per product, generated from the same
  dataset using the site's existing header, footer, `.img-slot`, `.badge`,
  `.card` and table components, so the pages are visually consistent with
  the rest of hareli.org.
- No build step is required to run the site — the generation script is an
  authoring tool only, not part of the deployed site. To edit a product,
  either hand-edit its `products/<slug>.html` file directly, or update
  `data/products.json` and regenerate.
