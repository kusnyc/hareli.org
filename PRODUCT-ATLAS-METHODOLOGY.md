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

## Why no product photography yet

Every product card and detail page uses the site's honest `.img-slot`
placeholder treatment (a dashed frame with a visible caption) rather than
hotlinked photography. For the earlier 7 site-wide image placeholders,
each image was individually sourced and gender/child-safety screened
against Wikimedia Commons (see `CREDITS.md`) — a process that doesn't
scale cleanly to 100 items without either (a) reusing generic,
non-specific stock photography that wouldn't actually depict the named
product/region and would risk being misleading, or (b) spending
disproportionate effort sourcing and verifying 100 individual images sight
unseen in an environment with no way to visually confirm what loads.
Leaving these as clearly labelled placeholders was the more honest choice.
The recommended path before launch is real photography or licensed stock
imagery sourced directly from each named producer collective, state
handicrafts board, or GI facilitator — which would also strengthen the
authenticity of the "reference, not resale" framing.

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
