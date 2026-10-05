from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from schemas.language_schema import LanguageUpdate
from services.language_service import update,get
router=APIRouter(prefix="/language",tags=["Language"])
@router.put("")
def update_language(data:LanguageUpdate,user=Depends(get_current_user)): return update(user["sub"],data.language)
@router.get("")
def get_language(user=Depends(get_current_user)): return get(user["sub"])
