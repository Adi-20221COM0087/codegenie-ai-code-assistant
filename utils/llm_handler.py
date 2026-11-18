
import requests

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:1.5b"


def generate_ai_response(code, language, operation):
    """
    Send code to the local Ollama AI model.
    """

    if not code.strip():
        return "Error: Please enter some code."

    prompts = {
        "explain": f"""
You are a programming teacher.
Explain this {language} code in simple language.

Include:
1. Purpose of the code
2. Step-by-step explanation
3. Functions and variables
4. Expected output if determinable

Code:
{code}
""",

        "debug": f"""
You are an expert {language} code debugger.

Carefully inspect the code without executing it.

Follow these steps:
1. Identify all function definitions and their required parameters.
2. Examine every function call and count the arguments.
3. Check for missing or extra arguments.
4. Identify syntax errors.
5. Identify possible runtime errors, including TypeError,
   NameError, IndexError, and ZeroDivisionError.
6. Identify logical mistakes.
7. Explain each confirmed or potential error clearly.
8. Provide corrected code.
9. Explain the expected output if determinable.

IMPORTANT:
- Do not claim the code is error-free without checking
  function calls against function definitions.
- Distinguish definite errors from possible errors.
- Do not claim to have executed the code.
- Use the correct syntax and rules for {language}.

CODE:
{code}
""",

        "optimize": f"""
You are an expert {language} programmer.

Improve the following code.

Include:
1. Optimization suggestions
2. Improved code
3. Explanation of improvements

Preserve the intended behavior.

Code:
{code}
""",

        "complexity": f"""
You are an expert {language} algorithm analyst.

Analyze the following code without executing it.

Include:
1. Worst-case time complexity using Big-O notation.
2. Best-case time complexity, when meaningful.
3. Average-case time complexity, when determinable.
4. Auxiliary space complexity using Big-O notation.
5. A clear explanation of loops, recursion, and
   data structures affecting complexity.

Important rules:
- Do not invent assumptions about the input.
- Do not assume an array is nonempty unless
  the code requires it.
- Do not assume a searched value exists.
- Distinguish auxiliary space from input storage.
- Explain when best-case and worst-case differ.
- If complexity cannot be determined reliably,
  explain the uncertainty.
- Do not claim the code was executed.

Code:
{code}
"""
    }

    if operation not in prompts:
        return "Error: Invalid operation."

    payload = {
        "model": MODEL_NAME,
        "prompt": prompts[operation],
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_ctx": 4096,
            "num_predict": 700
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        return result.get(
            "response",
            "No response generated."
        )

    except requests.exceptions.Timeout:
        return "Error: Ollama response timed out."

    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama."

    except requests.exceptions.RequestException as error:
        return f"Error: {error}"
