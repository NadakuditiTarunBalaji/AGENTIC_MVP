from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from backend.config.websocket_manager import manager

router = APIRouter()


@router.websocket("/ws/vehicle/{vehicle_id}")
async def vehicle_ws(websocket: WebSocket, vehicle_id: int):

    await manager.connect(websocket)

    try:
        while True:
            # keep connection alive
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)