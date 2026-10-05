from pydantic import BaseModel
class LabResultCreate(BaseModel):
    patient_id: str
    test_name: str
    value: str
    unit: str = ""
    reference_range: str = ""
    test_date: str | None = None
