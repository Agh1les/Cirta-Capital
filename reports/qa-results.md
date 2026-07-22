# QA results — final logo and legal notice correction

Date: 2026-07-22

## Scope

This pass was performed on top of commit `ef2f3ed`, without reverting to an earlier site version.

Changes covered:

- replacement of the inaccurate three-arch logo reconstruction with a technically clean SVG matching the supplied complete symbol;
- correction of intrinsic logo dimensions and responsive sizing in header and footer;
- replacement of the browser favicon with a cache-busted, correctly oriented version of the same symbol;
- removal of the visible preliminary legal-review banner from Privacy Policy and Terms of Use in English, French and Spanish;
- preservation of the current founder portrait treatment after visual review.

## Logo findings and correction

The previous SVG did not match the supplied master symbol. It used three complete arches, while the supplied mark contains one full left arch, one smaller central arch and two separated sides of the larger outer form. The issue was therefore not only container clipping: the underlying vector reconstruction was geometrically wrong.

The corrected `logo-symbol.svg`:

- uses the supplied geometry and orientation;
- has a safe `viewBox` of `0 0 112 44`;
- contains no masks, clipping paths, transforms or hidden overflow;
- preserves round line caps, line joins and the established brass colour;
- has matching intrinsic HTML dimensions of 112 × 44;
- uses `object-fit: contain` and a consistent aspect ratio in header and footer.

The favicon now uses a new filename, `favicon-v2.svg`, to avoid Chrome continuing to display a cached previous icon. It uses the same orientation as the main logo.

## Founder portrait decision

The existing navy/mineral presentation was retained. A white background would make the portrait feel more like an isolated cut-out, reduce integration with the dark premium visual system and increase the visibility of any edge imperfections around hair and clothing. The current restrained frame provides better brand continuity and visual authority without altering the person.

## Legal pages

The visible preliminary legal-review alert was removed from:

- `docs/en/privacy.html`
- `docs/en/terms.html`
- `docs/fr/privacy.html`
- `docs/fr/terms.html`
- `docs/es/privacy.html`
- `docs/es/terms.html`

No corporate address, privacy substance, terms, footer disclaimer or contact detail was changed.

## Automated validation

Command executed:

```bash
python scripts/validate_site.py
```

Result:

- 11 HTML files validated;
- 0 errors;
- 0 warnings;
- no unresolved address placeholders;
- confirmed registered address remains restricted to the six legal pages;
- no `LocalBusiness` structured data;
- no missing internal assets or broken internal references detected by the validator.

## Resource checks

- every HTML logo reference resolves to `assets/img/logo-symbol.svg`;
- every favicon reference resolves to `assets/img/favicon-v2.svg`;
- the web manifest points to the new favicon resource;
- no old legal-alert wording remains in the published HTML;
- the original pre-fix logo and favicon files are preserved under `docs/assets/img/originals/`.

## Manual checks still required after deployment

Because this environment cannot push to the connected GitHub/Cloudflare deployment, the following must be checked after publishing with a hard refresh or empty cache:

- Chrome tab icon, especially after closing and reopening the tab;
- header and footer logo at mobile and desktop widths;
- Safari/WebKit and Firefox rendering;
- all three language routes in production.

