import streamlit as st
from config import SUPPORTED_MODELS, DEFAULT_MODEL, DEFAULT_TEMPERATURE


def render_sidebar():
    """Renders the sidebar controls for model selection, temperature, and about info."""
    """Renders the sidebar controls for model selection, temperature, and system configuration."""
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/blood-test.png", width=64)
        st.title("Settings & Config")
        st.subheader("Configuration")

        # Model Selection
        selected_model = st.selectbox(
            "Select LLM Model",
            "Language Model",
            options=SUPPORTED_MODELS,
            index=0,
            help="Model used for biomarker extraction and Indian dietary recommendations.",
            help="Select the model used for biomarker extraction and clinical diet recommendations.",
        )

        # Temperature Slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.05,
            help="Lower values yield more deterministic and precise extraction.",
            help="Lower values yield deterministic and structured extraction.",
        )

        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.subheader("About Application")
        st.info(
            "This app uses a two-stage Agentic LLM workflow to:\n"
            "1. **Extract & Classify** blood parameters against reference ranges.\n"
            "2. **Generate** a patient-friendly summary and personalized **Indian Diet Plan**."
            "This application uses a two-stage agentic workflow to:\n\n"
            "1. Extract and classify diagnostic test parameters against clinical reference ranges.\n"
            "2. Generate an Indian dietary plan and health summary based on identified biomarkers."
        )

        st.markdown("---")
        st.caption("⚠️ **Medical Disclaimer**: This AI tool is for educational and informational purposes only. Always consult a qualified physician or registered dietitian for medical diagnosis and treatment.")
        st.caption("Medical Disclaimer: This application is for educational and informational purposes only. It should not be used as a substitute for professional clinical diagnosis or treatment. Consult a certified physician or registered dietitian for medical evaluation.")

        return selected_model, temperature

