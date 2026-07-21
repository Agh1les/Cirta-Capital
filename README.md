# Cirta Capital website v2

Recommended deployment: GitHub private repository connected to Cloudflare Pages.

Why Git now:
- version history and backups;
- automatic deployment when changes are approved;
- easy rollback;
- no lock-in to a designer or local computer.

Cloudflare Pages setup:
1. Create a private GitHub repository named `cirta-capital-website`.
2. Upload all files in this folder to the repository root.
3. Cloudflare → Workers & Pages → Create → Pages → Connect to Git.
4. Select the repository.
5. Framework preset: None.
6. Build command: leave blank.
7. Build output directory: `/` or leave the default root option accepted by the wizard.
8. Deploy.
9. Add custom domains `cirtacapital.com` and `www.cirtacapital.com`.

Do not delete Zoho MX, SPF, DKIM or DMARC records.
