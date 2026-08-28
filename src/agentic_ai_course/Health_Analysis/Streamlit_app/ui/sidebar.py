import streamlit as st
from config import SUPPORTED_MODELS, DEFAULT_MODEL, DEFAULT_TEMPERATURE


def render_sidebar():
    """Renders the sidebar controls for model selection, temperature, and about info."""
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/blood-test.png", width=64)
        st.title("Settings & Config")

        # Model Selection
        selected_model = st.selectbox(
            "Select LLM Model",
            options=SUPPORTED_MODELS,
            index=0,
            help="Model used for biomarker extraction and Indian dietary recommendations.",
        )

        # Temperature Slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.05,
            help="Lower values yield more deterministic and precise extraction.",
        )

        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.info(
            "This app uses a two-stage Agentic LLM workflow to:\n"
            "1. **Extract & Classify** blood parameters against reference ranges.\n"
            "2. **Generate** a patient-friendly summary and personalized **Indian Diet Plan**."
        )

        st.markdown("---")
        st.caption("⚠️ **Medical Disclaimer**: This AI tool is for educational and informational purposes only. Always consult a qualified physician or registered dietitian for medical diagnosis and treatment.")

        return selected_model, temperature
