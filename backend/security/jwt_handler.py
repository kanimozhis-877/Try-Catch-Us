from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import JWT_SECRET, JWT_EXPIRES_MINUTES
def create_token(user_id, role, language="en"):
    exp = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRES_MINUTES)
    return jwt.encode({"sub": str(user_id), "role": role, "language": language, "exp": exp}, JWT_SECRET, algorithm="HS256")
