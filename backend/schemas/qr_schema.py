from pydantic import BaseModel, Field
class QRCreateRequest(BaseModel):
    patient_id: str
    minutes: int = Field(default=10, ge=1, le=10)
class QRAccessRequest(BaseModel):
    qr_token: str
