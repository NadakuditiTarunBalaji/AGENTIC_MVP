from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.requirement import router as requirements_router
from backend.api.ecu import router as ecus_router
from backend.api.signal import router as signals_router
from backend.api.calibration import router as calibrations_router
from backend.api.fault import router as faults_router
from backend.api.dtc import router as dtcs_router
from backend.api.vehicle_data import router as vehicle_data_router
from backend.api.insurance_claim import router as insurance_router
from backend.api.testcase import router as testcase_router
from backend.api.can import router as can_router
from backend.api.ws import router as ws_router
from backend.api.dashboard import router as dashboard_router
from backend.api.ai import router as ai_router

app = FastAPI(
    title="ACIP-X1 - Automotive Cognitive Intelligence Platform",
    description="World's First Automotive Cognitive Intelligence Platform",
    version="1.0.0"
)

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "ACIP-X1 API Running",
        "version": "1.0.0",
        "modes": ["Engineering Mode", "Customer Mode"],
        "docs": "/docs"
    }


# Core Data APIs
app.include_router(requirements_router)
app.include_router(ecus_router)
app.include_router(signals_router)
app.include_router(calibrations_router)
app.include_router(faults_router)
app.include_router(dtcs_router)
app.include_router(vehicle_data_router)
app.include_router(insurance_router)
app.include_router(testcase_router)

# CAN + WebSocket
app.include_router(can_router)
app.include_router(ws_router)

# Dashboard + AI
app.include_router(dashboard_router)
app.include_router(ai_router)