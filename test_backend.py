
from modules.code_explainer import explain_code
from modules.code_debugger import debug_code
from modules.code_optimizer import optimize_code
from modules.complexity_analyzer import analyze_complexity

sample_code = """
def add(a, b):
    return a + b

print(add(10, 20))
"""

print("=== CodeGenie AI Backend Test ===")
print("1. Explain Code")
print("2. Debug Code")
print("3. Optimize Code")
print("4. Analyze Complexity")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = explain_code(sample_code, "Python")
elif choice == "2":
    result = debug_code(sample_code, "Python")
elif choice == "3":
    result = optimize_code(sample_code, "Python")
elif choice == "4":
    result = analyze_complexity(sample_code, "Python")
else:
    result = "Invalid choice"

print("\n=== AI RESPONSE ===\n")
print(result)
