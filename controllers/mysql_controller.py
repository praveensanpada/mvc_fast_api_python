# === controllers/mysql_controller.py ===
from models.mysql_model import MySQLModel

mysql_model = MySQLModel()

def get_mysql_row_by_season_uid(season_game_uid: str):
    row = mysql_model.fetch_mysql_data(season_game_uid)
    if row:
        return {
            "season_game_uid": season_game_uid,
            "record_found": True,
            "data": row
        }
    else:
        return {
            "season_game_uid": season_game_uid,
            "record_found": False,
            "message": "No data found for given season_game_uid"
        }
