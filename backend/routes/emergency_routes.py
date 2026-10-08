from fastapi import APIRouter

from schemas.qr_schema import (
    QRAccessRequest
)

from services.qr_service import (
    access_qr
)


router = APIRouter(
    prefix="/emergency",
    tags=["Emergency"]
)


@router.post("/access")
def emergency_access(
    data: QRAccessRequest
):

    return access_qr(
        data.qr_token
    )