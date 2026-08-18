# hareli.org

The public website for **Hareli Foundation** — the philanthropic and social-capital
arm building a women-owned tribal manufacturing federation across Jharkhand, Odisha
and Chhattisgarh.

Plain static HTML/CSS/JS. No build step, no framework, no dependencies to install.

## What's here

```
index.html          Home
about.html           About Hareli / case for support
programmes.html      The four programme verticals
impact.html          The seven-layer federation model, 5-year targets, capital plan
get-involved.html    Donate / partner / CSR / enquiry form
governance.html      Governance principles and (pending) filings
contact.html         Contact form and details
404.html             Not-found page (served automatically by Cloudflare Pages)
css/tokens.css        Design tokens (colour, type, spacing, shadow, motion)
css/styles.css        Components and layout, imports tokens.css
js/main.js             Mobile nav, toast confirmations, static-form handling
images/favicon.svg    Site mark
robots.txt, sitemap.xml, _headers   SEO + security headers for Cloudflare Pages
```

## Design system

See the flagged-substitution notes at the top of `css/tokens.css`. In short:
this is an **original visual identity built for Hareli**, not a real, supplied
brand. No logo, photography or licensed fonts were provided at the time of
writing, so:

- **Fonts** are Google Fonts substitutes — Fraunces (display), IBM Plex Sans
  (body/UI), IBM Plex Mono (figures) — loaded from `fonts.googleapis.com` in
  each page's `<head>`. Swap for licensed fonts by editing the `<link>` tags
  and `--font-*` tokens.
- **Photography** is a mix: four slots (`.photo-frame`) now hotlink real,
  freely-licensed photographs from Wikimedia Commons — see `CREDITS.md` for
  the full list, sources, and an important caveat about verifying them
  visually before launch. The remaining slots (`.img-slot`) are still dashed,
  labelled placeholders where no confidently-matching photo was found;
  replace an `.img-slot` div with a `.photo-frame` block (copy the pattern
  used elsewhere in the same file) once real photography exists.
- **Icons** are a small hand-drawn inline SVG set (no external icon library),
  so the site has zero runtime dependency on an icon CDN.
- **Decorative motifs** (the small triangle/dot band under the hero) are
  original geometric line art in the general idiom of Eastern Indian tribal
  wall-art traditions (Warli/Sohrai/Kohbar) — drawn fresh for this project,
  not a reproduction of any specific artwork.

## Content sourcing

Copy is drawn from the foundation's own working documents (case for support,
outreach playbook, design system spec). The confidential internal donor
prospect lists and target-ask figures are **deliberately not reproduced** on
the public site — `get-involved.html` describes partnership *categories*
(capital / capability / scale) instead of naming specific prospects.

`governance.html` is written honestly for an institution in its founding
phase: no invented trustee names, financials or registration numbers. Replace
the "pending" document cards once real filings exist.

## Local preview

No build step needed. From this folder:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

or simply open `index.html` directly in a browser (all paths are relative).

## Deploying: GitHub → Cloudflare Pages

### 1. Push this folder to a new GitHub repository

```bash
cd hareli-site
git init
git add .
git commit -m "Initial Hareli Foundation website"
git branch -M main
git remote add origin https://github.com/<your-org>/hareli-org.git
git push -u origin main
```

### 2. Connect the repo in Cloudflare Pages

1. Cloudflare dashboard → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**.
2. Select the `hareli-org` repository and the `main` branch.
3. Build settings — this is a static site, so:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/` (repository root)
4. Click **Save and Deploy**. Cloudflare builds and serves the site at
   `<project-name>.pages.dev` within a minute or two.

### 3. Connect the custom domain

1. In the Pages project → **Custom domains** → **Set up a custom domain** → enter `hareli.org` (and `www.hareli.org` if wanted).
2. If the domain's DNS is already on Cloudflare, the CNAME/records are added automatically.
   Otherwise, add the CNAME Cloudflare shows you at your DNS provider.
3. HTTPS is issued automatically; typically live within a few minutes.

### 4. Every future push to `main` auto-deploys

Cloudflare Pages redeploys automatically on every push to the connected
branch. Pull requests get their own preview URL automatically — useful for
reviewing copy or design changes before they go live.

### Notes

- `_headers` sets basic security headers and caching for static assets —
  Cloudflare Pages reads this file automatically; no configuration needed.
- `404.html` is served automatically by Cloudflare Pages for any unmatched
  path; no `_redirects` rule is required for it.
- The enquiry/contact forms (`get-involved.html`, `contact.html`) currently
  intercept `submit` client-side and show a confirmation toast — they do not
  send anywhere yet. To make them functional, either:
  - point the form's `action` at a form backend (e.g. Formspree, Cloudflare
    Pages Forms via a Worker, Basin) and remove the `data-static-form`
    attribute, or
  - set `data-endpoint="https://your-endpoint"` on the `<form>` — `js/main.js`
    already checks for this attribute and will let the submit through instead
    of intercepting it.

## Content still needed from the brand owner

1. Real photography from the field (Jharkhand / Odisha / Chhattisgarh) — every
   `.img-slot` states what it expects.
2. A logo/wordmark, if one exists or is commissioned — the current mark is an
   original placeholder geometric device (sal leaf + two dye-colour accents).
3. Legal registration details, trustee list, and first audited statements for
   `governance.html`.
4. A confirmed contact email/domain (`connect@hareli.org` /
   `partnerships@hareli.org` are placeholders matching the `hareli.org`
   domain — confirm or replace before launch).
