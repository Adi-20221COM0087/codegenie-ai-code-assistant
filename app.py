
import streamlit as st
from pathlib import Path

from modules.code_explainer import explain_code
from modules.code_debugger import debug_code
from modules.code_optimizer import optimize_code
from modules.complexity_analyzer import analyze_complexity


# Page configuration
st.set_page_config(
    page_title="CodeGenie - AI Code Assistant",
    page_icon="💻",
    layout="wide"
)


# Load custom CSS
css_path = Path(__file__).parent / "assets" / "style.css"

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True
        )


# Header
st.title("💻 CodeGenie")
st.subheader("AI-Based Code Explanation and Debugging Assistant")

st.write(
    "Understand, debug, optimize, and analyze your "
    "code using a locally running AI model."
)

st.divider()


# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox(
        "Select Programming Language",
        ["Python", "Java", "C", "C++"]
    )

    operation = st.radio(
        "Select AI Operation",
        [
            "Explain Code",
            "Debug Code",
            "Optimize Code",
            "Analyze Complexity"
        ]
    )

    st.divider()

    st.info(
        "AI Model: Qwen2.5-Coder 1.5B\n\n"
        "Backend: Ollama\n\n"
        "Framework: Streamlit"
    )


# Sample code templates
sample_codes = {
    "None": "",

    "Python - Factorial": """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))""",

    "Python - Debug Example": """def add(a, b):
    return a + b

print(add(10))""",

    "Python - Linear Search": """def search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False"""
}


# Initialize session state
if "code_input" not in st.session_state:
    st.session_state.code_input = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""

if "analysis_is_error" not in st.session_state:
    st.session_state.analysis_is_error = False


# Sample code selection
sample_choice = st.selectbox(
    "📚 Load Sample Code",
    list(sample_codes.keys())
)


# Load sample button
if st.button("Load Sample"):
    st.session_state.code_input = sample_codes[sample_choice]
    st.session_state.analysis_result = ""
    st.session_state.analysis_is_error = False
    st.rerun()


# Clear code button
if st.button("🗑️ Clear Code"):
    st.session_state.code_input = ""
    st.session_state.analysis_result = ""
    st.session_state.analysis_is_error = False
    st.rerun()


# Main layout - wider AI result panel
left_col, right_col = st.columns(
    [1, 1.2],
    gap="large"
)


with left_col:
    st.header("📝 Code Editor")

    code = st.text_area(
        "Enter your code below",
        height=400,
        placeholder="Paste your programming code here...",
        key="code_input"
    )

    # Syntax-highlighted code preview
    if code.strip():
        with st.expander("👁️ Syntax-Highlighted Preview"):

            language_map = {
                "Python": "python",
                "Java": "java",
                "C": "c",
                "C++": "cpp"
            }

            st.code(
                code,
                language=language_map[language],
                line_numbers=True
            )

    # Analyze code button
    analyze_button = st.button(
        "🚀 Analyze Code",
        type="primary",
        use_container_width=True
    )


with right_col:
    st.header("🤖 AI Analysis Result")

    if analyze_button:

        if not code.strip():
            st.warning("Please enter some code first.")

        else:
            operations = {
                "Explain Code": explain_code,
                "Debug Code": debug_code,
                "Optimize Code": optimize_code,
                "Analyze Complexity": analyze_complexity
            }

            selected_function = operations[operation]

            with st.spinner("AI is analyzing your code..."):
                result = selected_function(code, language)

            # Save the latest AI response
            st.session_state.analysis_result = result
            st.session_state.analysis_is_error = (
                result.startswith("Error:")
            )

    # Display saved analysis result
    if st.session_state.analysis_result:

        if st.session_state.analysis_is_error:
            st.error(st.session_state.analysis_result)

        else:
            st.markdown(st.session_state.analysis_result)

            # Download AI result
            st.download_button(
                label="📥 Download AI Result",
                data=st.session_state.analysis_result,
                file_name="CodeGenie_Analysis.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif not analyze_button:
        st.info(
            "Your AI-generated analysis will appear here."
        )


st.divider()

st.caption(
    "CodeGenie | Powered by Ollama and Qwen2.5-Coder | "
    "AI-generated results should be reviewed before use."
)
