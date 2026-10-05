from fastapi import HTTPException
from database.mongodb import db
from utils.response import serialize
from datetime import datetime, timezone

def create(data,user):
    d=data.model_dump(); d.update({"created_by":user["sub"],"created_at":datetime.now(timezone.utc)}); r=db.reports.insert_one(d); d["_id"]=r.inserted_id; return serialize(d)
def list_reports(patient_id): return serialize(list(db.reports.find({"patient_id":patient_id}).sort("created_at",-1)))
def get_report(report_id):
    from bson import ObjectId
    try:r=db.reports.find_one({"_id":ObjectId(report_id)})
    except Exception:r=None
    if not r: raise HTTPException(404,"Report not found")
    return serialize(r)
