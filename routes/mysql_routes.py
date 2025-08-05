# === routes/mysql_routes.py ===
from fastapi import APIRouter
from controllers.mysql_controller import get_mysql_row_by_season_uid

router = APIRouter()

@router.get("/mysql_record")
def display_mysql_data(season_game_uid: str):
    return get_mysql_row_by_season_uid(season_game_uid)
