
import os
import requests

# ==========================================
# AI BACKEND CONFIGURATION
# ==========================================

# Available backends: "ollama" or "gemini"
# Default: Ollama for offline/local usage
AI_BACKEND = os.getenv("AI_BACKEND", "ollama").strip().lower()

# Ollama configuration
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)
MODEL_NAME = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5-coder:1.5b"
)

# Gemini configuration
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.5-flash-lite"
)

GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models"
)


# ==========================================
# GOOGLE GEMINI CLOUD BACKEND
# ==========================================

def generate_gemini_response(prompt):
    """
    Send a prompt to Google Gemini API.
    Requires GEMINI_API_KEY.
    """

    api_key = os.getenv(
        "GEMINI_API_KEY", ""
    ).strip()

    if not api_key:
        return (
            "Error: GEMINI_API_KEY is not configured. "
            "Please configure your Gemini API key."
        )

    url = (
        f"{GEMINI_API_URL}/"
        f"{GEMINI_MODEL}:generateContent"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 1200
        }
    }

    try:
        response = requests.post(
            url,
            headers={
                "x-goog-api-key": api_key,
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        candidates = result.get(
            "candidates", []
        )

        if not candidates:
            return (
                "Error: Gemini returned no response. "
                "Check API quota, model availability, "
                "or content restrictions."
            )

        parts = candidates[0].get(
            "content", {}
        ).get(
            "parts", []
        )

        answer = "\n".join(
            part.get("text", "")
            for part in parts
            if part.get("text")
        ).strip()

        if not answer:
            return (
                "Error: Gemini returned an "
                "empty response."
            )

        return answer

    except requests.exceptions.Timeout:
        return (
            "Error: Gemini API response timed out."
        )

    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        if status_code == 400:
            return (
                "Error: Invalid Gemini API request. "
                "Check the selected model."
            )

        if status_code in (401, 403):
            return (
                "Error: Gemini API authentication "
                "or access failed. Check your API key."
            )

        if status_code == 404:
            return (
                "Error: Gemini model not found. "
                "Check GEMINI_MODEL."
            )

        if status_code == 429:
            return (
                "Error: Gemini API quota or rate "
                "limit exceeded. Try again later."
            )

        return (
            f"Error: Gemini API returned "
            f"HTTP {status_code}."
        )

    except requests.exceptions.ConnectionError:
        return (
            "Error: Cannot connect to Gemini API. "
            "Check your internet connection."
        )

    except requests.exceptions.RequestException:
        return (
            "Error: Gemini API request failed."
        )

    except ValueError:
        return (
            "Error: Invalid JSON response "
            "received from Gemini."
        )


# ==========================================
# LOCAL OLLAMA BACKEND
# ==========================================

def generate_ollama_response(prompt):
    """
    Send a prompt to the local Ollama model.
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
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
        return (
            "Error: Ollama response timed out."
        )

    except requests.exceptions.ConnectionError:
        return (
            "Error: Cannot connect to Ollama. "
            "Make sure Ollama is running."
        )

    except requests.exceptions.RequestException as error:
        return f"Error: {error}"

    except ValueError:
        return (
            "Error: Invalid JSON response "
            "received from Ollama."
        )


# ==========================================
# MAIN CODEGENIE AI FUNCTION
# ==========================================

def generate_ai_response(code, language, operation):
    """
    Generate an AI response using either
    local Ollama or hosted Google Gemini.

    Supported operations:
    - explain
    - debug
    - optimize
    - complexity
    """

    if not code or not code.strip():
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

    prompt = prompts[operation]

    # Select AI backend
    if AI_BACKEND == "gemini":
        return generate_gemini_response(prompt)

    if AI_BACKEND == "ollama":
        return generate_ollama_response(prompt)

    return (
        f"Error: Unsupported AI backend "
        f"'{AI_BACKEND}'. "
        "Use 'ollama' or 'gemini'."
    )
