# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from backend.config.database import get_db
# from backend.services.insurance_service import fetch_insurance

# router = APIRouter(
#     prefix="/api/insurance",
#     tags=["Insurance"]
# )

# @router.get("/")
# def get_insurance(db: Session = Depends(get_db)):
#     return fetch_insurance(db)
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
@router.post("/")
def add_insurance_claim(
    claim_id: str,
    status: str,
    description: str,
    db: Session = Depends(get_db)
):
    return create_insurance_claim(
        db,
        claim_id,
        status,
        description
    )