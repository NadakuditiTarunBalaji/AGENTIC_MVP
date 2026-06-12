from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VehicleDataBase(BaseModel):
    rpm: float
    battery_temp: float
    coolant_temp: float
    speed: float


class VehicleDataCreate(VehicleDataBase):
    pass


class VehicleDataResponse(VehicleDataBase):
    id: int
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True


class VehicleBase(BaseModel):
    vin: str
    model: str
    manufacturer: str
    year: int
    owner_name: Optional[str] = None
    owner_phone: Optional[str] = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseModel):
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    year: Optional[int] = None
    owner_name: Optional[str] = None
    owner_phone: Optional[str] = None


class VehicleResponse(VehicleBase):
    id: int

    class Config:
        from_attributes = True


class VehicleTelemetryBase(BaseModel):
    vehicle_id: str
    rpm: Optional[float] = 0
    speed: Optional[float] = 0
    coolant_temp: Optional[float] = 0
    battery_voltage: Optional[float] = 12.6
    fuel_level: Optional[float] = 100
    tyre_pressure_fl: Optional[float] = 32
    tyre_pressure_fr: Optional[float] = 32
    tyre_pressure_rl: Optional[float] = 32
    tyre_pressure_rr: Optional[float] = 32


class VehicleTelemetryCreate(VehicleTelemetryBase):
    pass


class VehicleTelemetryResponse(VehicleTelemetryBase):
    id: int
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True