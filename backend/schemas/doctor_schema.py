from pydantic import BaseModel
class DoctorCreate(BaseModel):
    name: str
    specialization: str = ""
    license_number: str = ""
