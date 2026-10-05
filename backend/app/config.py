import os
from pathlib import Path
from dotenv import load_dotenv

# Find the project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Explicitly load the .env file from the project root
ENV_FILE = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_FILE, override=True)

APP_NAME = os.getenv(
    "APP_NAME",
    "Clinical Context AI Backend"
)

MONGO_URI = os.getenv("MONGO_URI")

MONGO_DB = os.getenv(
    "MONGO_DB",
    "clinical_context_ai"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET",
    "change-this-secret"
)

JWT_EXPIRES_MINUTES = int(
    os.getenv("JWT_EXPIRES_MINUTES", "120")
)

CORS_ORIGINS = [
    x.strip()
    for x in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://localhost:3000"
    ).split(",")
    if x.strip()
]

UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR",
    "uploads"
)

MAX_UPLOAD_MB = int(
    os.getenv("MAX_UPLOAD_MB", "10")
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)

# Safety check
if not MONGO_URI:
    raise RuntimeError(
        f"MONGO_URI is missing. Please check your .env file at: {ENV_FILE}"
    )

# Prevent accidentally using local MongoDB
if "localhost:27017" in MONGO_URI:
    raise RuntimeError(
        "MONGO_URI is still pointing to localhost:27017. "
        "Please check your .env file."
    )