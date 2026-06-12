from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.models.vehicle_data import VehicleData
from backend.models.dtc import DTC
from backend.models.fault import Fault
from backend.models.can_frame import CANFrame
import json

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    # Get latest vehicle data
    latest = (
        db.query(VehicleData)
        .order_by(VehicleData.timestamp.desc())
        .first()
    )

    # Count totals
    total_dtcs = db.query(DTC).count()
    total_faults = db.query(Fault).count()
    total_can_frames = db.query(CANFrame).count()

    # Calculate real health score from latest data
    health_score = 100.0
    issues = []

    if latest:
        if latest.coolant_temp and latest.coolant_temp > 95:
            health_score -= 20
            issues.append("Engine overheating")
        if latest.rpm and latest.rpm > 6000:
            health_score -= 15
            issues.append("High RPM")
        if latest.battery_temp and latest.battery_temp > 45:
            health_score -= 10
            issues.append("High battery temperature")

    if health_score >= 80:
        status = "Healthy"
    elif health_score >= 60:
        status = "Warning"
    else:
        status = "Critical"

    return {
        "health_score": max(health_score, 0),
        "status": status,
        "issues": issues,
        "total_dtcs": total_dtcs,
        "total_faults": total_faults,
        "total_can_frames": total_can_frames,
        "latest_telemetry": {
            "rpm": latest.rpm if latest else 0,
            "speed": latest.speed if latest else 0,
            "coolant_temp": latest.coolant_temp if latest else 0,
            "battery_temp": latest.battery_temp if latest else 0,
        } if latest else {}
    }


@router.get("/health-history")
def get_health_history(
    limit: int = 20,
    db: Session = Depends(get_db)
):
    records = (
        db.query(VehicleData)
        .order_by(VehicleData.timestamp.desc())
        .limit(limit)
        .all()
    )
    return records


@router.get("/active-faults")
def get_active_faults(db: Session = Depends(get_db)):
    faults = db.query(Fault).filter(
        Fault.severity.in_(["High", "Critical"])
    ).all()
    return faults