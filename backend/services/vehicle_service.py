from backend.repositories.vehicle_repository import get_all_vehicle_data

def fetch_vehicle_data(db):
    return get_all_vehicle_data(db)