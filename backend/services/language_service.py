from fastapi import HTTPException
from database.mongodb import db

def update(user_id,language):
    if language not in ("en","ta"): raise HTTPException(400,"Supported languages: en, ta")
    from bson import ObjectId
    db.users.update_one({"_id":ObjectId(user_id)},{"$set":{"language":language}})
    return {"language":language}
def get(user_id):
    from bson import ObjectId
    u=db.users.find_one({"_id":ObjectId(user_id)})
    return {"language":u.get("language","en") if u else "en"}
