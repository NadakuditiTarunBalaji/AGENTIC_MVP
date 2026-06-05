from backend.repositories.insurance_repository import get_all_insurance

def fetch_insurance(db):
    return get_all_insurance(db)