
from utils.llm_handler import generate_ai_response


def analyze_complexity(code, language):
    return generate_ai_response(code, language, "complexity")
