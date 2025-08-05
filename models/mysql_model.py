# === models/mysql_model.py ===
from sqlalchemy import create_engine, text
from config.settings import GET_MYSQL_URI
from config.logger import get_logger

from bson.json_util import dumps
import json

logger = get_logger(__name__)

class MySQLModel:
    def __init__(self):
        try:
            self.mysql_engine = create_engine(GET_MYSQL_URI)
            logger.info("Connected to MySQL and MongoDB for data dump")
        except Exception as e:
            logger.error(f"Initialization failed: {e}")
            raise

    def fetch_mysql_data(self, season_game_uid: str):
        try:
            with self.mysql_engine.connect() as conn:
                query = text("SELECT * FROM vi_stats_season WHERE es_season_game_uid = :uid")
                result = conn.execute(query, {"uid": season_game_uid})

                row = result.fetchone()
                data = dict(zip(result.keys(), row)) if row else {}
                logger.info(f"Fetched 1 row from vi_stats_season where es_season_game_uid = {season_game_uid}")
                return data
        except Exception as e:
            logger.error(f"Error fetching data from MySQL: {e}")
            return {}
        except Exception as e:
            logger.error(f"Error fetching data from MySQL: {e}")
            return []
        except Exception as e:
            logger.error(f"Error fetching data from MySQL: {e}")
            return []
