from database.mongodb import db
from bson import ObjectId
from utils.response import serialize

def compare(previous_id,current_id):
    def get(i):
        try:return db.reports.find_one({"_id":ObjectId(i)})
        except:return None
    old,new=get(previous_id),get(current_id)
    if not old or not new: return {"message":"One or both reports were not found"}
    return {"previous":serialize(old),"current":serialize(new),"summary":"Compare the previous and current report values/content. Clinical interpretation must be done by a qualified clinician."}
