# Cirta Capital website

Static website designed for GitHub + Cloudflare Pages. No build step, framework, server, database or external font service is required.

## Cloudflare Pages settings
- Framework preset: **None**
- Build command: leave blank
- Build output directory: `/` when this folder is the repository root
- Root directory: leave blank

Upload every file and the `assets` folder to the repository root. The site entry point is `index.html`.

## Domain
Set `cirtacapital.com` as the custom domain in Cloudflare Pages. Ensure the DNS record points to the Pages project and remove conflicting old A/AAAA/CNAME records.
