from fastapi import APIRouter
from schemas.qr_schema import QRAccessRequest
from services.qr_service import access
router=APIRouter(prefix="/emergency",tags=["Emergency"])
@router.post("/access")
def emergency(data:QRAccessRequest): return access(data.qr_token)
