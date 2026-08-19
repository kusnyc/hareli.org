# Photo credits

Every image slot on the site now uses a real, freely-licensed photograph
hotlinked from Wikimedia Commons (via `Special:FilePath`, which redirects to
the current file at the requested width — no image files are copied into
this repository).

**Selection rule:** because Hareli is a women's organisation, every candidate
was screened to avoid a man in a prominent role in the shot. Where a file's
title didn't make the people in it unambiguous (e.g. generic "tribal
people," or a craft strongly associated with male artisans in that region —
Sambalpuri ikat weaving is traditionally a male-dominated handloom craft in
Odisha, so two earlier picks using it were dropped), the image was replaced
with one whose title explicitly says "woman"/"women," or with one clearly
depicting only women (e.g. a female minister addressing women workers).

**Two of the seven are approximate matches, honestly labelled as such** —
see "Approximate matches" below. Forcing an exact-scene photo (a federation's
own water-bottling line, an actual CSR site visit) wasn't possible without
either a mismatch or a gender-safety risk, so the closest safe, real
alternative was used with a caption that says what it actually shows.

**Standing caveat:** these were selected by searching Wikimedia Commons for
files with clear, self-describing titles, because the environment this site
was built in cannot load actual image bytes to visually confirm content
before publishing (no network access to image hosts). **Before launch, open
every page and confirm each photograph looks right** — swap the `src` (and
matching `photo-credit` link) on any that don't by editing the `<img>` tag
directly; no build step is required.

| Page | Section | File | Commons page |
|---|---|---|---|
| `index.html` | Hero | `Khariya Tribal lady from Jharkhand.jpg` | https://commons.wikimedia.org/wiki/File:Khariya_Tribal_lady_from_Jharkhand.jpg |
| `about.html` | The problem | `Santal woman in a traditional saree.jpg` | https://commons.wikimedia.org/wiki/File:Santal_woman_in_a_traditional_saree.jpg |
| `programmes.html` | Women's enterprise | `Group of Indian women in sari.jpg` | https://commons.wikimedia.org/wiki/File:Group_of_Indian_women_in_sari.jpg |
| `programmes.html` | Rural manufacturing † | `Woman harvesting wheat, Raisen district, Madhya Pradesh, India ggia version.jpg` | https://commons.wikimedia.org/wiki/File:Woman_harvesting_wheat,_Raisen_district,_Madhya_Pradesh,_India_ggia_version.jpg |
| `programmes.html` | Leadership development | `SHG meeting.jpg` | https://commons.wikimedia.org/wiki/File:SHG_meeting.jpg |
| `programmes.html` | Community institutions | `Women at farmers rally, Bhopal, India, Nov 2005.jpg` | https://commons.wikimedia.org/wiki/File:Women_at_farmers_rally,_Bhopal,_India,_Nov_2005.jpg |
| `get-involved.html` | CSR collaboration † | `The Union Minister for Women and Child Development... addressing the Anganwadi workers... at Manan Kendra, in Gangtok.jpg` | https://commons.wikimedia.org/wiki/File:The_Union_Minister_for_Women_and_Child_Development,_Smt._Maneka_Sanjay_Gandhi_addressing_the_Anganwadi_workers_and_other_women_and_child_development_functionaries,_at_Manan_Kendra,_in_Gangtok.jpg |

† = approximate match, see below.

## Approximate matches

- **Rural manufacturing** uses a photo of a woman harvesting wheat in Madhya
  Pradesh — not Hareli's own packaged-water or beverage line (no
  gender-safe, unambiguous photo of an actual Indian rural manufacturing
  floor turned up in search). It's captioned as illustrative of rural
  women's productive labour, not as Hareli's facility. Replace with real
  production-floor photography as soon as it exists — this is the highest-
  priority swap on the site.
- **CSR collaboration** uses a Press Information Bureau photo of the then
  Union Minister for Women and Child Development addressing Anganwadi
  workers in Gangtok — an all-women engagement (minister and audience both
  women), but not an actual Hareli site visit. Captioned accordingly.
  Replace with a real CSR site-visit photo once one exists.

All content hosted on Wikimedia Commons is required to carry a free license
(public domain, CC0, CC-BY, or CC-BY-SA) — but the exact licence and the
photographer's name to credit varies file to file. **Before publishing,
open each Commons page above and copy the exact attribution line its licence
requires** (most CC-BY-SA files want "© [Photographer name], CC BY-SA
[version], via Wikimedia Commons"; PIB photos are typically GODL-India
licensed). Each photo already links out to its Commons file page via the
small "Wikimedia Commons ↗" tag in its bottom-right corner, which covers the
"link to the file page" part of CC-BY-SA — add the photographer's name to
that link text once confirmed if your organisation's compliance standard
requires a fuller credit.

## Resilience

Every hotlinked photo has a JavaScript fallback (`js/main.js`): if the
Commons URL ever 404s or the file is renamed, the frame automatically
reverts to the same dashed-placeholder look with its caption text, instead
of showing a broken-image icon.

## Product Atlas photography (100 additional images)

The 100 product pages under `products/` each carry their own hotlinked
Commons photograph using the same mechanism described above. Because that
set is a full order of magnitude larger than the seven photos catalogued
here, its sourcing notes, and — importantly — which of those 100 are
confirmed exact matches versus honestly-labelled "representative"
photographs, are kept in **`PRODUCT-ATLAS-METHODOLOGY.md`** rather than
duplicated in this file. Read that file before using the Product Atlas
publicly.
