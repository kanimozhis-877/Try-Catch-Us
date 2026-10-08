from fastapi import (
    APIRouter,
    Depends
)

from app.dependencies import (
    get_current_user
)

from schemas.qr_schema import (
    QRCreateRequest
)

from services.qr_service import (
    create_qr
)


router = APIRouter(
    prefix="/qr",
    tags=["QR Access"]
)


@router.post("/create")
def create(
    data: QRCreateRequest,

    user=Depends(
        get_current_user
    )
):

    return create_qr(
        data.patient_id,
        data.minutes
    )