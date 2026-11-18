
from utils.llm_handler import generate_ai_response
from utils.python_analyzer import analyze_python_code


def debug_code(code, language):
    if language == "Python":
        detected_errors = analyze_python_code(code)

        if detected_errors:
            error_report = "\n".join(
                f"- {error}" for error in detected_errors
            )

            return (
                "### Python Static Analysis Findings\n\n"
                "**Potential issues detected:**\n\n"
                + error_report
                + "\n\n"
                "**Explanation:**\n\n"
                "The static analyzer identified potential "
                "syntax or function-call issues. Review "
                "the findings above to understand which "
                "rules may have been violated.\n\n"
                "**Suggested correction:**\n\n"
                "Correct the reported syntax or function-call "
                "issues, then analyze the updated code again.\n\n"
                "**Note:** This analyzer checks selected "
                "Python patterns without executing the code. "
                "It cannot detect every possible error."
            )

    return generate_ai_response(code, language, "debug")
