from pydantic import BaseModel, EmailStr, Field
class RegisterRequest(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=6)
    role: str = "patient"
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
