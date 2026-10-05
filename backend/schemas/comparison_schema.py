from pydantic import BaseModel
class ComparisonRequest(BaseModel):
    patient_id: str
    previous_report_id: str
    current_report_id: str
