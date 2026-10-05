from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.record_schema import MedicalRecordCreate
from services.record_service import create,list_records
router=APIRouter(prefix="/medical-records",tags=["Medical Records"])
@router.post("")
def create_record(data:MedicalRecordCreate,user=Depends(get_current_user)): return create(data,user)
@router.get("/{patient_id}")
def records(patient_id:str,user=Depends(get_current_user)): return list_records(patient_id)
