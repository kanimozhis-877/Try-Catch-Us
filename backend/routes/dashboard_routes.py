from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from database.mongodb import db
router=APIRouter(prefix="/dashboard",tags=["Dashboard"])
@router.get("")
def dashboard(user=Depends(get_current_user)):
    if user.get("role")=="doctor": return {"role":"doctor","patient_count":db.patients.count_documents({}),"report_count":db.reports.count_documents({})}
    p=db.patients.find_one({"user_id":user["sub"]})
    pid=p.get("patient_id") if p else None
    return {"role":"patient","patient":p,"patient_id":pid,"report_count":db.reports.count_documents({"patient_id":pid}) if pid else 0}
