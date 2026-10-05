from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pathlib import Path
from app.config import APP_NAME,CORS_ORIGINS,UPLOAD_DIR
from database.mongodb import connect_db,close_db
from routes.auth_routes import router as auth_router
from routes.doctor_routes import router as doctor_router
from routes.patient_routes import router as patient_router
from routes.dashboard_routes import router as dashboard_router
from routes.language_routes import router as language_router
from routes.medical_record_routes import router as record_router
from routes.report_routes import router as report_router
from routes.upload_routes import router as upload_router
from routes.lab_result_routes import router as lab_router
from routes.comparison_routes import router as comparison_router
from routes.analysis_routes import router as analysis_router
from routes.ai_routes import router as ai_router
from routes.qr_routes import router as qr_router
from routes.emergency_routes import router as emergency_router
from routes.health_routes import router as health_router

@asynccontextmanager
async def lifespan(app):
    Path(UPLOAD_DIR).mkdir(parents=True,exist_ok=True)
    connect_db(); yield; close_db()

app=FastAPI(title=APP_NAME,version="1.0.0",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=CORS_ORIGINS,allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
for r in [health_router,auth_router,doctor_router,patient_router,dashboard_router,language_router,record_router,report_router,upload_router,lab_router,comparison_router,analysis_router,ai_router,qr_router,emergency_router]: app.include_router(r,prefix="/api")
@app.get("/")
def root(): return {"message":"Clinical Context AI Backend is running","docs":"/docs"}
