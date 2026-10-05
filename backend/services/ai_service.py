from ai.context_engine import build_context
from ai.ollama_client import ask_ollama

def analyze(patient_id,question):
    context=build_context(patient_id)
    prompt=f"""You are a clinical decision-support assistant. Do not diagnose, prescribe, or replace a clinician. Identify observations, changes, missing information, possible risks to review, and useful questions for a clinician.\n\nQuestion: {question}\nPatient context:\n{context}"""
    answer=ask_ollama(prompt)
    return {"patient_id":patient_id,"answer":answer,"disclaimer":"AI output is decision support only. A qualified healthcare professional must verify all findings and make clinical decisions."}
