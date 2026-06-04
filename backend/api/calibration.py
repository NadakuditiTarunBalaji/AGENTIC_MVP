from fastapi import APIRouter

router = APIRouter(
    prefix="/api/calibrations",
    tags=["Calibrations"]
)

@router.get("/")
def get_calibrations():
    return {
        "status": "success",
        "message": "Calibrations API Working"
    }