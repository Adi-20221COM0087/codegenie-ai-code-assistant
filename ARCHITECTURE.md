# CodeGenie — System Architecture and Workflow

## 1. Introduction

CodeGenie is a locally running AI-powered code analysis application developed using Python, Streamlit, Ollama and Qwen2.5-Coder 1.5B.

It provides code explanation, debugging assistance, optimization suggestions and algorithmic complexity analysis.

## 2. System Architecture

The application follows a modular architecture consisting of the presentation layer, analysis modules, static-analysis component and local AI inference layer.

### Presentation Layer

The Streamlit application (`app.py`) provides the interface for entering code, selecting the programming language, choosing the analysis operation and viewing results.

### Analysis Layer

The application contains four primary modules:

- `code_explainer.py`: Generates code explanations.
- `code_debugger.py`: Identifies potential programming errors.
- `code_optimizer.py`: Suggests improvements to submitted code.
- `complexity_analyzer.py`: Estimates algorithmic time and space complexity.

### Static Analysis Component

The `python_analyzer.py` module uses Python's Abstract Syntax Tree (AST) to detect selected syntax errors and function argument mismatches without executing the submitted program.

For Python debugging, the static analyzer runs first. When it reports issues, the debugger returns a predefined report. Otherwise, the request is forwarded to the local AI model.

### AI Inference Layer

The `llm_handler.py` module constructs task-specific prompts and communicates with the Ollama API using HTTP requests.

The application uses the Qwen2.5-Coder 1.5B model for local inference.

## 3. System Workflow

1. The user enters programming code.
2. The user selects Python, Java, C or C++.
3. The user chooses an analysis operation.
4. Streamlit forwards the request to the appropriate module.
5. For Python debugging, selected static-analysis checks run first.
6. Requests requiring AI inference are forwarded to the LLM handler.
7. The LLM handler sends the prompt to Ollama.
8. Ollama processes the prompt using Qwen2.5-Coder 1.5B.
9. The resulting analysis is returned to the Streamlit dashboard.
10. The user reviews the response and may download it as a text file.

## 4. Technologies

- Python — Application programming language.
- Streamlit — Web interface.
- Ollama — Local model execution.
- Qwen2.5-Coder 1.5B — Generative AI model.
- Requests — HTTP communication.
- Python AST — Selected static-analysis checks.
- Pygments — Syntax-highlighting library.
- CSS — Dashboard styling.

## 5. Advantages

- Local AI inference without requiring a paid cloud API.
- Modular implementation.
- Beginner-friendly interface.
- Support for four programming languages.
- Static checks for selected Python errors.
- Downloadable analysis results.

## 6. Limitations

- The application does not execute submitted code.
- AI responses may contain incorrect suggestions.
- The AST analyzer detects only selected Python error patterns.
- Complexity estimates are not formally verified.
- The local Ollama model must be available for AI-powered operations.

## 7. Conclusion

CodeGenie demonstrates the integration of generative AI, local model inference, static program analysis and an interactive web interface to support programming education and code review.
