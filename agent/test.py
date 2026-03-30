# test_openai.py
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "Convert SQL to MongoDB: SELECT * FROM users"
    }
)

print(response.text)