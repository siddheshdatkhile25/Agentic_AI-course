# 🤖 Agentic AI Course - Health & Blood Work Analysis

A modular, agentic AI-powered application that parses patient blood test reports, extracts and classifies lab biomarkers against reference intervals, and generates patient-friendly health summaries along with personalized Indian dietary recommendations.

---

## 🚀 Features

- **Multi-Input Support**:
  - 📄 **1-Click Sample Report**: Preloaded with a sample blood test report (`blood_work.txt`).
  - 📁 **File Upload**: Supports `.pdf` and `.txt` blood test reports.
  - ✏️ **Interactive Editor**: Direct text editing and real-time report modification.
- **Two-Stage Agentic LLM Pipeline**:
  - **Stage 1 (Medical Biomarker Extraction)**: Extracts all test names, values, units, reference intervals, and tags each as `HIGH` (🔴), `LOW` (🟡), or `NORMAL` (🟢).
  - **Stage 2 (Clinical Nutritionist)**: Generates a 4–5 line plain-language health summary and tailored Indian dietary recommendations (strictly split into *Foods to Avoid* and *Foods to Eat More Of*).
- **Interactive Streamlit Dashboard**:
  - Top biomarker metrics strip (Total, Normal, High, Low).
  - Filterable & searchable test biomarker table with color-coded status badges.
  - Formatted patient health summary and side-by-side diet recommendation cards.
  - 1-Click export to Markdown (`.md`) and CSV (`.csv`).
- **Modular Architecture**: Clean separation between configuration, utilities, LLM services, and UI components.

---

## 📁 Repository Structure

```text
.
├── pyproject.toml
├── README.md
├── .env.example
├── .gitignore
└── src/
    └── agentic_ai_course/
        ├── LLM_basic_calling/
        │   └── call_llm.ipynb
        └── Health_Analysis/
            ├── blood_work.txt
            ├── blood_work_analysis.ipynb
            └── Streamlit_app/
                ├── app.py                     # Main application entrypoint
                ├── config.py                  # Prompts, constants, models & styles
                ├── services/
                │   ├── __init__.py
                │   ├── llm_service.py         # ChatGroq client & stage executions
                │   └── parser_service.py      # Biomarker table & diet section parsers
                ├── utils/
                │   ├── __init__.py
                │   └── file_utils.py          # Sample loader & PDF text extractor
                └── ui/
                    ├── __init__.py
                    ├── sidebar.py             # Model selection & disclaimer
                    ├── input_view.py          # Input tabs & editor view
                    └── dashboard_view.py      # Diagnostic dashboard & export options
```

---

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+
- A [Groq Cloud](https://console.groq.com/) API Key

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/siddheshdatkhile25/Agentic_AI-course.git
cd Agentic_AI-course
```

Install packages using `pip` or `uv`:

```bash
pip install -e .
# or
uv pip install -e .
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Add your Groq API key:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### 4. Running the Streamlit App

```bash
streamlit run src/agentic_ai_course/Health_Analysis/Streamlit_app/app.py
```

---

## ⚠️ Medical Disclaimer

This AI tool is designed for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a physician or qualified health provider.

