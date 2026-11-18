
import requests

print("Connecting to Ollama...")

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5-coder:1.5b",
    "prompt": """
Explain this Python code in simple language:

def add(a, b):
    return a + b

print(add(10, 20))
""",
    "stream": False
}

try:
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()

    result = response.json()

    print("\nConnection Successful!")
    print("\nAI Explanation:\n")
    print(result["response"])

except requests.exceptions.RequestException as e:
    print("Connection Failed:", e)
