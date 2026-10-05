from database.mongodb import db
from utils.response import serialize
def create(data,user):
    d=data.model_dump(); d["created_by"]=user["sub"]; r=db.lab_results.insert_one(d); d["_id"]=r.inserted_id; return serialize(d)
def list_results(patient_id): return serialize(list(db.lab_results.find({"patient_id":patient_id}).sort("created_at",-1)))
