from bson import ObjectId
from datetime import datetime, timezone
from database.mongodb import db

class BaseRepository:
    def __init__(self, collection): self.collection = db[collection]
    def _id(self, value):
        try: return ObjectId(value)
        except Exception: return value
    def get(self, value): return self.collection.find_one({"_id": self._id(value)})
    def find_one(self, query): return self.collection.find_one(query)
    def find(self, query=None, sort=None, limit=100):
        cur = self.collection.find(query or {})
        if sort: cur = cur.sort(sort)
        return list(cur.limit(limit))
    def insert(self, data):
        data = dict(data); data.setdefault("created_at", datetime.now(timezone.utc))
        result = self.collection.insert_one(data); return str(result.inserted_id)
    def update(self, value, data):
        data = dict(data); data["updated_at"] = datetime.now(timezone.utc)
        result = self.collection.update_one({"_id": self._id(value)}, {"$set": data})
        return result.modified_count > 0
    def delete(self, value): return self.collection.delete_one({"_id": self._id(value)}).deleted_count > 0
