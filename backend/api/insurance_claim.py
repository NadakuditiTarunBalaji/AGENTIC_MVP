from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.insurance_service import fetch_insurance

router = APIRouter(
    prefix="/api/insurance",
    tags=["Insurance"]
)

@router.get("/")
def get_insurance(db: Session = Depends(get_db)):
    return fetch_insurance(db)