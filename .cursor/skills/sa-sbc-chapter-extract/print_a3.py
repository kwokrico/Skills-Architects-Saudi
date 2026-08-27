"""Print a finalized SBC extract Markdown file to Landscape A3 PDF.

Chrome prints. Playwright only issues the print. markdown2 builds the HTML.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import markdown2
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

CSS_NAME = "print-a3-landscape.css"
MARKDOWN_EXTRAS = ["tables", "fenced-code-blocks", "header-ids", "strike"]
CHROME_MISSING = (
    "Installed Google Chrome was not found (Playwright channel='chrome'). "
    "Install Chrome and retry. Do not use Edge CLI or gstack make-pdf."
)
HEADER_TMPL = (
    '<div style="font-size:8px; color:#333; width:100%; padding:0 12mm; '
    'font-family:Segoe UI, Arial, sans-serif;">'
    "<span>{title}</span></div>"
)
FOOTER_TMPL = (
    '<div style="font-size:8px; color:#333; width:100%; padding:0 12mm; '
    "font-family:Segoe UI, Arial, sans-serif; display:flex; "
    'justify-content:space-between;">'
    "<span>Source-only advisory matrix — not a stamped compliance document</span>"
    '<span><span class="pageNumber"></span> / '
    '<span class="totalPages"></span> · A3 landscape</span></div>'
)


def wrap_document(title: str, body: str, css: str) -> str:
    return (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<title>{html.escape(title)}</title><style>{css}</style></head>"
        f"<body>{body}</body></html>"
    )


def print_pdf(md_path: Path) -> Path:
    css_path = Path(__file__).with_name(CSS_NAME)
    css = css_path.read_text(encoding="utf-8")
    markdown = md_path.read_text(encoding="utf-8")
    if re.search(r"^## Appendix A\b", markdown, flags=re.M):
        raise ValueError(f"{md_path.name} still contains Appendix A. Finalize the MD first.")
    pdf_path = md_path.with_suffix(".pdf")
    html_path = md_path.with_suffix(".print.html")
    body = markdown2.markdown(markdown, extras=MARKDOWN_EXTRAS)
    html_path.write_text(wrap_document(md_path.stem, body, css), encoding="utf-8")
    try:
        with sync_playwright() as playwright:
            try:
                browser = playwright.chromium.launch(channel="chrome", headless=True)
            except PlaywrightError as exc:
                raise RuntimeError(CHROME_MISSING) from exc
            page = browser.new_page()
            page.emulate_media(media="print")
            page.goto(html_path.resolve().as_uri(), wait_until="load")
            page.pdf(
                path=str(pdf_path.resolve()),
                format="A3",
                landscape=True,
                print_background=True,
                margin={
                    "top": "12mm",
                    "bottom": "14mm",
                    "left": "8mm",
                    "right": "8mm",
                },
                display_header_footer=True,
                header_template=HEADER_TMPL.format(title=html.escape(md_path.stem)),
                footer_template=FOOTER_TMPL,
            )
            browser.close()
    finally:
        html_path.unlink(missing_ok=True)
    if not pdf_path.is_file() or pdf_path.stat().st_size < 1000:
        raise RuntimeError(f"PDF print produced no usable file: {pdf_path}")
    return pdf_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Print SBC extract MD to Landscape A3 PDF.")
    parser.add_argument("markdown", type=Path, help="Finalized extract .md path")
    args = parser.parse_args()
    md_path = args.markdown.resolve()
    if not md_path.is_file():
        print(f"Missing file: {md_path}", file=sys.stderr)
        return 1
    try:
        pdf_path = print_pdf(md_path)
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
