import requests
from app.config import OLLAMA_URL, OLLAMA_MODEL

def ask_ollama(prompt):
    try:
        r=requests.post(OLLAMA_URL,json={"model":OLLAMA_MODEL,"prompt":prompt,"stream":False},timeout=60)
        r.raise_for_status(); return r.json().get("response", "")
    except Exception:
        return "AI service is currently unavailable. Please review the patient's records manually."
