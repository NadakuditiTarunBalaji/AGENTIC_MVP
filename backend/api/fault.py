from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.fault_service import fetch_faults

router = APIRouter(
    prefix="/api/faults",
    tags=["Faults"]
)

@router.get("/")
def get_faults(db: Session = Depends(get_db)):
    return fetch_faults(db)