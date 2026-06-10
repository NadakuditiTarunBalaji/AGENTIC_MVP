from sqlalchemy.orm import Session

from backend.models.vehicle_data import VehicleData
from backend.models.fault import Fault
from backend.models.dtc import DTC
from backend.models.insurance_claim import InsuranceClaim


def get_dashboard_summary(db: Session):

    return {
        "total_vehicles": db.query(VehicleData).count(),
        "active_faults": db.query(Fault).count(),
        "active_dtcs": db.query(DTC).count(),
        "insurance_claims": db.query(InsuranceClaim).count()
    }


def get_vehicle_health(db: Session):

    total = db.query(VehicleData).count()

    # Example logic (you can refine later with real fields)
    healthy = int(total * 0.7)
    warning = int(total * 0.2)
    critical = total - healthy - warning

    return {
        "healthy": healthy,
        "warning": warning,
        "critical": critical
    }


def get_analytics(db: Session):

    return {
        "monthly_faults": db.query(Fault).count(),
        "monthly_dtcs": db.query(DTC).count(),
        "monthly_claims": db.query(InsuranceClaim).count(),
        "maintenance_predictions": db.query(Fault).count() // 2
    }