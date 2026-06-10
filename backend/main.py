from fastapi import FastAPI

from backend.api.requirement import router as requirements_router
from backend.api.ecu import router as ecus_router
from backend.api.signal import router as signals_router
from backend.api.calibration import router as calibrations_router
from backend.api.fault import router as faults_router
from backend.api.dtc import router as dtcs_router
from backend.api.vehicle_data import router as vehicle_data_router
from backend.api.insurance_claim import router as insurance_router

from backend.api.ai import router as ai_router

from backend.api.dashboard import router as dashboard_router

from backend.api.can import router as can_router

from backend.api.ws import router as ws_router

app = FastAPI(
    title="ACIP-X1 - Automotive Cognitive Intelligence Platform"
)

@app.get("/")
def home():
    return {
        "message": "ACIP-X1 API Running"
    }

app.include_router(requirements_router)
app.include_router(ecus_router)
app.include_router(signals_router)
app.include_router(calibrations_router)
app.include_router(faults_router)
app.include_router(dtcs_router)
app.include_router(vehicle_data_router)
app.include_router(insurance_router)


app.include_router(ai_router)


app.include_router(dashboard_router)



app.include_router(can_router)


app.include_router(ws_router)



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)