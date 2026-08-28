import sys
from pathlib import Path
import streamlit as st

# -----------------------------------------------------------------------------
# Path Resolution for Modular Imports
# -----------------------------------------------------------------------------
APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from config import CUSTOM_CSS
from ui.sidebar import render_sidebar
from ui.input_view import render_input_section
from ui.dashboard_view import render_dashboard
from services.llm_service import (
    get_llm_client,
    run_stage_1_extraction,
    run_stage_2_diet_summary,
)

# -----------------------------------------------------------------------------
# Streamlit Page Setup & Styling
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Blood Work AI & Indian Diet Advisor",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown('<div class="main-header">🩸 Blood Work Analysis & Indian Diet Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Automated diagnostic report parsing, biomarker status classification, and personalized Indian dietary recommendations.</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Main Application Flow
# -----------------------------------------------------------------------------
def main():
    # 1. Sidebar Controls
    selected_model, temperature = render_sidebar()

    # 2. Input Section
    active_report = render_input_section()

    # 3. Execution Trigger
    analyze_btn = st.button("🚀 Analyze Blood Report", type="primary", use_container_width=True)

    if analyze_btn:
        if not active_report:
            st.error("❌ Please provide or load a blood test report before analyzing.")
        else:
            try:
                with st.spinner("Initializing LLM client..."):
                    llm = get_llm_client(model_name=selected_model, temperature=temperature)

                with st.status("🔬 Processing Blood Work Report...", expanded=True) as status_box:
                    st.write("Extracting lab markers and classifying reference intervals...")
                    extracted_values = run_stage_1_extraction(llm, active_report)
                    st.session_state["extracted_values"] = extracted_values
                    st.write("✅ Lab markers extracted & classified.")

                    st.write("Generating clinical health summary and Indian diet plan...")
                    diet_summary = run_stage_2_diet_summary(llm, extracted_values)
                    st.session_state["diet_summary"] = diet_summary
                    st.write("✅ Clinical health summary & Indian diet recommendations ready.")

                    status_box.update(label="🎉 Analysis Completed Successfully!", state="complete", expanded=False)

            except Exception as e:
                st.error(f"Error during analysis: {e}")

    # 4. Results Dashboard
    if "extracted_values" in st.session_state and "diet_summary" in st.session_state:
        render_dashboard(
            extracted_values=st.session_state["extracted_values"],
            diet_summary=st.session_state["diet_summary"]
        )


if __name__ == "__main__":
    main()
