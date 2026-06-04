# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/api/requirements",
#     tags=["Requirements"]
# )

# @router.get("/")
# def get_requirements():
#     return {
#         "status": "success",
#         "message": "Requirements API Working"
#     }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.services.requirement_service import fetch_requirements

router = APIRouter(
    prefix="/api/requirements",
    tags=["Requirements"]
)

@router.get("/")
def get_requirements(db: Session = Depends(get_db)):
    return fetch_requirements(db)