# === routes/mongo_routes.py ===
from fastapi import APIRouter
from controllers.mongo_controller import get_venue_by_uid

router = APIRouter()

@router.get("/get_venue_detail")
def fetch_venue(venue_uid: str):
    return get_venue_by_uid(venue_uid)