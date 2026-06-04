from fastapi import APIRouter

router = APIRouter(
    prefix="/api/vehicle-data",
    tags=["Vehicle Data"]
)

@router.get("/")
def get_vehicle_data():
    return {
        "status": "success",
        "message": "Vehicle Data API Working"
    }