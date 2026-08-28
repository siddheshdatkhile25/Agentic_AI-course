from pathlib import Path
from pypdf import PdfReader
from config import SAMPLE_CANDIDATE_PATHS, DEFAULT_SAMPLE_REPORT


def load_sample_report() -> str:
    """Reads the default sample blood_work.txt file across candidate paths."""
    for path in SAMPLE_CANDIDATE_PATHS:
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        return content
            except Exception:
                pass
    return DEFAULT_SAMPLE_REPORT.strip()


def extract_text_from_pdf(uploaded_file) -> str:
    """Extracts text content from an uploaded PDF file."""
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text.strip()
    except Exception as e:
        return ""

