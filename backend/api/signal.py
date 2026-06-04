from fastapi import APIRouter

router = APIRouter(
    prefix="/api/signals",
    tags=["Signals"]
)

@router.get("/")
def get_signals():
    return {
        "status": "success",
        "message": "Signals API Working"
    }