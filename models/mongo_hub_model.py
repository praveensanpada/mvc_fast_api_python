# === models/mongo_hub_model.py ===
from pymongo import MongoClient
from config.settings import POST_MONGO_URI, POST_MONGO_DB_NAME
from config.logger import get_logger

logger = get_logger(__name__)

class MongoHubModel:
    def __init__(self):
        try:
            self.write_client = MongoClient(POST_MONGO_URI)
            self.write_db = self.write_client[POST_MONGO_DB_NAME]

            logger.info("MongoDB read/write connections initialized")
        except Exception as e:
            logger.error(f"MongoDB connection error: {e}")
            raise

    def insert_venue(self, data: dict):
        try:
            result = self.write_db.temp_venue_store.insert_one(data)
            logger.info(f"Inserted venue document with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error inserting venue: {e}")
            return None