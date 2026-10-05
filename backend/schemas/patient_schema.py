from pydantic import BaseModel, Field
class PatientCreate(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)
    gender: str
    phone: str = ""
    language: str = "en"
class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    gender: str | None = None
    phone: str | None = None
    language: str | None = None
