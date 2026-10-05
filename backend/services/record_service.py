from database.mongodb import db
from utils.response import serialize
def create(data, user):
    d=data.model_dump(); d["created_by"]=user["sub"]; r=db.medical_records.insert_one(d); d["_id"]=r.inserted_id; return serialize(d)
def list_records(patient_id): return serialize(list(db.medical_records.find({"patient_id":patient_id}).sort("created_at",-1)))
