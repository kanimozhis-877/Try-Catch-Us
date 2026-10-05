import secrets
from datetime import datetime,timedelta,timezone
from database.mongodb import db
from utils.response import serialize
from utils.qr_generator import make_qr
from fastapi import HTTPException

def create(patient_id,minutes=10):
    if not db.patients.find_one({"patient_id":patient_id}): raise HTTPException(404,"Patient not found")
    token=secrets.token_urlsafe(32); expires=datetime.now(timezone.utc)+timedelta(minutes=minutes)
    db.qr_sessions.insert_one({"token":token,"patient_id":patient_id,"expires_at":expires,"created_at":datetime.now(timezone.utc)})
    return {"qr_token":token,"expires_at":expires.isoformat(),"qr_png_base64":__import__('base64').b64encode(make_qr(token)).decode()}

def access(token):
    s=db.qr_sessions.find_one({"token":token})
    if not s or s["expires_at"]<=datetime.now(timezone.utc): raise HTTPException(401,"QR expired or invalid")
    p=db.patients.find_one({"patient_id":s["patient_id"]})
    reports=list(db.reports.find({"patient_id":s["patient_id"]}).sort("created_at",-1).limit(5))
    labs=list(db.lab_results.find({"patient_id":s["patient_id"]}).sort("created_at",-1).limit(10))
    return {"patient":serialize(p),"reports":serialize(reports),"lab_results":serialize(labs),"expires_at":s["expires_at"].isoformat(),"notice":"Emergency/QR view contains limited information for clinical review."}
