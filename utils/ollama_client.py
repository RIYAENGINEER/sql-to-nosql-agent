import requests

def generate_with_ollama(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False  # 🔥 important
        }
    )

    data = response.json()
    return data.get("response", "")