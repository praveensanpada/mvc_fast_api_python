# === models/mongo_model.py ===
from pymongo import MongoClient
from config.settings import GET_MONGO_URI, GET_MONGO_DB_NAME, POST_MONGO_URI, POST_MONGO_DB_NAME
from config.logger import get_logger

from bson.json_util import dumps
import json

logger = get_logger(__name__)

class MongoModel:
    def __init__(self):
        try:
            self.read_client = MongoClient(GET_MONGO_URI)
            self.read_db = self.read_client[GET_MONGO_DB_NAME]

            self.write_client = MongoClient(POST_MONGO_URI)
            self.write_db = self.write_client[POST_MONGO_DB_NAME]

            logger.info("MongoDB read/write connections initialized")
        except Exception as e:
            logger.error(f"MongoDB connection error: {e}")
            raise

    def get_venue_by_uid(self, venue_uid: str):
        try:
            venue = self.read_db.rag_llm_venues.find_one({"venue_uid": venue_uid})
            logger.info(f"Fetched venue with UID {venue_uid}")
            return json.loads(dumps(venue)) if venue else {}
        except Exception as e:
            logger.error(f"Error fetching venue by UID: {e}")
            return {}

    def insert_venue(self, data: dict):
        try:
            result = self.write_db.temp_venue_store.insert_one(data)
            logger.info(f"Inserted venue document with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            logger.error(f"Error inserting venue: {e}")
            return None