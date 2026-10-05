from fastapi import APIRouter,Depends
from app.dependencies import get_current_user,require_role
from schemas.patient_schema import PatientCreate
from services.patient_service import create_patient,get_patient,list_patients
router=APIRouter(prefix="/patients",tags=["Patients"])
@router.post("")
def create(data:PatientCreate,user=Depends(require_role("doctor","patient"))): return create_patient(data,user["sub"])
@router.get("")
def list_all(user=Depends(require_role("doctor"))): return list_patients()
@router.get("/{patient_id}")
def get(patient_id:str,user=Depends(get_current_user)): return get_patient(patient_id)
