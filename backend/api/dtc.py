from fastapi import APIRouter

router = APIRouter(
    prefix="/api/dtcs",
    tags=["DTCs"]
)

@router.get("/")
def get_dtcs():
    return {
        "status": "success",
        "message": "DTCs API Working"
    }