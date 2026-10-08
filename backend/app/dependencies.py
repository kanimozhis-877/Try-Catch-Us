from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from jose import (
    jwt,
    JWTError
)

from app.config import JWT_SECRET


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials =
    Depends(security)
):

    try:

        payload = jwt.decode(
            credentials.credentials,
            JWT_SECRET,
            algorithms=["HS256"]
        )

        if not payload.get("sub"):

            raise ValueError()

        return payload

    except (
        JWTError,
        ValueError
    ):

        raise HTTPException(
            status_code=
            status.HTTP_401_UNAUTHORIZED,

            detail=
            "Invalid or expired token"
        )


def require_role(*roles):

    def checker(
        user=Depends(get_current_user)
    ):

        if user.get("role") not in roles:

            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return user

    return checker