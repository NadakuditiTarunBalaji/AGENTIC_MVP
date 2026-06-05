from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.vehicle_service import (
    fetch_vehicle_data,
    add_vehicle
)

# Router MUST be created before using @router decorators
router = APIRouter(
    prefix="/api/vehicle-data",
    tags=["Vehicle Data"]
)

@router.get("/")
def get_vehicle_data(db: Session = Depends(get_db)):
    return fetch_vehicle_data(db)

@router.post("/")
def add_vehicle_data(
    rpm: float,
    battery_temp: float,
    coolant_temp: float,
    speed: float,
    db: Session = Depends(get_db)
):
    return add_vehicle(
        db,
        rpm,
        battery_temp,
        coolant_temp,
        speed
    )