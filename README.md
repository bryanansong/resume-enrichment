# Resume Enrichment

A script that embeds invisible, ATS-readable keyword text into your resume PDFs — without visually changing how they look.

## How It Works

Many Applicant Tracking Systems (ATS) parse raw PDF text to score resumes for keyword relevance. This tool inserts a hidden block of text (white color, microscopic font size) into your PDF. The text is invisible to human readers but is picked up by ATS scanners, effectively boosting your resume's keyword match score.

**Workflow:**
1. You drop your resume PDF(s) into `drop-resume-here/`
2. You edit `keywords.txt` with the text you want embedded
3. You run the script
4. Enriched PDFs are saved to `resulting-resume/`

---

## Setup & Usage (2 options)

### Option A — With `uv`

```bash
# Install dependencies
uv pip install pymupdf

# Run the script
uv run main.py
```

### Option B — Standard Python (pip + venv)

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pymupdf

# Run the script
python main.py
```

---

## Customisation

| File / Constant | Purpose |
|---|---|
| `keywords.txt` | The hidden text embedded in every PDF. Edit this with relevant skills, buzzwords, or project descriptions. |
| `drop-resume-here/` | Place your input PDF resume(s) here. |
| `resulting-resume/` | Output directory — processed PDFs are saved here automatically. |
| `INSERT_X / INSERT_Y` | Pixel coordinates (in points) for where the hidden text is placed on the page. |
| `PAGE_INDEX` | Which page to embed the text on (0 = first page). |

---

## Requirements

- Python ≥ 3.12
- [`PyMuPDF`](https://pymupdf.readthedocs.io/) (`fitz`)
