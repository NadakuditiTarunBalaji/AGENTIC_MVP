from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.vehicle_service import fetch_vehicle_data

router = APIRouter(
    prefix="/api/vehicle-data",
    tags=["Vehicle Data"]
)

@router.get("/")
def get_vehicle_data(db: Session = Depends(get_db)):
    return fetch_vehicle_data(db)