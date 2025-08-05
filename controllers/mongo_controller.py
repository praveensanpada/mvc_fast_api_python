# === controllers/mongo_controller.py ===
from models.mongo_model import MongoModel

mongo_model = MongoModel()

def get_venue_by_uid(venue_uid: str):
    row = mongo_model.get_venue_by_uid(venue_uid)
    if row:
        return {
            "venue_uid": venue_uid,
            "record_found": True,
            "data": row
        }
    else:
        return {
            "venue_uid": venue_uid,
            "record_found": False,
            "message": "No data found for given venue_uid"
        }