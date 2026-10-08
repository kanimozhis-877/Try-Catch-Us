import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE, override=True)


APP_NAME = os.getenv(
    "APP_NAME",
    "LIFE LINK Backend"
)

MONGO_URI = os.getenv("MONGO_URI")

MONGO_DB = os.getenv(
    "MONGO_DB",
    "life_link"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET",
    "change-this-secret"
)

JWT_EXPIRES_MINUTES = int(
    os.getenv(
        "JWT_EXPIRES_MINUTES",
        "120"
    )
)

CORS_ORIGINS = [
    item.strip()
    for item in os.getenv(
        "CORS_ORIGINS",
        "http://127.0.0.1:5500,http://localhost:5500"
    ).split(",")
    if item.strip()
]

UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR",
    "uploads"
)

MAX_UPLOAD_MB = int(
    os.getenv(
        "MAX_UPLOAD_MB",
        "10"
    )
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)


if not MONGO_URI:
    raise RuntimeError(
        "MONGO_URI is missing in backend/.env"
    )