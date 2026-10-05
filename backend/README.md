# Clinical Context AI Backend

FastAPI + MongoDB backend for the Clinical Context AI project.

## Run on Windows

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
Copy-Item .env.example .env
pip install -r requirements.txt
python run.py
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

MongoDB must be running. Change `MONGO_URI` in `.env` for MongoDB Atlas.

Swagger: http://127.0.0.1:8000/docs

## Ollama (optional)

```powershell
ollama serve
ollama pull llama3.2
```

## Main endpoints

- POST `/api/auth/register`
- POST `/api/auth/login`
- GET `/api/dashboard`
- POST `/api/patients`
- GET `/api/patients/{patient_id}`
- POST `/api/reports`
- GET `/api/reports/patient/{patient_id}`
- POST `/api/lab-results`
- POST `/api/medical-records`
- POST `/api/comparison`
- POST `/api/ai/analyze`
- POST `/api/qr/create`
- POST `/api/emergency/access`
- PUT `/api/language`
- POST `/api/uploads`

AI output is decision support only and must be reviewed by a qualified clinician.
