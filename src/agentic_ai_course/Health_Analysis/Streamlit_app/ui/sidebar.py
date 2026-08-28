import streamlit as st
from config import SUPPORTED_MODELS, DEFAULT_MODEL, DEFAULT_TEMPERATURE


def render_sidebar():
    """Renders the sidebar controls for model selection, temperature, and system configuration."""
    with st.sidebar:
        st.subheader("Configuration")

        # Model Selection
        selected_model = st.selectbox(
            "Language Model",
            options=SUPPORTED_MODELS,
            index=0,
            help="Select the model used for biomarker extraction and clinical diet recommendations.",
        )

        # Temperature Slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULT_TEMPERATURE,
            step=0.05,
            help="Lower values yield deterministic and structured extraction.",
        )

        st.markdown("---")
        st.subheader("About Application")
        st.info(
            "This application uses a two-stage agentic workflow to:\n\n"
            "1. Extract and classify diagnostic test parameters against clinical reference ranges.\n"
            "2. Generate an Indian dietary plan and health summary based on identified biomarkers."
        )

        st.markdown("---")
        st.caption("Medical Disclaimer: This application is for educational and informational purposes only. It should not be used as a substitute for professional clinical diagnosis or treatment. Consult a certified physician or registered dietitian for medical evaluation.")

        return selected_model, temperature
