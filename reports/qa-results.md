# Cirta Capital — Final QA Results

**Review date:** 22 July 2026  
**Source baseline:** exclusively the latest audited delivery, `cirta-capital-site-final.zip`. No earlier implementation was used.  
**Scope:** confirmed corporate email, legal and postal address, multilingual legal pages, address-placement controls, static-site validation, responsive browser checks and production-domain review.

## Confirmed information incorporated

- Corporate email: `contact@cirtacapital.com` — confirmed operational and monitored by the owner.
- Legal entity: Cirta Capital LLC.
- Registered and mailing address: confirmed exactly as supplied by the owner and incorporated only in the published legal pages.
- The address is described only as a legal and postal correspondence address.
- Every language states that Cirta Capital operates internationally and that the address is not a public-facing office.
- No residential address, Florida provider address, `c/o`, PMB or unconfirmed mailbox information has been added.

## Multilingual legal verification

| Language | Privacy Policy | Legal Notice section in Terms | Required label | Non-public-office notice |
|---|---:|---:|---:|---:|
| English | Pass | Pass | Pass | Pass |
| French | Pass | Pass | Pass | Pass |
| Spanish | Pass | Pass | Pass | Pass |

The preliminary legal-review warning remains visible in all six legal pages. Professional legal review is **still pending** and has not been marked as completed.

## Address placement audit

Within the published `docs/` output, the street address appears only in these six files:

- `docs/en/privacy.html`
- `docs/en/terms.html`
- `docs/fr/privacy.html`
- `docs/fr/terms.html`
- `docs/es/privacy.html`
- `docs/es/terms.html`

Confirmed absent from:

- all three home pages and hero sections;
- the global footer;
- page titles, descriptions, Open Graph and other metadata;
- JSON-LD and other structured data;
- `LocalBusiness` structured data;
- sitemap, robots, manifest and CNAME;
- maps, visit buttons, opening hours or operational-location claims.

No unresolved address marker remains in the website or documentation.

## Automated validation

- `python3 scripts/validate_site.py`: **passed with 0 warnings**
- HTML files checked: **11**
- Internal links, local assets and section anchors: **passed**
- Duplicate IDs and heading structure: **passed**
- SEO metadata, canonical URLs and `hreflang`: **passed**
- Contact form fields and static-site disclosure: **passed**
- Financial-services disclaimer in all three languages: **passed**
- Legal-address presence, localisation and permitted scope: **passed**
- Address absence from head, footer and structured data: **passed**
- Address placeholders: **none unresolved**
- `LocalBusiness` structured data: **none**
- Sitemap, robots, CNAME, manifest and Pages workflow: **passed**
- Third-party analytics and advertising trackers: **none detected**
- JavaScript syntax (`node --check docs/assets/js/main.js`): **passed**

## Browser and responsive tests

Chromium tests were rerun against a local HTTP build at **1440 px** and **390 px** widths.

| Area | English | French | Spanish |
|---|---:|---:|---:|
| Home page desktop rendering | Pass | Pass | Pass |
| Home page mobile rendering | Pass | Pass | Pass |
| Privacy page desktop and mobile | Pass | Pass | Pass |
| Terms / Legal Notice page desktop and mobile | Pass | Pass | Pass |
| Address copy and labels | Pass | Pass | Pass |
| Horizontal overflow | None | None | None |
| Console errors | None | None | None |
| Page JavaScript errors | None | None | None |
| Missing resources / HTTP 404s | None | None | None |
| Mobile menu open / close | Pass | Pass | Pass |
| Escape key closes menu | Pass | Pass | Pass |
| Focus returns to menu control | Pass | Pass | Pass |
| Eight required form-field checks | Pass | Pass | Pass |
| Localised validation status | Pass | Pass | Pass |

All 11 HTML documents were loaded in both viewports: **22 successful browser-page checks**, with no missing assets, console errors, JavaScript exceptions or horizontal overflow.

## Production-domain review

- `https://cirtacapital.com/` is reachable over HTTPS.
- DNS is resolving and the domain is publicly accessible.
- At the time of this review, the public domain is serving a previous site implementation, not the latest audited package used for this update.
- The public version currently uses an older root-page structure and older legal routes/content. Therefore this updated package must be deployed through the active GitHub/Cloudflare publication path before the changes in this report are considered live.
- After deployment, production should be checked specifically at `/en/`, `/fr/`, `/es/` and the six legal-page URLs contained in the package.

## Legal status

The legal pages are proportionate preliminary drafts for a static informational website without analytics, advertising pixels or non-essential cookies. They contain no obvious operational-location claim, financial-services implication or false server-side form representation. Nevertheless, they remain preliminary documents and must be reviewed by a qualified legal professional before being treated as final legal advice or a definitive compliance position.

## Remaining launch control

1. Deploy this updated package so that it replaces the previous public implementation.
2. Confirm the deployment workflow completes successfully.
3. Recheck the public multilingual and legal URLs after cache propagation.
4. Obtain professional legal review; this item remains open.

## Files modified from the audited baseline

1. `docs/en/privacy.html`
2. `docs/en/terms.html`
3. `docs/fr/privacy.html`
4. `docs/fr/terms.html`
5. `docs/es/privacy.html`
6. `docs/es/terms.html`
7. `scripts/validate_site.py`
8. `reports/qa-results.md`
9. `reports/launch-checklist.md`
10. `reports/strategy-and-validation.md`
11. `README.md`

No image, stylesheet, JavaScript, workflow, metadata, structured-data, sitemap, robots, manifest, CNAME or home-page content file was modified.
