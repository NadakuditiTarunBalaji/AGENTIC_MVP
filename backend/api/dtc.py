from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.dtc_service import fetch_dtcs

router = APIRouter(
    prefix="/api/dtcs",
    tags=["DTCs"]
)

@router.get("/")
def get_dtcs(db: Session = Depends(get_db)):
    return fetch_dtcs(db)