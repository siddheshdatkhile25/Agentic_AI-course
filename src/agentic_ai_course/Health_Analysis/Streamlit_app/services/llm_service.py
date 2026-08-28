import os
from langchain_groq import ChatGroq
from config import (
    EXTRACTION_PROMPT_TEMPLATE,
    DIET_PROMPT_TEMPLATE,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
)


def extract_text_from_response(response) -> str:
    """Safely extracts string content from LangChain / Groq response object."""
    if response is None:
        return ""
    if hasattr(response, "content") and response.content is not None:
        if isinstance(response.content, str):
            return response.content
        elif isinstance(response.content, list):
            parts = []
            for part in response.content:
                if isinstance(part, str):
                    parts.append(part)
                elif isinstance(part, dict) and "text" in part:
                    parts.append(part["text"])
                else:
                    parts.append(str(part))
            return "".join(parts)
    if hasattr(response, "text") and response.text is not None:
        return str(response.text)
    return str(response)



def get_llm_client(model_name: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE) -> ChatGroq:
    """Initializes and returns the ChatGroq client using GROQ_API_KEY from environment."""
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY was not found in the environment. Please check your .env file.")
    return ChatGroq(
        model=model_name,
        api_key=api_key,
        temperature=temperature,
    )


def run_stage_1_extraction(llm: ChatGroq, report_text: str) -> str:
    """Stage 1: Extract lab biomarkers and classify reference ranges."""
    prompt = EXTRACTION_PROMPT_TEMPLATE.format(blood_report=report_text)
    response = llm.invoke(prompt)
    return extract_text_from_response(response)


def run_stage_2_diet_summary(llm: ChatGroq, extracted_values: str) -> str:
    """Stage 2: Generate health summary and personalized Indian diet recommendations."""
    prompt = DIET_PROMPT_TEMPLATE.format(extracted_values=extracted_values)
    response = llm.invoke(prompt)
    return extract_text_from_response(response)

