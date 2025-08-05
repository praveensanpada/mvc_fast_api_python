# === controllers/mongo_hub_controller.py ===
from models.mongo_hub_model import MongoHubModel

mongo_hub_model = MongoHubModel()

def insert_venue_data(payload: dict):
    return mongo_hub_model.insert_venue(payload)