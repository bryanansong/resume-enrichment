#!/usr/bin/env python3
"""
Insert and update invisible (opacity=0) searchable text in a PDF using PyMuPDF.

Usage:
  - Set INIT_MODE = True to insert a new placeholder.
  - Set UPDATE_MODE = True to replace old hidden text with new hidden text.
  - Edit constants below to adjust behavior.
"""

import fitz  # PyMuPDF

# ------------------ CONFIG CONSTANTS ------------------

INIT_MODE = True      # True = insert a hidden placeholder

INPUT_PDF = "data/input.pdf"     # Path to input PDF
OUTPUT_PDF = "output.pdf"   # Path to output PDF after modification

PAGE_INDEX = 0              # Page number (0-based index)

# For INIT_MODE
def load_keywords():
    """Load keywords from keywords.txt file."""
    try:
        with open("keywords.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Warning: keywords.txt not found, using empty string")
        return ""

PLACEHOLDER_TEXT = load_keywords()  # Text to insert once as placeholder
INSERT_X = 35.0                 # X coordinate (points) for insertion
INSERT_Y = 200.0                 # Y coordinate (baseline, points)
FONT_SIZE = 0.001                  # Font size in points (tiny, invisible)


# ------------------ FUNCTIONS ------------------

def insert_invisible_text(page, x, y, text, fontsize=0.1):
    """Insert invisible (0 fill-opacity) text at (x,y)."""
    shape = page.new_shape()
    shape.insert_text((x, y), text, fontsize=fontsize, color=(1, 1, 1))
    shape.finish()
    shape.commit()


# ------------------ MAIN ------------------

doc = fitz.open(INPUT_PDF)
page = doc[PAGE_INDEX]

insert_invisible_text(page, INSERT_X, INSERT_Y, PLACEHOLDER_TEXT, fontsize=FONT_SIZE)
print(f"Inserted placeholder '{PLACEHOLDER_TEXT}' on page {PAGE_INDEX}")

doc.save(OUTPUT_PDF)
print(f"Saved modified PDF as {OUTPUT_PDF}")
