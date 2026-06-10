from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.dashboard_service import (
    get_dashboard_summary,
    get_vehicle_health,
    get_analytics
)

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return get_dashboard_summary(db)


@router.get("/vehicle-health")
def vehicle_health(db: Session = Depends(get_db)):
    return get_vehicle_health(db)


@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    return get_analytics(db)