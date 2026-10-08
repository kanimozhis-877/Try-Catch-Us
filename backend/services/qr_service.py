import base64
import secrets

from datetime import (
    datetime,
    timedelta,
    timezone
)

from fastapi import HTTPException

from database.mongodb import db

from utils.qr_generator import (
    make_qr
)

from utils.response import (
    serialize
)


def create_qr(
    patient_id,
    minutes
):

    patient = db.patients.find_one(
        {
            "patient_id":
                patient_id
        }
    )


    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )


    token = secrets.token_urlsafe(
        32
    )


    expires_at = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=minutes
        )
    )


    db.qr_sessions.insert_one({

        "token":
            token,

        "patient_id":
            patient_id,

        "expires_at":
            expires_at,

        "created_at":
            datetime.now(
                timezone.utc
            )
    })


    qr_bytes = make_qr(
        token
    )


    qr_base64 = base64.b64encode(
        qr_bytes
    ).decode()


    return {

        "qr_token":
            token,

        "patient_id":
            patient_id,

        "expires_at":
            expires_at.isoformat(),

        "qr_png_base64":
            qr_base64
    }


def access_qr(
    token
):

    session = db.qr_sessions.find_one(
        {
            "token":
                token
        }
    )


    if not session:

        raise HTTPException(
            status_code=401,
            detail="Invalid QR"
        )


    if session["expires_at"] <= \
            datetime.now(timezone.utc):

        raise HTTPException(
            status_code=401,
            detail="QR expired"
        )


    patient = db.patients.find_one(
        {
            "patient_id":
                session["patient_id"]
        }
    )


    reports = list(
        db.reports.find(
            {
                "patient_id":
                    session["patient_id"]
            }
        )
        .sort(
            "created_at",
            -1
        )
        .limit(10)
    )


    return {

        "patient":
            serialize(patient),

        "reports":
            serialize(reports),

        "expires_at":
            session[
                "expires_at"
            ].isoformat(),

        "notice":
            "Temporary medical access"
    }