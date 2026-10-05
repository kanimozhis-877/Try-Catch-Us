from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.report_schema import ReportCreate
from services.report_service import create,list_reports,get_report
router=APIRouter(prefix="/reports",tags=["Reports"])
@router.post("")
def create_report(data:ReportCreate,user=Depends(get_current_user)): return create(data,user)
@router.get("/patient/{patient_id}")
def reports(patient_id:str,user=Depends(get_current_user)): return list_reports(patient_id)
@router.get("/{report_id}")
def report(report_id:str,user=Depends(get_current_user)): return get_report(report_id)
