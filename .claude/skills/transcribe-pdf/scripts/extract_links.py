"""Extract hyperlink annotations from a PDF using PyMuPDF.

Usage: uv run --with pymupdf extract_links.py <pdf-path>

Outputs ready-to-paste markdown links grouped by page.
"""

import sys

import fitz  # PyMuPDF


def get_anchor_text(page, link_rect):
    """Find words that overlap with a link's bounding rectangle."""
    words = page.get_text("words")  # (x0, y0, x1, y1, word, block, line, word_no)
    matched = []
    for w in words:
        word_rect = fitz.Rect(w[:4])
        word_mid_y = (w[1] + w[3]) / 2
        if word_rect.intersects(link_rect) and link_rect.y0 <= word_mid_y <= link_rect.y1:
            matched.append((w[0], w[1], w[4]))  # x0, y0, text
    # Sort by position: top-to-bottom, then left-to-right
    matched.sort(key=lambda m: (m[1], m[0]))
    text = " ".join(m[2] for m in matched)
    return text.rstrip(".,;:!?)")


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_links.py <pdf-path>", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(sys.argv[1])
    for page in doc:
        links = [l for l in page.get_links() if l.get("uri")]
        if not links:
            continue
        print(f"=== Page {page.number + 1} ===")
        for link in links:
            uri = link["uri"]
            link_rect = fitz.Rect(link["from"])
            anchor = get_anchor_text(page, link_rect)
            if anchor:
                print(f"[{anchor}]({uri})")
            else:
                print(f"[]({uri})")
        print()

    doc.close()


if __name__ == "__main__":
    main()
