from pydantic import BaseModel
class MedicalRecordCreate(BaseModel):
    patient_id: str
    diagnosis: str = ""
    notes: str = ""
    doctor_name: str = ""
