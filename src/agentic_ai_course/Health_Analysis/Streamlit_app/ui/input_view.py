import streamlit as st
from utils.file_utils import load_sample_report, extract_text_from_pdf


def set_sample_report():
    """Callback to load sample blood report into editor."""
    sample_content = load_sample_report()
    st.session_state["report_editor"] = sample_content
    st.session_state["report_loaded_msg"] = "Sample blood report loaded successfully."


def handle_file_upload():
    """Callback to handle text or PDF file upload."""
    uploaded = st.session_state.get("uploaded_file_input")
    if uploaded is not None:
        if uploaded.name.endswith(".pdf"):
            content = extract_text_from_pdf(uploaded)
        else:
            content = uploaded.read().decode("utf-8", errors="ignore")
        if content:
            st.session_state["report_editor"] = content
            st.session_state["report_loaded_msg"] = f"Loaded file '{uploaded.name}' successfully."


def render_input_section() -> str:
    """Renders the blood report input methods and text area editor."""
    if "report_editor" not in st.session_state:
        st.session_state["report_editor"] = ""

    st.subheader("1. Laboratory Report Input")

    tab_sample, tab_upload, tab_text = st.tabs([
        "Sample Report",
        "Upload File (PDF / TXT)",
        "Direct Text Input"
    ])

    with tab_sample:
        st.caption("Load pre-configured reference report for testing (Patient: Rajesh Sharma, Age 48).")
        st.button("Load Sample Report", on_click=set_sample_report, type="secondary")

    with tab_upload:
        st.file_uploader(
            "Upload Laboratory Report (PDF or TXT format)",
            type=["pdf", "txt"],
            key="uploaded_file_input",
            on_change=handle_file_upload,
            help="Upload diagnostic test results in text or PDF format."
        )

    with tab_text:
        st.caption("Paste or modify raw laboratory test results.")

    if "report_loaded_msg" in st.session_state and st.session_state["report_loaded_msg"]:
        st.success(st.session_state["report_loaded_msg"])
        st.session_state["report_loaded_msg"] = ""

    # Main text editor for the report
    st.text_area(
        "Report Content",
        height=220,
        placeholder="Enter or paste blood test report text...",
        key="report_editor"
    )

    return st.session_state.get("report_editor", "").strip()
