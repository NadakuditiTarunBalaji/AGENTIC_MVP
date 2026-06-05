from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.dtc_service import (
    fetch_dtcs,
    add_dtc
)
router = APIRouter( 
    prefix="/api/dtcs",
    tags=["DTCs"]
)

@router.get("/")
def get_dtcs(db: Session = Depends(get_db)):
    return fetch_dtcs(db)
@router.post("/")
def add_dtc_api(
    dtc_code: str,
    description: str,
    severity: str,

    db: Session = Depends(get_db)
):
    return add_dtc(
        db,
        dtc_code,
        description,
        severity
    )