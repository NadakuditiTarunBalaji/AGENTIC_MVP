from fastapi import FastAPI

from backend.api.requirement import router as requirements_router
from backend.api.ecu import router as ecus_router
from backend.api.signal import router as signals_router
from backend.api.calibration import router as calibrations_router
from backend.api.fault import router as faults_router
from backend.api.dtc import router as dtcs_router
from backend.api.vehicle_data import router as vehicle_data_router
from backend.api.insurance_claim import router as insurance_router

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