import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:latest"

SYSTEM_INSTRUCTIONS = """You are an AI Email Assistant.
Given an email, produce:
1) SUMMARY: 3-5 bullet points
2) REPLY: a professional, friendly reply
If details are missing, add:
QUESTIONS: bullet list

Return output exactly in this format:

SUMMARY:
- ...

REPLY:
...

QUESTIONS (if needed):
- ...
"""

def ask_ollama(email_text: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": f"{SYSTEM_INSTRUCTIONS}\n\nEMAIL:\n{email_text.strip()}",
        "stream": False,
        "options": {
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": 350
        }
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=300)
    r.raise_for_status()
    return r.json()["response"].strip()

if __name__ == "__main__":
    print("Paste the email below. Press ENTER on an empty line to finish:\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    email = "\n".join(lines).strip()

    if not email:
        print("No email text provided.")
    else:
        print("\n" + ask_ollama(email))
