from fastapi import FastAPI

from routes.auth_routes import router as auth_router
from routes.patient_routes import router as patient_router


app = FastAPI(
    title="MediSense-AI",
    description="AI-powered healthcare information analysis system",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(patient_router)


@app.get("/")
async def root():
    return {
        "message": "MediSense-AI Backend is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }