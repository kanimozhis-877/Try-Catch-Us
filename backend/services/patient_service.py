from fastapi import HTTPException
from database.mongodb import db
from utils.patient_id_generator import generate_patient_id
from utils.response import serialize

def create_patient(data, user_id):
    pid=generate_patient_id()
    while db.patients.find_one({"patient_id":pid}): pid=generate_patient_id()
    doc=data.model_dump(); doc.update({"patient_id":pid,"user_id":user_id})
    db.patients.insert_one(doc); return serialize(doc)

def get_patient(patient_id):
    p=db.patients.find_one({"patient_id":patient_id})
    if not p: raise HTTPException(404,"Patient not found")
    return serialize(p)

def list_patients(): return serialize(list(db.patients.find({}).limit(100)))
