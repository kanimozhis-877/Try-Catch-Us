from pymongo import MongoClient

from app.config import (
    MONGO_URI,
    MONGO_DB
)


client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)

db = client[MONGO_DB]


def connect_db():

    client.admin.command("ping")

    create_indexes()

    print(
        "MongoDB connected successfully"
    )

    return db


def close_db():

    client.close()

    print(
        "MongoDB connection closed"
    )


def create_indexes():

    db.users.create_index(
        "email",
        unique=True
    )

    db.patients.create_index(
        "patient_id",
        unique=True
    )

    db.patients.create_index(
        "user_id",
        unique=True
    )

    db.reports.create_index(
        [
            ("patient_id", 1),
            ("created_at", -1)
        ]
    )

    db.qr_sessions.create_index(
        "token",
        unique=True
    )

    db.qr_sessions.create_index(
        "expires_at",
        expireAfterSeconds=0
    )