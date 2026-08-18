# Photo credits

Four image slots use real, freely-licensed photographs hotlinked from Wikimedia
Commons (via `Special:FilePath`, which redirects to the current file at the
requested width — no image files are copied into this repository). The
remaining image slots (`.img-slot`) are still honest dashed placeholders,
because a search for a confidently-matching, unambiguous, adult-appropriate
photograph did not turn up a good result for that specific scene (an SHG
meeting in progress, a federation governance meeting, a packaged-water
production line, or a CSR site visit) — see "What's still a placeholder"
below.

**Important caveat:** these were selected by searching Wikimedia Commons for
files with clear, self-describing titles (e.g. `Khariya Tribal lady from
Jharkhand.jpg`), because the environment this site was built in could not
load the actual image bytes to visually confirm content before publishing.
**Before launch, open each page and confirm every photograph looks right and
fits the tone of the page it's on** — swap the `src` (and the matching
`photo-credit` link) on any that don't by editing the `<img>` tag directly;
no build step is required.

| Page | Section | File | Commons page | Likely license |
|---|---|---|---|---|
| `index.html` | Hero | `Khariya Tribal lady from Jharkhand.jpg` | https://commons.wikimedia.org/wiki/File:Khariya_Tribal_lady_from_Jharkhand.jpg | Free license (Commons-hosted); confirm exact tag on file page |
| `about.html` | The problem | `Santal people Jharkhand India.jpg` | https://commons.wikimedia.org/wiki/File:Santal_people_Jharkhand_India.jpg | Free license (Commons-hosted); confirm exact tag on file page |
| `programmes.html` | Women's enterprise | `Weaving of Sambalpuri sari.jpg` | https://commons.wikimedia.org/wiki/File:Weaving_of_Sambalpuri_sari.jpg | Free license (Commons-hosted); confirm exact tag on file page |
| `programmes.html` | Rural manufacturing | `Sambalpuri Ikat weaving loom (Tanta) from Odisha.jpg` | https://commons.wikimedia.org/wiki/File:Sambalpuri_Ikat_weaving_loom_(Tanta)_from_Odisha.jpg | Free license (Commons-hosted); confirm exact tag on file page |

All content hosted on Wikimedia Commons is required to carry a free license
(public domain, CC0, CC-BY, or CC-BY-SA) — but the exact licence and the
photographer's name to credit varies file to file. **Before publishing,
open each Commons page above and copy the exact attribution line its licence
requires** (most CC-BY-SA files want "© [Photographer name], CC BY-SA
[version], via Wikimedia Commons"). Each photo already links out to its
Commons file page via the small "Wikimedia Commons ↗" tag in its
bottom-right corner, which covers the "link to the file page" part of
CC-BY-SA — add the photographer's name to that link text once confirmed if
your organisation's compliance standard requires a fuller credit.

## What's still a placeholder

- `programmes.html` — Leadership development, Community institutions
- `get-involved.html` — CSR collaboration
- Every `.img-slot` you see once these are replaced follows the same dashed,
  labelled convention — replace the `<div class="img-slot ...">` block with
  a `<div class="photo-frame ...">` block (copy the pattern used elsewhere in
  the same file) once a matching real photograph is available. Forcing a
  mismatched stock photo into these (e.g. a craft photo captioned as a board
  meeting) would misrepresent what's actually happening in it, so they were
  left honest instead.

## Resilience

Every hotlinked photo has a JavaScript fallback (`js/main.js`): if the
Commons URL ever 404s or the file is renamed, the frame automatically
reverts to the same dashed-placeholder look with its caption text, instead
of showing a broken-image icon.
