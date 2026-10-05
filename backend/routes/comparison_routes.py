from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.comparison_schema import ComparisonRequest
from services.comparison_service import compare
router=APIRouter(prefix="/comparison",tags=["Comparison"])
@router.post("")
def compare_reports(data:ComparisonRequest,user=Depends(get_current_user)): return compare(data.previous_report_id,data.current_report_id)
