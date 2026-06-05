from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from backend.config.database import get_db



router = APIRouter(
    prefix="/api/ecus",
    tags=["ECUs"]
)


class ECUCreate(BaseModel):
    ecu_id: str
    ecu_name: str
    function: str


@router.get("/")
def get_ecus(db: Session = Depends(get_db)):
    return fetch_ecus(db)


@router.post("/")
def add_ecu(
    ecu: ECUCreate,
    db: Session = Depends(get_db)
):
    return create_ecu(
        db,
        ecu.ecu_id,
        ecu.ecu_name,
        ecu.function
    )

    
from backend.services.ecu_service import fetch_ecus

@router.put("/{ecu_id}")
def edit_ecu(
    ecu_id: str,
    ecu: ECUCreate,
    db: Session = Depends(get_db)
):
    return update_ecu(
        db,
        ecu_id,
        ecu.ecu_name,
        ecu.function
    )

from backend.repositories.ecu_repository import (
    create_ecu,
    update_ecu,
    delete_ecu
)


@router.delete("/{ecu_id}")
def remove_ecu(
    ecu_id: str,
    db: Session = Depends(get_db)
):
    return delete_ecu(
        db,
        ecu_id
    )