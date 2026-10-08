from datetime import (
    datetime,
    timezone
)

from fastapi import HTTPException

from bson import ObjectId

from database.mongodb import db

from utils.response import serialize


def create_report(
    data,
    user
):

    patient = db.patients.find_one(
        {
            "patient_id":
                data.patient_id
        }
    )


    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )


    report = {

        "patient_id":
            data.patient_id,

        "report_type":
            data.report_type,

        "title":
            data.title,

        "content":
            data.content,

        "notes":
            data.notes,

        "file_name":
            data.file_name,

        "report_date":
            data.report_date,

        "created_by":
            user["sub"],

        "created_at":
            datetime.now(
                timezone.utc
            ),

        "doctor_reviewed":
            False
    }


    result = db.reports.insert_one(
        report
    )


    report["_id"] = result.inserted_id


    return serialize(
        report
    )


def list_reports(
    patient_id
):

    reports = list(
        db.reports.find(
            {
                "patient_id":
                    patient_id
            }
        ).sort(
            "created_at",
            -1
        )
    )


    return serialize(
        reports
    )


def get_report(
    report_id
):

    try:

        report = db.reports.find_one(
            {
                "_id":
                    ObjectId(
                        report_id
                    )
            }
        )

    except Exception:

        report = None


    if not report:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )


    return serialize(
        report
    )