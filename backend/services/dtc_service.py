# from backend.repositories.dtc_repository import get_all_dtcs
from backend.repositories.dtc_repository import (
    get_all_dtcs,
    create_dtc
)

def fetch_dtcs(db):
    return get_all_dtcs(db)
def add_dtc(db, dtc_code, description,severity):
    return create_dtc(
        db,
        dtc_code,
        description,
        severity
    )