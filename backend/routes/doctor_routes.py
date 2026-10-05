from fastapi import APIRouter,Depends
from app.dependencies import require_role
from database.mongodb import db
from utils.response import serialize
router=APIRouter(prefix="/doctors",tags=["Doctors"])
@router.get("/dashboard")
def dashboard(user=Depends(require_role("doctor"))):
    return {"doctor":user.get("sub"),"patients":db.patients.count_documents({}),"reports":db.reports.count_documents({})}
