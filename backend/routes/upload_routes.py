from pathlib import Path
from uuid import uuid4

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from app.dependencies import (
    get_current_user
)

from app.config import (
    UPLOAD_DIR,
    MAX_UPLOAD_MB
)


router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"]
)


ALLOWED_TYPES = {

    "application/pdf",

    "image/jpeg",

    "image/png"
}


@router.post("")
async def upload_report(
    file: UploadFile = File(...),

    user=Depends(
        get_current_user
    )
):

    if file.content_type not in \
            ALLOWED_TYPES:

        raise HTTPException(
            status_code=400,
            detail=
            "Only PDF, JPG and PNG files are allowed"
        )


    content = await file.read()


    max_size = (
        MAX_UPLOAD_MB
        * 1024
        * 1024
    )


    if len(content) > max_size:

        raise HTTPException(
            status_code=413,
            detail=
            f"File must be below {MAX_UPLOAD_MB} MB"
        )


    folder = (
        Path(UPLOAD_DIR)
        / "reports"
    )


    folder.mkdir(
        parents=True,
        exist_ok=True
    )


    original_name = (
        file.filename
        or "medical_report"
    )


    safe_name = (
        f"{uuid4().hex}_"
        f"{original_name}"
    )


    file_path = (
        folder /
        safe_name
    )


    file_path.write_bytes(
        content
    )


    return {

        "message":
            "Report uploaded successfully",

        "filename":
            safe_name,

        "original_filename":
            original_name,

        "content_type":
            file.content_type,

        "size":
            len(content)
    }