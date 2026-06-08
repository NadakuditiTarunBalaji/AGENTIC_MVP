from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.ai_service import analyze_fault

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
