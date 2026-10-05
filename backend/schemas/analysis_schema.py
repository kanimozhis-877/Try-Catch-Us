from pydantic import BaseModel
class AnalysisRequest(BaseModel):
    patient_id: str
    question: str = "Summarize the patient's current clinical context for clinician review."
