from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.analysis_schema import AnalysisRequest
from services.ai_service import analyze
router=APIRouter(prefix="/ai",tags=["AI Analysis"])
@router.post("/analyze")
def analyze_patient(data:AnalysisRequest,user=Depends(get_current_user)): return analyze(data.patient_id,data.question)
