from sqlalchemy.orm import Session

from backend.repositories.insurance_repository import (
    get_all_insurance_claims
)

def fetch_insurance(db: Session):
    return get_all_insurance_claims(db)