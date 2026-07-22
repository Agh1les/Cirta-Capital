#!/usr/bin/env python3
"""Dependency-free validation for the static Cirta Capital site."""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ERRORS: list[str] = []
WARNINGS: list[str] = []

REGISTERED_ADDRESS = "30 N Gould St " + "Ste R"
LEGAL_ADDRESS_PAGES = {
    Path("en/privacy.html"),
    Path("en/terms.html"),
    Path("fr/privacy.html"),
    Path("fr/terms.html"),
    Path("es/privacy.html"),
    Path("es/terms.html"),
}
LEGAL_COPY = {
    "en": {
        "label": "Registered and mailing address:",
        "notice": "Cirta Capital LLC operates internationally. This address is used for legal and postal correspondence and is not a public-facing office.",
    },
    "fr": {
        "label": "Adresse légale et postale :",
        "notice": "Cirta Capital LLC exerce ses activités à l’international. Cette adresse est utilisée pour la correspondance légale et postale et ne constitue pas un bureau ouvert au public.",
    },
    "es": {
        "label": "Dirección registral y postal:",
        "notice": "Cirta Capital LLC opera internacionalmente. Esta dirección se utiliza para correspondencia legal y postal y no es una oficina abierta al público.",
    },
}


def error(message: str) -> None:
    ERRORS.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.title_parts: list[str] = []
        self.in_title = False
        self.ids: list[str] = []
        self.headings: list[int] = []
        self.links: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.meta: list[dict[str, str]] = []
        self.link_tags: list[dict[str, str]] = []
        self.forms: list[dict[str, str]] = []
        self.form_fields: list[dict[str, str]] = []
        self._form_depth = 0
        self.text_parts: list[str] = []

    @staticmethod
    def attrs_dict(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key: value or "" for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = self.attrs_dict(attrs)
        if tag == "html":
            self.html_lang = data.get("lang", "")
        if tag == "title":
            self.in_title = True
        if "id" in data:
            self.ids.append(data["id"])
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "a" and data.get("href"):
            self.links.append(("href", data["href"]))
        elif tag == "link":
            self.link_tags.append(data)
            if data.get("href"):
                self.links.append(("href", data["href"]))
        elif tag == "script" and data.get("src"):
            self.links.append(("src", data["src"]))
        elif tag == "img":
            self.images.append(data)
            if data.get("src"):
                self.links.append(("src", data["src"]))
        elif tag == "meta":
            self.meta.append(data)
        elif tag == "form":
            self.forms.append(data)
            self._form_depth += 1
        elif tag in {"input", "select", "textarea"} and self._form_depth:
            self.form_fields.append(data)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag == "form" and self._form_depth:
            self._form_depth -= 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "form" and self._form_depth:
            self._form_depth -= 1

    def handle_data(self, data: str) -> None:
        clean = " ".join(data.split())
        if clean:
            self.text_parts.append(clean)
            if self.in_title:
                self.title_parts.append(clean)

    @property
    def title(self) -> str:
        return " ".join(self.title_parts).strip()

    @property
    def text(self) -> str:
        return " ".join(self.text_parts)

    def has_meta(self, *, name: str | None = None, property_: str | None = None) -> bool:
        for item in self.meta:
            if name is not None and item.get("name") == name:
                return True
            if property_ is not None and item.get("property") == property_:
                return True
        return False

    def meta_content(self, *, name: str | None = None, property_: str | None = None) -> str:
        for item in self.meta:
            if name is not None and item.get("name") == name:
                return item.get("content", "")
            if property_ is not None and item.get("property") == property_:
                return item.get("content", "")
        return ""


def parse_page(page: Path) -> tuple[PageParser, str]:
    text = page.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(text)
    parser.close()
    return parser, text


def local_target(page: Path, href: str) -> tuple[Path, str | None] | None:
    if not href or href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https"}:
        return None
    fragment = parsed.fragment or None
    path = parsed.path
    if not path:
        target = page
    elif path.startswith("/"):
        target = DOCS / path.lstrip("/")
    else:
        target = (page.parent / path).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target, fragment


def target_has_id(target: Path, fragment: str) -> bool:
    parser, _ = parse_page(target)
    return fragment in parser.ids


def validate_html(page: Path) -> None:
    parser, source = parse_page(page)
    rel = page.relative_to(ROOT)

    if not parser.html_lang:
        error(f"{rel}: missing html lang")
    if not parser.title:
        error(f"{rel}: missing title")
    if page.name != "404.html" and not parser.meta_content(name="description").strip():
        error(f"{rel}: missing meta description")

    duplicates = [item for item, count in Counter(parser.ids).items() if count > 1]
    if duplicates:
        error(f"{rel}: duplicate IDs {duplicates}")

    if parser.headings and parser.headings.count(1) != 1:
        error(f"{rel}: expected one h1, found {parser.headings.count(1)}")
    for previous, current in zip(parser.headings, parser.headings[1:]):
        if current > previous + 1:
            warn(f"{rel}: heading level jumps h{previous} to h{current}")

    for image in parser.images:
        if "alt" not in image:
            error(f"{rel}: image without alt: {image.get('src', '(unknown)')}")

    for _, value in parser.links:
        target_info = local_target(page, value)
        if not target_info:
            continue
        target, fragment = target_info
        try:
            target.relative_to(ROOT)
        except ValueError:
            error(f"{rel}: link escapes repository: {value}")
            continue
        if not target.exists():
            error(f"{rel}: missing internal target {value} -> {target.relative_to(ROOT)}")
            continue
        if fragment and target.suffix.lower() in {".html", ""} and not target_has_id(target, fragment):
            error(f"{rel}: missing anchor #{fragment} in {target.relative_to(ROOT)}")

    is_language_home = page.name == "index.html" and page.parent.name in {"en", "fr", "es"}
    if is_language_home:
        lang = page.parent.name
        required = [
            ("canonical", any(link.get("rel") == "canonical" for link in parser.link_tags)),
            ("og:title", parser.has_meta(property_="og:title")),
            ("og:description", parser.has_meta(property_="og:description")),
            ("og:image", parser.has_meta(property_="og:image")),
            ("twitter:card", parser.has_meta(name="twitter:card")),
        ]
        for label, present in required:
            if not present:
                error(f"{rel}: missing SEO element {label}")

        alternates = {link.get("hreflang") for link in parser.link_tags if link.get("rel") == "alternate"}
        if not {"en", "fr", "es", "x-default"}.issubset(alternates):
            error(f"{rel}: incomplete hreflang set {alternates}")

        form = next((item for item in parser.forms if "data-mailto-form" in item), None)
        if not form:
            error(f"{rel}: missing static contact form")
        else:
            names = {field.get("name") for field in parser.form_fields}
            expected = {"fullName", "company", "email", "country", "need", "stage", "urgency", "situation"}
            if not expected.issubset(names):
                error(f"{rel}: form fields missing {sorted(expected - names)}")

        normalized = parser.text.lower()
        disclosures = {
            "en": "does not transmit data to a server",
            "fr": "ne transmet aucune donnée à un serveur",
            "es": "no transmite datos a un servidor",
        }
        if disclosures[lang] not in normalized:
            error(f"{rel}: static-form disclosure missing")

        notices = {
            "en": "does not provide investment, banking or financial advisory services",
            "fr": "ne fournit aucun service d’investissement",
            "es": "no presta servicios de inversión",
        }
        if notices[lang] not in normalized:
            error(f"{rel}: non-financial-services notice missing")

    disallowed = ["googletagmanager", "google-analytics", "facebook.net", "hubspot", "hotjar", "doubleclick"]
    source_lower = source.lower()
    for token in disallowed:
        if token in source_lower:
            error(f"{rel}: disallowed tracker reference: {token}")


def validate_legal_address_scope() -> None:
    address_occurrences: set[Path] = set()
    placeholder_patterns = [
        "[" + "Insert",
        "[" + "Insérer",
        "[" + "Insertar",
        "registered office address after " + "legal review",
        "adresse du siège après " + "validation juridique",
        "domicilio social tras la " + "revisión legal",
    ]

    for page in sorted(DOCS.rglob("*.html")):
        rel_docs = page.relative_to(DOCS)
        parser, source = parse_page(page)
        if REGISTERED_ADDRESS in source:
            address_occurrences.add(rel_docs)
            if rel_docs not in LEGAL_ADDRESS_PAGES:
                error(f"{rel_docs}: registered address appears outside approved legal pages")

            head = source.split("</head>", 1)[0]
            footer = source.split("<footer", 1)[1] if "<footer" in source else ""
            if REGISTERED_ADDRESS in head:
                error(f"{rel_docs}: registered address appears in metadata/head")
            if REGISTERED_ADDRESS in footer:
                error(f"{rel_docs}: registered address appears in global footer")
            if re.search(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>.*?' + re.escape(REGISTERED_ADDRESS), source, re.I | re.S):
                error(f"{rel_docs}: registered address appears in structured data")

        for token in placeholder_patterns:
            if token.lower() in source.lower():
                error(f"{rel_docs}: unresolved address placeholder: {token}")

        if "LocalBusiness" in source:
            error(f"{rel_docs}: LocalBusiness structured data is not permitted")

        if rel_docs in LEGAL_ADDRESS_PAGES:
            lang = rel_docs.parts[0]
            expected = LEGAL_COPY[lang]
            normalized = parser.text
            if REGISTERED_ADDRESS not in source:
                error(f"{rel_docs}: confirmed registered address missing")
            if expected["label"] not in normalized:
                error(f"{rel_docs}: localized address label missing")
            if expected["notice"] not in normalized:
                error(f"{rel_docs}: localized non-public-office notice missing")

    missing_pages = LEGAL_ADDRESS_PAGES - address_occurrences
    if missing_pages:
        error(f"Confirmed registered address missing from legal pages: {sorted(str(p) for p in missing_pages)}")
    extra_pages = address_occurrences - LEGAL_ADDRESS_PAGES
    if extra_pages:
        error(f"Confirmed registered address found outside legal pages: {sorted(str(p) for p in extra_pages)}")

    text_extensions = {".html", ".md", ".txt", ".xml", ".json", ".yml", ".yaml", ".js", ".css", ".py"}
    for item in ROOT.rglob("*"):
        if not item.is_file() or item.suffix.lower() not in text_extensions:
            continue
        content = item.read_text(encoding="utf-8", errors="replace")
        for token in placeholder_patterns:
            if token.lower() in content.lower():
                error(f"{item.relative_to(ROOT)}: unresolved address placeholder remains in package")


def validate_support_files() -> None:
    required = [
        DOCS / "404.html",
        DOCS / "robots.txt",
        DOCS / "sitemap.xml",
        DOCS / "site.webmanifest",
        DOCS / "CNAME",
        DOCS / ".nojekyll",
        ROOT / ".github/workflows/pages.yml",
    ]
    for item in required:
        if not item.exists():
            error(f"Missing required file: {item.relative_to(ROOT)}")

    try:
        manifest = json.loads((DOCS / "site.webmanifest").read_text(encoding="utf-8"))
        if not manifest.get("name") or not manifest.get("icons"):
            error("site.webmanifest is incomplete")
    except Exception as exc:
        error(f"Invalid site.webmanifest: {exc}")

    try:
        ET.parse(DOCS / "sitemap.xml")
    except Exception as exc:
        error(f"Invalid sitemap.xml: {exc}")

    robots = (DOCS / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://cirtacapital.com/sitemap.xml" not in robots:
        error("robots.txt does not advertise the production sitemap")

    if (DOCS / "CNAME").read_text(encoding="utf-8").strip() != "cirtacapital.com":
        error("CNAME does not match cirtacapital.com")

    workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    for token in ["actions/checkout@", "actions/configure-pages@", "actions/upload-pages-artifact@", "actions/deploy-pages@"]:
        if token not in workflow:
            error(f"Workflow missing {token}")


def main() -> int:
    pages = sorted(DOCS.rglob("*.html"))
    for page in pages:
        validate_html(page)
    validate_legal_address_scope()
    validate_support_files()

    print(f"Validated {len(pages)} HTML files.")
    for message in WARNINGS:
        print(f"WARNING: {message}")
    for message in ERRORS:
        print(f"ERROR: {message}")
    if ERRORS:
        print(f"Validation failed with {len(ERRORS)} error(s) and {len(WARNINGS)} warning(s).")
        return 1
    print(f"Validation passed with {len(WARNINGS)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
