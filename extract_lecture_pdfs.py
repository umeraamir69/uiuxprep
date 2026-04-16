#!/usr/bin/env python3
"""Extract plain text from Lecture 1-15 PDFs into lectures_extracted/."""
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "lectures_extracted"
OUT.mkdir(exist_ok=True)


def main():
    for n in range(1, 16):
        pdf_path = ROOT / f"Lecture {n}.pdf"
        if not pdf_path.exists():
            print("Missing:", pdf_path)
            continue
        reader = PdfReader(str(pdf_path))
        parts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                parts.append(t)
        text = "\n\n".join(parts)
        out = OUT / f"lec{n:02d}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"{pdf_path.name} -> {out.name} ({len(text)} chars, {len(reader.pages)} pages)")


if __name__ == "__main__":
    main()
