from backend.repositories.vehicle_repository import (
    get_all_vehicle_data,
    create_vehicle
)

def fetch_vehicle_data(db):
    return get_all_vehicle_data(db)

def add_vehicle(
    db,
    rpm,
    battery_temp,
    coolant_temp,
    speed
):
    return create_vehicle(
        db,
        rpm,
        battery_temp,
        coolant_temp,
        speed
    )