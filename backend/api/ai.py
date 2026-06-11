from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from backend.config.database import get_db
from backend.models.dtc import DTC
from backend.models.fault import Fault

router = APIRouter(
    prefix="/api/ai",
    tags=["AI Analysis"]
)


class DiagnosticRequest(BaseModel):
    vehicle_id: str
    rpm: Optional[float] = 0
    speed: Optional[float] = 0
    engine_temp: Optional[float] = 0
    battery_voltage: Optional[float] = 12.6
    fuel_level: Optional[float] = 100


@router.post("/diagnose")
def diagnose_vehicle(
    request: DiagnosticRequest,
    db: Session = Depends(get_db)
):
    issues = []
    recommendations = []
    health_score = 100.0

    # RPM check
    if request.rpm > 6000:
        issues.append({
            "parameter": "RPM",
            "value": request.rpm,
            "threshold": 6000,
            "severity": "High",
            "message": "Engine RPM critically high"
        })
        recommendations.append("Reduce engine load immediately")
        health_score -= 20

    # Engine temp check
    if request.engine_temp > 95:
        issues.append({
            "parameter": "Engine Temperature",
            "value": request.engine_temp,
            "threshold": 95,
            "severity": "Critical",
            "message": "Engine overheating detected"
        })
        recommendations.append("Stop vehicle and check coolant level")
        health_score -= 25

    # Battery voltage check
    if request.battery_voltage < 12.0:
        issues.append({
            "parameter": "Battery Voltage",
            "value": request.battery_voltage,
            "threshold": 12.0,
            "severity": "Medium",
            "message": "Low battery voltage"
        })
        recommendations.append("Check charging system and battery health")
        health_score -= 15

    # Fuel level check
    if request.fuel_level < 10:
        issues.append({
            "parameter": "Fuel Level",
            "value": request.fuel_level,
            "threshold": 10,
            "severity": "Medium",
            "message": "Critically low fuel"
        })
        recommendations.append("Refuel immediately")
        health_score -= 10

    if health_score >= 80:
        status = "Healthy"
    elif health_score >= 60:
        status = "Warning"
    else:
        status = "Critical"

    return {
        "vehicle_id": request.vehicle_id,
        "health_score": max(health_score, 0),
        "status": status,
        "issues": issues,
        "recommendations": recommendations,
        "total_issues": len(issues)
    }


@router.get("/analyze-dtc/{dtc_id}")
def analyze_dtc(
    dtc_id: str,
    db: Session = Depends(get_db)
):
    dtc = db.query(DTC).filter(DTC.dtc_id == dtc_id).first()
    if not dtc:
        return {"error": "DTC not found"}

    # Find related faults
    related_faults = db.query(Fault).filter(
        Fault.fault_name.contains(dtc.description.split()[0])
    ).all()

    return {
        "dtc": {
            "id": dtc.dtc_id,
            "description": dtc.description,
            "severity": dtc.severity
        },
        "related_faults": [
            {
                "fault_id": f.fault_id,
                "name": f.fault_name,
                "root_cause": f.root_cause,
                "severity": f.severity
            }
            for f in related_faults
        ],
        "recommendation": f"Inspect system related to: {dtc.description}"
    }