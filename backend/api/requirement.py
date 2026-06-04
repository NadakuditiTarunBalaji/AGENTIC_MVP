from fastapi import APIRouter

router = APIRouter(
    prefix="/api/requirements",
    tags=["Requirements"]
)

@router.get("/")
def get_requirements():
    return {
        "status": "success",
        "message": "Requirements API Working"
    }