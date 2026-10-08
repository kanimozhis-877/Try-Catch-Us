from fastapi import (
    APIRouter,
    Depends
)

from app.dependencies import (
    get_current_user
)

from database.mongodb import db

from utils.response import serialize


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard(
    user=Depends(get_current_user)
):

    role = user["role"]


    if role == "doctor":

        return {

            "role": "doctor",

            "patient_count":
                db.patients.count_documents({}),

            "report_count":
                db.reports.count_documents({})
        }


    patient = db.patients.find_one(
        {
            "user_id":
                user["sub"]
        }
    )


    patient_id = (
        patient["patient_id"]
        if patient
        else None
    )


    report_count = 0


    if patient_id:

        report_count = (
            db.reports.count_documents(
                {
                    "patient_id":
                        patient_id
                }
            )
        )


    return {

        "role": "patient",

        "patient":
            serialize(patient)
            if patient
            else None,

        "patient_id":
            patient_id,

        "report_count":
            report_count
    }