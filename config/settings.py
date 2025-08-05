# === config/settings.py ===
import os
from dotenv import load_dotenv

load_dotenv()

GET_MONGO_URI = os.getenv("GET_MONGO_URI")
GET_MONGO_DB_NAME = os.getenv("GET_MONGO_DB_NAME")
GET_MYSQL_URI = (
    f"mysql+pymysql://{os.getenv('GET_MYSQL_USER_STATS_DB')}:{os.getenv('GET_MYSQL_PASSWORD_STATS_DB')}"
    f"@{os.getenv('GET_MYSQL_HOST_STATS_DB')}:{os.getenv('GET_MYSQL_PORT_STATS_DB')}/{os.getenv('GET_MYSQL_DB_STATS_DB')}"
)

POST_MONGO_URI = os.getenv("POST_MONGO_URI")
POST_MONGO_DB_NAME = os.getenv("POST_MONGO_DB_NAME")

PORT = int(os.getenv("PORT", 8000))