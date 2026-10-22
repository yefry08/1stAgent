#!/usr/bin/env python3
"""Render deck.html to AISDOM_Pitch_Deck.pdf (one 1280x720 slide per page).

Usage: python3 build_pdf.py
Requires: pip install playwright  (and a Chromium build; set
PLAYWRIGHT_BROWSERS_PATH or run `playwright install chromium`).
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SRC = HERE / "deck.html"
OUT = HERE / "AISDOM_Pitch_Deck.pdf"


def find_chromium():
    """Use a pre-installed Chromium if Playwright's own isn't downloaded."""
    root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for pattern in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome"):
        hits = sorted(root.glob(pattern))
        if hits:
            return str(hits[-1])
    return None


def main():
    with sync_playwright() as p:
        kwargs = {}
        try:
            browser = p.chromium.launch()
        except Exception:
            exe = find_chromium()
            if not exe:
                sys.exit("No Chromium found. Run: playwright install chromium")
            browser = p.chromium.launch(executable_path=exe)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(SRC.as_uri())
        page.wait_for_load_state("networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            width="1280px",
            height="720px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            prefer_css_page_size=False,
        )
        browser.close()
    print(f"Wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
