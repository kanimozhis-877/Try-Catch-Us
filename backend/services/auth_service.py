from fastapi import HTTPException
from database.repositories.user_repository import UserRepository
from security.password_handler import hash_password, verify_password
from security.jwt_handler import create_token
from utils.response import serialize
repo=UserRepository()

def register(data):
    if data.role not in ("patient","doctor"): raise HTTPException(400,"Role must be patient or doctor")
    if repo.find_one({"email":data.email}): raise HTTPException(409,"Email already registered")
    uid=repo.insert({"name":data.name,"email":data.email,"password":hash_password(data.password),"role":data.role,"language":"en"})
    return {"message":"Registration successful","user_id":uid}

def login(data):
    user=repo.find_one({"email":data.email})
    if not user or not verify_password(data.password,user["password"]): raise HTTPException(401,"Invalid email or password")
    token=create_token(user["_id"],user["role"],user.get("language","en"))
    return {"access_token":token,"token_type":"bearer","role":user["role"],"user":serialize({"id":user["_id"],"name":user["name"],"email":user["email"],"language":user.get("language","en")})}
