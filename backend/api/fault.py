from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.fault_service import (
    fetch_faults,
    create_fault,
    modify_fault,
    remove_fault
)

router = APIRouter(
    prefix="/api/faults",
    tags=["Faults"]
)

@router.get("/")
def get_faults(db: Session = Depends(get_db)):
    return fetch_faults(db)

@router.post("/")
def add_fault(
    fault_id: str,
    fault_name: str,
    severity: str,
    root_cause: str,
    db: Session = Depends(get_db)
):
    return create_fault(
        db,
        fault_id,
        fault_name,
        severity,
        root_cause
    )
@router.put("/")
@router.put("/{fault_id}")
def update_fault_api(
    fault_id: str,
    fault_name: str,
    root_cause: str,
    severity: str,
    db: Session = Depends(get_db)
):
    return modify_fault(
        db,
        fault_id,
        fault_name,
        root_cause,
        severity
    )

@router.delete("/{fault_id}")
def delete_fault_api(
    fault_id: str,
    db: Session = Depends(get_db)
):
    return remove_fault(
        db,
        fault_id
    )