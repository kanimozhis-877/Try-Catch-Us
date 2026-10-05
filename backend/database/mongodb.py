from pymongo import MongoClient
from app.config import MONGO_URI, MONGO_DB

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[MONGO_DB]

def connect_db():
    client.admin.command("ping")
    create_indexes()
    return db

def close_db():
    client.close()

def create_indexes():
    db.users.create_index("email", unique=True)
    db.patients.create_index("patient_id", unique=True)
    db.qr_sessions.create_index("token", unique=True)
    db.qr_sessions.create_index("expires_at", expireAfterSeconds=0)
    db.reports.create_index([("patient_id", 1), ("created_at", -1)])
    db.lab_results.create_index([("patient_id", 1), ("test_date", -1)])
