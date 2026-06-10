from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.schemas.can import CANFrameCreate
from backend.services.can_service import CANService
from backend.services.ai_fusion_service import analyze_vehicle_ai
from backend.config.websocket_manager import manager

# ✅ MUST BE FIRST
router = APIRouter(prefix="/api/can", tags=["CAN"])


# -----------------------------
# POST CAN FRAME
# -----------------------------
@router.post("/frame")
async def add_frame(data: CANFrameCreate, db: Session = Depends(get_db)):

    # 1. STORE IN DB
    frame = CANService.store(db, data)

    # 2. AI ANALYSIS
    ai_result = analyze_vehicle_ai(data.decoded_data)

    # 3. REAL-TIME PAYLOAD (FRONTEND FRIENDLY)
    payload = {
        "vehicle_id": data.vehicle_id,
        "can": data.decoded_data,
        "ai": ai_result
    }

    # 4. SEND TO WEBSOCKET
    await manager.send_json(payload)

    return {
        "status": "success",
        "stored": True,
        "ai": ai_result
    }


# -----------------------------
# GET LATEST FRAME
# -----------------------------
@router.get("/latest/{vehicle_id}")
def get_latest(vehicle_id: int, db: Session = Depends(get_db)):

    return CANService.get_latest(db, vehicle_id)


# -----------------------------
# GET HISTORY
# -----------------------------
@router.get("/history/{vehicle_id}")
def get_history(vehicle_id: int, db: Session = Depends(get_db)):

    return CANService.get_history(db, vehicle_id)