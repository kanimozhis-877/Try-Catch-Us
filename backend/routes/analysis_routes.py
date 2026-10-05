from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from services.ai_service import analyze
router=APIRouter(prefix="/analysis",tags=["Analysis"])
@router.get("/{patient_id}")
def analysis(patient_id:str,user=Depends(get_current_user)): return analyze(patient_id,"Provide a concise clinical-context summary for clinician review.")
