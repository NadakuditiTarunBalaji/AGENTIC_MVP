from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.ai_service import analyze_fault

from backend.services.ai_service import analyze_dtc

router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)

@router.get("/fault-analysis/{fault_id}")
def fault_analysis(
    fault_id: str,
    db: Session = Depends(get_db)
):
    return analyze_fault(
        db,
        fault_id
    )

@router.get("/dtc-analysis/{dtc_code}")
def dtc_analysis(
    dtc_code: str,
    db: Session=Depends(get_db)):
    return analyze_dtc(
        db,
        dtc_code
        )
