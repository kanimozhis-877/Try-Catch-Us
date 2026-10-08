from datetime import datetime
from typing import Any


def _get_value(obj: Any, key: str, default=None):
    """
    Get a value from either a dictionary or an object.
    """
    if isinstance(obj, dict):
        return obj.get(key, default)

    return getattr(obj, key, default)


def _user_id(current_user):
    """
    Get the user's ID from either MongoDB-style data
    or an object/model.
    """
    user_id = _get_value(current_user, "_id")

    if user_id is None:
        user_id = _get_value(current_user, "id")

    return str(user_id) if user_id is not None else None


def get_my_profile(current_user):
    """
    Get the currently logged-in patient's profile.
    """

    return {
        "success": True,
        "message": "Patient profile fetched successfully",
        "profile": {
            "id": _user_id(current_user),
            "name": _get_value(current_user, "name", ""),
            "email": _get_value(current_user, "email", ""),
            "phone": _get_value(current_user, "phone", ""),
            "age": _get_value(current_user, "age"),
            "gender": _get_value(current_user, "gender", ""),
            "role": _get_value(current_user, "role", "patient"),
        }
    }


def update_my_profile(current_user, profile_data):
    """
    Update patient profile data.

    This is currently an in-memory service response.
    Connect your database update function here later.
    """

    name = _get_value(profile_data, "name", "")
    phone = _get_value(profile_data, "phone", "")
    age = _get_value(profile_data, "age")
    gender = _get_value(profile_data, "gender", "")

    return {
        "success": True,
        "message": "Patient profile updated successfully",
        "profile": {
            "id": _user_id(current_user),
            "name": name,
            "email": _get_value(current_user, "email", ""),
            "phone": phone,
            "age": age,
            "gender": gender,
            "role": "patient",
        }
    }


def upload_report(current_user, filename: str, file_path: str):
    """
    Store uploaded report information.

    The actual file is saved by the route.
    This service prepares the response data.
    """

    return {
        "success": True,
        "message": "Medical report uploaded successfully",
        "report": {
            "patient_id": _user_id(current_user),
            "filename": filename,
            "file_path": file_path,
            "uploaded_at": datetime.now().isoformat(),
        }
    }


def get_my_reports(current_user):
    """
    Get reports belonging to the logged-in patient.

    Replace this with your database query when the DB layer is connected.
    """

    return {
        "success": True,
        "message": "Patient reports fetched successfully",
        "reports": []
    }


def get_report(current_user, report_id: str):
    """
    Get one report belonging to the patient.
    """

    return {
        "success": True,
        "message": "Report fetched successfully",
        "report": {
            "id": report_id,
            "patient_id": _user_id(current_user)
        }
    }


def delete_report(current_user, report_id: str):
    """
    Delete a patient's report.
    """

    return {
        "success": True,
        "message": "Report deleted successfully",
        "report_id": report_id
    }