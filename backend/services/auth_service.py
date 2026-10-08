from fastapi import HTTPException

from database.mongodb import db

from security.password_handler import (
    hash_password,
    verify_password
)

from security.jwt_handler import create_token

from utils.response import serialize

from utils.patient_id_generator import (
    generate_patient_id
)


def register(data):

    if data.role not in (
        "patient",
        "doctor"
    ):

        raise HTTPException(
            status_code=400,
            detail=
            "Role must be patient or doctor"
        )


    existing = db.users.find_one(
        {"email": data.email}
    )

    if existing:

        raise HTTPException(
            status_code=409,
            detail=
            "Email already registered"
        )


    user = {

        "name": data.name,

        "email": data.email,

        "password":
            hash_password(
                data.password
            ),

        "role": data.role,

        "language": "en"
    }


    result = db.users.insert_one(
        user
    )


    user_id = result.inserted_id


    # Automatically create patient profile
    if data.role == "patient":

        patient = {

            "patient_id":
                generate_patient_id(),

            "user_id":
                str(user_id),

            "name":
                data.name,

            "age": 0,

            "gender":
                "Not specified",

            "phone": "",

            "language": "en",

            "blood_group": "",

            "emergency_contact": ""
        }


        db.patients.insert_one(
            patient
        )


    return {

        "message":
            "Registration successful",

        "user_id":
            str(user_id)
    }


def login(data):

    user = db.users.find_one(
        {"email": data.email}
    )


    if not user:

        raise HTTPException(
            status_code=401,
            detail=
            "Invalid email or password"
        )


    if not verify_password(
        data.password,
        user["password"]
    ):

        raise HTTPException(
            status_code=401,
            detail=
            "Invalid email or password"
        )


    token = create_token(
        user["_id"],
        user["role"],
        user.get(
            "language",
            "en"
        )
    )


    return {

        "access_token":
            token,

        "token_type":
            "bearer",

        "role":
            user["role"],

        "user":
            serialize({

                "id":
                    user["_id"],

                "name":
                    user["name"],

                "email":
                    user["email"],

                "language":
                    user.get(
                        "language",
                        "en"
                    )
            })
    }