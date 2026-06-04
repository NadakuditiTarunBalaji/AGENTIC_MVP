from fastapi import APIRouter

router = APIRouter(
    prefix="/api/faults",
    tags=["Faults"]
)

@router.get("/")
def get_faults():
    return {
        "status": "success",
        "message": "Faults API Working"
    }