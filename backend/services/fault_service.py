from backend.repositories.fault_repository import (
    get_all_faults,
    create_fault
)

def fetch_faults(db):
    return get_all_faults(db)

def add_fault(
    db,
    fault_id,
    fault_name,
    severity,
    root_cause
):
    return create_fault(
        db,
        fault_id,
        fault_name,
        severity,
        root_cause
    )