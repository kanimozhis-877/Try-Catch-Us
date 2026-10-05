from fastapi import APIRouter,UploadFile,File,Depends,HTTPException
from app.dependencies import get_current_user
from app.config import UPLOAD_DIR,MAX_UPLOAD_MB
from pathlib import Path
import uuid
router=APIRouter(prefix="/uploads",tags=["Uploads"])
@router.post("")
async def upload(file:UploadFile=File(...),user=Depends(get_current_user)):
    data=await file.read()
    if len(data)>MAX_UPLOAD_MB*1024*1024: raise HTTPException(413,"File too large")
    folder=Path(UPLOAD_DIR)/"reports"; folder.mkdir(parents=True,exist_ok=True)
    name=f"{uuid.uuid4().hex}_{file.filename}"; path=folder/name; path.write_bytes(data)
    return {"filename":name,"path":str(path),"content_type":file.content_type,"size":len(data)}
