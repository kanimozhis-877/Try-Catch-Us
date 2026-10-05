from fastapi import APIRouter
from schemas.auth_schema import RegisterRequest,LoginRequest
from services.auth_service import register,login
router=APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/register")
def register_user(data:RegisterRequest): return register(data)
@router.post("/login")
def login_user(data:LoginRequest): return login(data)
