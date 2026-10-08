from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import BaseModel

from services.patient_service import (
    get_my_profile,
    update_my_profile,
    upload_report,
    get_my_reports,
    get_report,
    delete_report,
)


router = APIRouter(
    prefix="/api/patient",
    tags=["Patient"]
)


# ============================================================
# TEMPORARY CURRENT USER
# ============================================================

def get_current_patient():
    """
    Temporary patient object.

    Later this should be replaced with your JWT authentication
    dependency from auth_service.py.
    """

    return {
        "_id": "demo-patient-id",
        "name": "Demo Patient",
        "email": "patient@example.com",
        "phone": "",
        "age": None,
        "gender": "",
        "role": "patient"
    }


# ============================================================
# PROFILE SCHEMA
# ============================================================

class ProfileUpdate(BaseModel):
    name: str = ""
    phone: str = ""
    age: int | None = None
    gender: str = ""


# ============================================================
# GET PROFILE
# ============================================================

@router.get("/profile")
async def my_profile(
    current_user=Depends(get_current_patient)
):
    return get_my_profile(current_user)


# ============================================================
# UPDATE PROFILE
# ============================================================

@router.put("/profile")
async def update_profile(
    profile_data: ProfileUpdate,
    current_user=Depends(get_current_patient)
):
    return update_my_profile(
        current_user,
        profile_data
    )


# ============================================================
# UPLOAD MEDICAL REPORT
# ============================================================

@router.post("/reports/upload")
async def upload_patient_report(
    file: UploadFile = File(...),
    current_user=Depends(get_current_patient)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    allowed_extensions = {
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg"
    }

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, PNG, JPG and JPEG files are allowed"
        )

    upload_directory = Path("uploads")

    upload_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = upload_directory / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(file_content)

    return upload_report(
        current_user,
        file.filename,
        str(file_path)
    )


# ============================================================
# GET ALL REPORTS
# ============================================================

@router.get("/reports")
async def my_reports(
    current_user=Depends(get_current_patient)
):
    return get_my_reports(current_user)


# ============================================================
# GET SINGLE REPORT
# ============================================================

@router.get("/reports/{report_id}")
async def single_report(
    report_id: str,
    current_user=Depends(get_current_patient)
):
    return get_report(
        current_user,
        report_id
    )


# ============================================================
# DELETE REPORT
# ============================================================

@router.delete("/reports/{report_id}")
async def remove_report(
    report_id: str,
    current_user=Depends(get_current_patient)
):
    return delete_report(
        current_user,
        report_id
    )