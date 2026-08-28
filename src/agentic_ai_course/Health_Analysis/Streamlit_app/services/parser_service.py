import re
import pandas as pd


def parse_extracted_tests(extracted_text: str) -> pd.DataFrame:
    """
    Parses the LLM Stage 1 extraction response into a structured DataFrame.
    Expected line format: - Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range
    """
    records = []
    if not extracted_text or not isinstance(extracted_text, str):
        return pd.DataFrame()

    lines = extracted_text.strip().split("\n")

    for line in lines:
        line_clean = line.strip()
        if not line_clean or not line_clean.startswith("-"):
            continue

        clean_str = line_clean.lstrip("-* \t")
        parts = [p.strip() for p in clean_str.split("|")]
        if len(parts) >= 2:
            test_part = parts[0]
            if ":" in test_part:
                test_name, test_val = test_part.split(":", 1)
            else:
                test_name, test_val = test_part, "N/A"

            status = "UNKNOWN"
            status_part = parts[1]
            if ":" in status_part:
                _, status = status_part.split(":", 1)
            else:
                status = status_part
            status = status.strip().upper()

            ref_range = "N/A"
            if len(parts) >= 3:
                ref_part = parts[2]
                if ":" in ref_part:
                    _, ref_range = ref_part.split(":", 1)
                else:
                    ref_range = ref_part
                ref_range = ref_range.strip()

            records.append({
                "Test Name": test_name.strip(),
                "Measured Value": test_val.strip(),
                "Status": status,
                "Reference Range": ref_range
            })

    return pd.DataFrame(records)


def parse_diet_sections(diet_text: str):
    """
    Splits the nutritionist response into:
    1. Health Summary
    2. Food to Avoid
    3. Food to Eat More Of
    """
    if not diet_text or not isinstance(diet_text, str):
        return "", "", ""

    # Strip thinking tags from reasoning models if present
    cleaned = re.sub(r"<think>.*?</think>", "", diet_text, flags=re.DOTALL).strip()

    # Regex patterns for matching common heading variations
    avoid_pattern = r"(?:^|\n)\s*(?:#{1,4}\s*|\*{0,2}\s*(?:(?:1|2|\(1\)|\(2\))\s*[\.\)]?\s*)?)(?:Foods?|Items?|Dietary Items?)\s+to\s+avoid\s*:?\*{0,2}"
    eat_pattern = r"(?:^|\n)\s*(?:#{1,4}\s*|\*{0,2}\s*(?:(?:1|2|\(1\)|\(2\))\s*[\.\)]?\s*)?)(?:Foods?|Items?|Dietary Items?)\s+to\s+eat\s*(?:more\s*of|include)?\s*:?\*{0,2}"

    avoid_matches = list(re.finditer(avoid_pattern, cleaned, re.IGNORECASE))
    eat_matches = list(re.finditer(eat_pattern, cleaned, re.IGNORECASE))

    summary_part = ""
    avoid_part = ""
    eat_part = ""

    if avoid_matches and eat_matches:
        av_start, av_end = avoid_matches[0].start(), avoid_matches[0].end()
        eat_start, eat_end = eat_matches[0].start(), eat_matches[0].end()

        if av_start < eat_start:
            summary_part = cleaned[:av_start].strip()
            avoid_part = cleaned[av_end:eat_start].strip()
            eat_part = cleaned[eat_end:].strip()
        else:
            summary_part = cleaned[:eat_start].strip()
            eat_part = cleaned[eat_end:av_start].strip()
            avoid_part = cleaned[av_end:].strip()
    elif avoid_matches:
        av_start, av_end = avoid_matches[0].start(), avoid_matches[0].end()
        summary_part = cleaned[:av_start].strip()
        avoid_part = cleaned[av_end:].strip()
    elif eat_matches:
        eat_start, eat_end = eat_matches[0].start(), eat_matches[0].end()
        summary_part = cleaned[:eat_start].strip()
        eat_part = cleaned[eat_end:].strip()
    else:
        summary_part = cleaned

    # Clean leading/trailing dividers
    summary_part = re.sub(r"^[-–—]{3,}\s*", "", summary_part.strip(), flags=re.MULTILINE).strip()
    avoid_part = re.sub(r"^[-–—]{3,}\s*", "", avoid_part.strip(), flags=re.MULTILINE).strip()
    eat_part = re.sub(r"^[-–—]{3,}\s*", "", eat_part.strip(), flags=re.MULTILINE).strip()

    return summary_part, avoid_part, eat_part

