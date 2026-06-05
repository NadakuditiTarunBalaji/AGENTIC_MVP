from backend.repositories.dtc_repository import get_all_dtcs


def fetch_dtcs(db):
    return get_all_dtcs(db)