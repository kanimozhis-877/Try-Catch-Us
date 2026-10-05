from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.lab_schema import LabResultCreate
from services.lab_service import create,list_results
router=APIRouter(prefix="/lab-results",tags=["Lab Results"])
@router.post("")
def create_lab(data:LabResultCreate,user=Depends(get_current_user)): return create(data,user)
@router.get("/patient/{patient_id}")
def labs(patient_id:str,user=Depends(get_current_user)): return list_results(patient_id)
