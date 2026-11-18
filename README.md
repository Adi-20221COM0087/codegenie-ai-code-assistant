# CodeGenie — AI-Based Code Explanation and Debugging Assistant

## Project Overview

CodeGenie is a locally running, AI-powered programming assistant developed using Python, Streamlit, Ollama and the Qwen2.5-Coder 1.5B model.

The application helps users understand programming code, identify potential errors, receive optimization suggestions and estimate algorithmic complexity.

CodeGenie supports Python, Java, C and C++.

## Objectives

- Explain programming code in beginner-friendly language.
- Identify possible syntax, runtime and logical errors.
- Suggest corrections and improvements.
- Recommend code optimizations.
- Estimate time and space complexity using Big-O notation.
- Provide an interactive interface for code analysis.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend programming |
| Streamlit | Web application interface |
| Ollama | Local AI model runtime |
| Qwen2.5-Coder 1.5B | AI-powered code analysis |
| Requests | Communication with Ollama API |
| Pygments | Installed syntax-highlighting library |
| HTML/CSS | Custom interface styling |

## Key Features

### 1. Code Explanation

Explains the purpose, functions, variables, execution flow and expected output of submitted code.

### 2. Code Debugging

Identifies potential programming errors and provides correction suggestions.

For selected Python patterns, the application uses static analysis to identify errors such as missing required function arguments.

### 3. Code Optimization

Suggests improvements in code readability, structure and efficiency while aiming to preserve intended behavior.

### 4. Complexity Analysis

Estimates time and auxiliary space complexity using Big-O notation.

### 5. Additional Features

- Support for Python, Java, C and C++.
- Sample Python programs.
- Syntax-highlighted code preview with line numbers.
- Clear Code functionality.
- Downloadable AI analysis results.
- Dark-themed Streamlit dashboard.
- Local AI processing through Ollama.

## System Requirements

- Windows 11 or another compatible operating system.
- Python 3.13 or a compatible version.
- Ollama installed.
- Qwen2.5-Coder 1.5B model downloaded.
- At least 8 GB RAM recommended for the tested local configuration.

## Installation and Setup

### Step 1: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 2: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Install and Configure Ollama

Install Ollama from its official website:

https://ollama.com

Download the required AI model:

```powershell
ollama pull qwen2.5-coder:1.5b
```

Ensure the Ollama service is running.

### Step 5: Run CodeGenie

```powershell
python -m streamlit run app.py
```

Open the application at:

http://localhost:8501

## How to Use

1. Open the CodeGenie dashboard.
2. Select a programming language.
3. Select Explain, Debug, Optimize or Analyze Complexity.
4. Paste code into the editor or load a sample program.
5. Click Analyze Code.
6. Review the AI-generated response.
7. Optionally download the analysis as a text file.

## Application Architecture

CodeGenie follows a modular architecture.

**User → Streamlit Interface → Selected Analysis Module → Ollama API → Qwen2.5-Coder → Analysis Result**

The Python debugger also incorporates local static-analysis checks for selected Python error patterns.

## Testing Summary

Eight planned functional test groups were completed:

| Test | Status |
|---|---|
| Python Code Explanation | Passed |
| Python Debugging | Passed |
| Python Code Optimization | Passed |
| Python Complexity Analysis | Passed |
| Java Code Explanation | Passed |
| C Code Explanation | Passed |
| C++ Code Explanation | Passed |
| Dashboard Functionality | Passed |

Dashboard testing included sample loading, clearing code, empty-input validation, syntax highlighting, result persistence and downloading analysis results.

## Limitations

- AI-generated explanations may contain inaccuracies.
- The application does not execute submitted programs.
- Python static analysis supports selected error patterns rather than complete program verification.
- Complexity estimates depend on the model's interpretation.
- Local inference speed depends on available hardware.
- The application requires Ollama and the downloaded model to be available locally.

## Future Enhancements

- Support for additional programming languages.
- More comprehensive static analysis.
- Automatic test-case generation.
- File upload support.
- Code comparison and optimization history.
- Improved error classification.
- More advanced AI models.

## Conclusion

CodeGenie demonstrates how a locally running generative AI model can be integrated into a web application to assist with code explanation, debugging, optimization and complexity analysis.

The project provides a practical example of generative AI integration using Python, Streamlit and Ollama.

## Project Type

B.Tech Generative AI Mini-Project
