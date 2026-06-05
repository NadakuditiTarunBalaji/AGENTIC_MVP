from backend.repositories.fault_repository import get_all_faults

def fetch_faults(db):
    return get_all_faults(db)