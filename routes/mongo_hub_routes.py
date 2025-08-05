# === routes/mongo_hub_routes.py ===
from fastapi import APIRouter
from controllers.mongo_hub_controller import  insert_venue_data

router = APIRouter()

@router.post("/add_venue")
def write_venue(payload: dict):
    return {"inserted_id": insert_venue_data(payload)}