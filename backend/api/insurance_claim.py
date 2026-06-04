from fastapi import APIRouter

router = APIRouter(
    prefix="/api/insurance",
    tags=["Insurance"]
)

@router.get("/")
def get_insurance():
    return {
        "status": "success",
        "message": "Insurance API Working"
    }