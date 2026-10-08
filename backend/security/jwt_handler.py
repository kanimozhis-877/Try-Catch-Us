from datetime import (
    datetime,
    timedelta,
    timezone
)

from jose import jwt

from app.config import (
    JWT_SECRET,
    JWT_EXPIRES_MINUTES
)


def create_token(
    user_id,
    role,
    language="en"
):

    expiry = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=JWT_EXPIRES_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "role": role,
        "language": language,
        "exp": expiry
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm="HS256"
    )