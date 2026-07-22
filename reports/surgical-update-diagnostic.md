# Surgical visual and editorial update

## Baseline

The auditable published package was preserved in Git commit `fcff27d` before any modification.

## Diagnosis and decisions

### Logo

The source geometry was sound, but the SVG canvas had no deliberate safety area and the HTML intrinsic dimensions did not match the SVG aspect ratio. Header and footer relied only on CSS width, creating inconsistent reserved boxes and exposing the symbol to apparent clipping during responsive scaling and initial rendering.

The paths, stroke width and colour were preserved exactly. The SVG canvas was expanded from `0 0 220 70` to `-6 -6 232 82`, and matching intrinsic dimensions plus explicit aspect-ratio and `object-fit: contain` were applied in both placements.

### Founder photograph

The original photograph was retained unchanged as the source asset. A restrained CSS treatment was selected instead of destructive background replacement: reduced saturation, modest contrast control, a deep-navy/mineral frame, a subtle tonal overlay and precise object positioning. This harmonises the busy exhibition background with the brand while preserving the person, avoiding segmentation halos and keeping the original available as the production source and backup.

### Home length

The Home was strategically complete but rhythmically overextended at 14 sections and approximately 1,370–1,415 words depending on language. Two blocks repeated information already established elsewhere:

- “Operational outcomes” restated the consequences of the three service sections and the methodology.
- “International delivery” was valuable but did not require a separate full-height section after the experience metrics.

The outcomes block was removed. International delivery was merged into the experience section. All mandatory proof, services, industries, founder content, international reach, engagement models, contact path and financial-services disclaimer remain.

The revised Home contains 12 sections. The intervention shortens the journey without turning the page into a thin brochure and improves layered scanning on mobile.

## Subsequent correction — 2026-07-22

A later review established that the supplied logo geometry itself differed from the first reconstructed SVG. The final resource is documented in `reports/logo-final-fix.md`. The visible preliminary legal-review banners were also removed from all six legal pages at the owner's request; the legal substance and registered address were not changed.
