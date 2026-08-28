import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# Paths & Environment Setup
# -----------------------------------------------------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
HEALTH_DIR = CURRENT_DIR.parent
PROJECT_ROOT = HEALTH_DIR.parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
SAMPLE_REPORT_PATH = HEALTH_DIR / "blood_work.txt"

# Search paths for blood_work.txt
SAMPLE_CANDIDATE_PATHS = [
    SAMPLE_REPORT_PATH,
    HEALTH_DIR / "blood_work.txt",
    CURRENT_DIR / "blood_work.txt",
    Path("blood_work.txt"),
    PROJECT_ROOT / "src" / "agentic_ai_course" / "Health_Analysis" / "blood_work.txt",
]

# Load environment variables
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    load_dotenv()

# -----------------------------------------------------------------------------
# LLM Models & Settings
# -----------------------------------------------------------------------------
SUPPORTED_MODELS = [
    "openai/gpt-oss-120b",
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "deepseek-r1-distill-llama-70b",
    "gemma2-9b-it",
]

DEFAULT_MODEL = "openai/gpt-oss-120b"
DEFAULT_TEMPERATURE = 0.1

# -----------------------------------------------------------------------------
# Prompts
# -----------------------------------------------------------------------------
EXTRACTION_PROMPT_TEMPLATE = """
You are a medical data extraction assistant,

From the blood report below , extract ALL test values and classify each one as HIGH , LOW or NORMAL
based on the reference ranges provided in the report.

format the reponse as:
- Test Name: value | Status : HIGH/LOW/NORMAL | Reference: range

Blood Report:{blood_report}
"""

DIET_PROMPT_TEMPLATE = """
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the Blood work analysis below write:
1. A short health Summary in 4-5 lines explaining the Patient Condition in simple Language
2. A short, practical Indian diet plan having only the two section (1) Food to avoid (2) Food to eat more of,
    Do not include any other section in diet plan.

Blood work Analysis: {extracted_values}
"""

# -----------------------------------------------------------------------------
# Sample Fallback Report
# -----------------------------------------------------------------------------
DEFAULT_SAMPLE_REPORT = """Patient: Rajesh Sharma, Age 48, Male
Date: May 7, 2026

COMPLETE BLOOD COUNT (CBC)
--------------------------
Hemoglobin:        15.1 g/dL        (Normal: 13.5–17.5)
Hematocrit:        44%              (Normal: 41–53%)
WBC:               6.8 x10^3/uL     (Normal: 4.5–11.0)
Platelets:         220 x10^3/uL     (Normal: 150–400)

LIPID PANEL
-----------
Total Cholesterol: 238 mg/dL        (Normal: <200)
LDL Cholesterol:   162 mg/dL        (Normal: <100)
HDL Cholesterol:   36 mg/dL         (Normal: >40)
Triglycerides:     188 mg/dL        (Normal: <150)

METABOLIC PANEL
---------------
Glucose (Fasting): 92 mg/dL         (Normal: 70–99)
HbA1c:             5.3%             (Normal: <5.7%)
Creatinine:        1.0 mg/dL        (Normal: 0.7–1.3)
eGFR:              82 mL/min        (Normal: >60)

LIVER FUNCTION
--------------
ALT:               28 U/L           (Normal: 7–40)
AST:               25 U/L           (Normal: 10–40)
Bilirubin Total:   0.8 mg/dL        (Normal: 0.2–1.2)

Reviewing Physician: Dr. Priya Nair
"""

# -----------------------------------------------------------------------------
# Custom CSS Styling
# -----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
.main-header {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 0.2rem;
}
.sub-header {
    font-size: 1.05rem;
    color: #4B5563;
    margin-bottom: 1.5rem;
}
.status-badge-high {
    background-color: #FEE2E2;
    color: #991B1B;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
}
.status-badge-low {
    background-color: #FEF3C7;
    color: #92400E;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
}
.status-badge-normal {
    background-color: #DCFCE7;
    color: #166534;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
}
</style>
"""
