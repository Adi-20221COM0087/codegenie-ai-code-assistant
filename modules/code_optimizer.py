
from utils.llm_handler import generate_ai_response


def optimize_code(code, language):
    return generate_ai_response(code, language, "optimize")
