AI Email Assistant (Local & Free)

A local AI-powered Email Assistant that summarizes emails and generates
professional reply suggestions using Ollama and open-source LLMs.

Runs 100% locally
No paid APIs required
Privacy-first and offline

--------------------------------------------------

KEY FEATURES
- Email summarization (3–5 bullet points)
- Professional reply drafting
- Clarification questions when details are missing
- Fully offline and secure
- Beginner-friendly and lightweight

--------------------------------------------------

HOW IT WORKS

Email Text
   |
   v
Prompt + Instructions
   |
   v
Local LLM (Ollama)
   |
   v
Summary + Reply + Questions

--------------------------------------------------

TECH STACK
- Python 3.10+
- Ollama (Local LLM runtime)
- LLaMA 3.2 / Gemma / Qwen models
- Requests (HTTP client)

--------------------------------------------------

SYSTEM REQUIREMENTS
- OS: Windows / macOS / Linux
- RAM: 16 GB recommended
- GPU: Optional (CPU works fine)
- Python 3.10 or higher

--------------------------------------------------

SETUP GUIDE (STEP-BY-STEP)

1. INSTALL PYTHON
Download from:
https://www.python.org/downloads/

IMPORTANT: Check "Add Python to PATH" during installation.

Verify:
python --version

--------------------------------------------------

2. INSTALL OLLAMA
Download from:
https://ollama.com

Verify:
ollama --version

--------------------------------------------------

3. PULL A MODEL (ONE TIME)
Recommended model:
ollama pull llama3.2:latest

Check installed models:
ollama list

--------------------------------------------------

4. CREATE PROJECT FOLDER
mkdir ai-email-assistant
cd ai-email-assistant

--------------------------------------------------

5. CREATE VIRTUAL ENVIRONMENT
python -m venv .venv
.venv\Scripts\activate

You should see:
(.venv)

--------------------------------------------------

6. INSTALL DEPENDENCIES
pip install requests

--------------------------------------------------

7. CREATE APPLICATION FILE
Create a file named:
ollama_email_assistant.py

Paste the Python code from this repository.

--------------------------------------------------

8. RUN THE APPLICATION
python ollama_email_assistant.py

Paste the email text.
Press ENTER on an empty line to finish.
The AI-generated summary and reply will be shown.

--------------------------------------------------

EXAMPLE INPUT

We are still facing intermittent login issues in the production environment.
Please let us know the root cause and when we can expect a permanent fix.
Also confirm if there is any workaround.

--------------------------------------------------

EXAMPLE OUTPUT

SUMMARY:
- Intermittent login issues in production
- Root cause and ETA requested
- Workaround requested

REPLY:
Thank you for the update. We are currently investigating the issue and will
share root cause details and a confirmed ETA shortly.

QUESTIONS:
- When did the issue start?
- Are all users affected?

--------------------------------------------------

FUTURE IMPROVEMENTS
- JSON output for automation (n8n / Zapier)
- Batch email processing from files
- Simple web UI (Streamlit)
- Outlook / Whats
