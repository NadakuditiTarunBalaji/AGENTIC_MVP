from fastapi import APIRouter

router = APIRouter(
    prefix="/api/ecus",
    tags=["ECUs"]
)

@router.get("/")
def get_ecus():
    return {
        "status": "success",
        "message": "ECUs API Working"
    }