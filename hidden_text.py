#!/usr/bin/env python3
"""
Insert invisible (opacity=0) searchable text into all PDFs in a directory.

Usage:
  - Place your PDFs in the `drop-resume-here` directory.
  - Run this script. It will process all PDFs and save them to the `resulting-resume` directory.
  - Edit constants below to adjust behavior (e.g., coordinates, font size).
"""

import fitz  # PyMuPDF

# ------------------ CONFIG CONSTANTS ------------------

import os
import glob

INPUT_DIR = "drop-resume-here"     # Directory containing input PDFs
OUTPUT_DIR = "resulting-resume"    # Directory for final modified PDFs

PAGE_INDEX = 0              # Page number (0-based index)

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

def process_pdf(pdf_path, text):
    doc = fitz.open(pdf_path)
    if len(doc) <= PAGE_INDEX:
        print(f"Skipping {pdf_path}: doesn't have page index {PAGE_INDEX}")
        return
    page = doc[PAGE_INDEX]
    
    insert_invisible_text(page, INSERT_X, INSERT_Y, text, fontsize=FONT_SIZE)
    
    filename = os.path.basename(pdf_path)
    output_pdf = os.path.join(OUTPUT_DIR, filename)
    
    doc.save(output_pdf)
    print(f"Saved modified PDF for '{filename}' as '{output_pdf}'")

if __name__ == "__main__":
    if not os.path.exists(INPUT_DIR):
        print(f"Directory '{INPUT_DIR}' not found. Please create it and add PDFs.")
    else:
        pdf_files = glob.glob(os.path.join(INPUT_DIR, "*.pdf"))
        
        if not pdf_files:
            print(f"No PDFs found in directory: {INPUT_DIR}")
        else:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            print(f"Found {len(pdf_files)} PDF(s) to process.")
            text = PLACEHOLDER_TEXT
            for pdf_path in pdf_files:
                print(f"Processing '{pdf_path}'...")
                try:
                    process_pdf(pdf_path, text)
                except Exception as e:
                    print(f"Error processing {pdf_path}: {e}")
