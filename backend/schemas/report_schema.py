from pydantic import BaseModel
class ReportCreate(BaseModel):
    patient_id: str
    report_type: str
    title: str
    content: str = ""
    report_date: str | None = None
