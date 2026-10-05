from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.qr_schema import QRCreateRequest
from services.qr_service import create
router=APIRouter(prefix="/qr",tags=["QR"])
@router.post("/create")
def create_qr(data:QRCreateRequest,user=Depends(get_current_user)): return create(data.patient_id,data.minutes)
