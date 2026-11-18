# 💻 CodeGenie — AI-Based Code Explanation and Debugging Assistant

**B.Tech Generative AI Mini-Project**

CodeGenie is an AI-powered programming assistant that helps developers and students understand, debug, optimize, and analyze programming code.

The application supports both **Google Gemini cloud AI** and **local Ollama AI**, providing flexible options for online and local code analysis.

## 🌐 Live Demo

**Try CodeGenie online:**

**[🚀 Launch CodeGenie](https://codegenie-ai-code-assistant-h8jebagittpvxrsiaceua6.streamlit.app)**

**[📂 View GitHub Repository](https://github.com/Adi-20221COM0087/codegenie-ai-code-assistant)**

The application is deployed on **Streamlit Community Cloud** and uses Google Gemini 3.5 Flash Lite for cloud-based AI analysis.

The live deployment requires no local installation. Availability depends on Streamlit hosting and Gemini API service limits.

## 📖 Project Overview

CodeGenie is an AI-powered programming assistant developed using Python, Streamlit, Google Gemini, Ollama, and Qwen2.5-Coder 1.5B.

The application helps users understand programming code, identify potential errors, receive optimization suggestions, and estimate algorithmic complexity.

CodeGenie supports four programming languages:

- Python
- Java
- C
- C++

### AI Backend Options

| Mode | AI Model | Backend | Requirements |
|---|---|---|---|
| Cloud Mode | Gemini 3.5 Flash Lite | Google Gemini API | Internet connection and API key |
| Local Mode | Qwen2.5-Coder 1.5B | Ollama | Installed Ollama and downloaded model |

The deployed application uses **Cloud Mode**, while the local installation can use either backend.

## 🎯 Objectives

- Explain programming code in beginner-friendly language.
- Identify possible syntax, runtime, and logical errors.
- Suggest corrections and improvements.
- Recommend code optimizations.
- Estimate time and auxiliary space complexity using Big-O notation.
- Provide an interactive interface for code analysis.
- Support both local and cloud-based AI processing.
- Make CodeGenie accessible through a public web application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend programming and tested local environment |
| Streamlit | Interactive web application interface and cloud deployment |
| Google Gemini API | Cloud-based AI code analysis |
| Gemini 3.5 Flash Lite | AI model used for cloud inference |
| Ollama | Local AI model runtime |
| Qwen2.5-Coder 1.5B | Local AI-powered code analysis |
| Requests | HTTP communication with Gemini and Ollama APIs |
| Python AST | Static analysis of selected Python error patterns |
| Pygments | Installed syntax-highlighting library |
| Python-dotenv | Environment configuration support |
| HTML/CSS | Custom dashboard styling |
| GitHub | Source code hosting and version control |
| Streamlit Community Cloud | Public application hosting |

## ✨ Key Features

### 1. Code Explanation

Explains the purpose, functions, variables, execution flow, and expected output of submitted programming code.

### 2. Code Debugging

Identifies potential syntax, runtime, and logical errors and provides correction suggestions.

For selected Python patterns, the application uses static analysis to identify errors such as missing required function arguments.

### 3. Code Optimization

Suggests improvements in code readability, structure, and efficiency while aiming to preserve intended behavior.

### 4. Complexity Analysis

Estimates:

- Worst-case time complexity
- Best-case time complexity, when meaningful
- Average-case time complexity, when determinable
- Auxiliary space complexity

Complexity estimates use Big-O notation and depend on the code and assumptions involved.

### 5. Additional Features

- Support for Python, Java, C, and C++.
- Google Gemini cloud AI integration.
- Local Ollama AI support.
- Automatic backend and model information in the dashboard.
- Sample Python programs.
- Syntax-highlighted code preview with line numbers.
- Clear Code functionality.
- Downloadable AI analysis results.
- Dark-themed Streamlit dashboard.
- Public web application accessible through a browser.

## 💻 System Requirements

### Cloud Version

To use the deployed CodeGenie application:

- A modern web browser.
- An internet connection.

**Live Application:** https://codegenie-ai-code-assistant-h8jebagittpvxrsiaceua6.streamlit.app

No Python or Ollama installation is required for visitors using the hosted application.

### Local Version

- Windows 11 or another compatible operating system.
- Python 3.13 or a compatible version.
- Ollama installed for local AI mode.
- Qwen2.5-Coder 1.5B downloaded for local AI mode.
- At least 8 GB RAM recommended for the tested local configuration.
- Internet connection and Gemini API key for cloud AI mode.

## ⚙️ Installation and Setup

### Step 1: Clone or Download the Repository

Clone the project:

```powershell
git clone https://github.com/Adi-20221COM0087/codegenie-ai-code-assistant.git
```

Navigate to the project folder:

```powershell
cd codegenie-ai-code-assistant
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

The project's direct dependencies are:

```text
streamlit==1.67.0
requests==2.34.2
Pygments==2.21.0
python-dotenv==1.2.4
```

## 🤖 AI Backend Configuration

CodeGenie supports two AI backends.

### Option A: Google Gemini Cloud Mode

This mode uses Google Gemini through its hosted API.

**Step 1:** Create a Gemini API key using Google AI Studio.

https://aistudio.google.com/

**Step 2:** Create the following file in the project directory:

```text
.streamlit/secrets.toml
```

**Step 3:** Add the configuration:

```toml
AI_BACKEND = "gemini"
GEMINI_MODEL = "gemini-3.5-flash-lite"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your private API key.

**Important:** Never upload `secrets.toml` or your actual API key to GitHub.

The `.gitignore` file excludes `.streamlit/secrets.toml` from normal Git tracking.

Cloud API access is subject to Google's current pricing, quotas, and model availability.

### Option B: Local Ollama Mode

This mode uses Ollama and Qwen2.5-Coder 1.5B on your computer.

**Step 1:** Install Ollama from:

https://ollama.com/

**Step 2:** Download the required model:

```powershell
ollama pull qwen2.5-coder:1.5b
```

**Step 3:** Configure the local backend using PowerShell:

```powershell
$env:AI_BACKEND = "ollama"
$env:OLLAMA_MODEL = "qwen2.5-coder:1.5b"
```

If your local `secrets.toml` specifies `AI_BACKEND = "gemini"`, update that setting to `"ollama"` or remove the conflicting configuration before starting Streamlit.

**Step 4:** Ensure the Ollama service is running.

Local Ollama inference does not require a hosted Gemini API key.

## 🚀 Run CodeGenie Locally

Start the Streamlit application:

```powershell
python -m streamlit run app.py
```

Open the application at:

http://localhost:8501

The dashboard automatically displays the configured AI backend and model.

## 📋 How to Use

1. Open the CodeGenie dashboard.
2. Select a programming language: Python, Java, C, or C++.
3. Select an operation: Explain Code, Debug Code, Optimize Code, or Analyze Complexity.
4. Paste programming code into the editor or load a sample program.
5. Click **Analyze Code**.
6. Review the AI-generated response.
7. Optionally download the analysis as a text file.

### Example

**Input:**

```python
print(2 + 3)
```

**Expected analysis:**

CodeGenie explains that Python evaluates the expression `2 + 3` and passes the result to the `print()` function.

**Expected program output:**

```text
5
```

CodeGenie analyzes submitted code without executing it.

## 🏗️ Application Architecture

CodeGenie follows a modular architecture supporting both local and cloud-based AI inference.

### Cloud Architecture

**User → Streamlit Interface → Selected Analysis Module → Google Gemini API → Gemini Model → Analysis Result**

### Local Architecture

**User → Streamlit Interface → Selected Analysis Module → Ollama API → Qwen2.5-Coder → Analysis Result**

The Python debugger also incorporates local static-analysis checks for selected Python error patterns.

### Project Structure

```text
AI_Code_Assistant/
├── assets/
│   └── style.css
├── modules/
│   ├── __init__.py
│   ├── code_explainer.py
│   ├── code_debugger.py
│   ├── code_optimizer.py
│   └── complexity_analyzer.py
├── utils/
│   ├── __init__.py
│   ├── llm_handler.py
│   └── python_analyzer.py
├── app.py
├── README.md
├── ARCHITECTURE.md
├── requirements.txt
├── .gitignore
├── test_backend.py
└── test_ollama.py
```

For local Gemini configuration, create `.streamlit/secrets.toml` separately. This private file must not be committed.

## 🧪 Testing Summary

Eight planned functional test groups were completed during local development:

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

Dashboard testing included sample loading, clearing code, empty-input validation, syntax highlighting, result persistence, and downloading analysis results.

### Cloud Deployment Testing

| Test | Status |
|---|---|
| Streamlit Community Cloud deployment | Passed |
| Cloud dashboard loading | Passed |
| Gemini API integration | Passed |
| Python code explanation using Gemini | Passed |
| Expected output identification | Passed |
| Cloud debugging, optimization, and complexity operations | Pending full verification |

The hosted application successfully generated an explanation for `print(2 + 3)` using Gemini 3.5 Flash Lite.

These results describe functional checks and do not represent a formal model accuracy benchmark.

## ☁️ Cloud Deployment

CodeGenie is deployed using **Streamlit Community Cloud**.

### Deployment Configuration

| Setting | Value |
|---|---|
| Hosting Platform | Streamlit Community Cloud |
| GitHub Repository | `Adi-20221COM0087/codegenie-ai-code-assistant` |
| Branch | `main` |
| Main Application File | `app.py` |
| AI Backend | `gemini` |
| AI Model | `gemini-3.5-flash-lite` |

### Deployment Steps

1. Upload the project source code to GitHub.
2. Open https://share.streamlit.io/.
3. Sign in using GitHub.
4. Select the CodeGenie repository.
5. Choose the `main` branch.
6. Set the main application file to `app.py`.
7. Open Advanced settings and configure the private secrets.
8. Deploy the application.
9. Verify that the dashboard loads and the Gemini backend responds.

### Streamlit Cloud Secrets

Configure the following values privately in Streamlit Community Cloud:

```toml
AI_BACKEND = "gemini"
GEMINI_MODEL = "gemini-3.5-flash-lite"
GEMINI_API_KEY = "YOUR_PRIVATE_GEMINI_API_KEY"
```

Do not store actual API keys in public source code.

### Live Application

https://codegenie-ai-code-assistant-h8jebagittpvxrsiaceua6.streamlit.app

The deployment has a public URL, but continuous availability is not guaranteed. Streamlit may put inactive applications to sleep, and Gemini requests depend on API service availability and quota.

## ⚠️ Limitations

- AI-generated explanations and suggestions may contain inaccuracies.
- The application does not execute submitted programs.
- Python static analysis supports selected error patterns rather than complete program verification.
- Complexity estimates depend on the model's interpretation and assumptions.
- Local inference speed depends on available hardware.
- Local Ollama mode requires the Ollama service and downloaded model.
- Cloud mode requires internet connectivity and a valid Gemini API key.
- Cloud inference may be affected by rate limits, quotas, or service interruptions.
- Public Streamlit applications may become inactive when not in use.
- The application is intended for educational assistance, not guaranteed program verification.

## 🔮 Future Enhancements

- Support for additional programming languages.
- More comprehensive static analysis.
- Automatic test-case generation.
- File upload support.
- Code comparison and optimization history.
- Improved error classification.
- More advanced AI models.
- Additional cloud model options.
- Improved API quota and error handling.
- User authentication and analysis history.

## 🎓 Conclusion

CodeGenie demonstrates how generative AI models can be integrated into an interactive web application to assist with code explanation, debugging, optimization, and complexity analysis.

The project supports both **local AI inference using Ollama and Qwen2.5-Coder** and **cloud-based inference using Google Gemini**.

By deploying CodeGenie on Streamlit Community Cloud, the application can be accessed through a public web link without requiring visitors to install Python or Ollama.

The project provides a practical example of generative AI integration, modular Python development, API communication, and cloud deployment.

## 📚 Project Type

**B.Tech Generative AI Mini-Project**

**Project Name:** CodeGenie — AI-Based Code Explanation and Debugging Assistant

**Source Code:** https://github.com/Adi-20221COM0087/codegenie-ai-code-assistant

**Live Demo:** https://codegenie-ai-code-assistant-h8jebagittpvxrsiaceua6.streamlit.app
