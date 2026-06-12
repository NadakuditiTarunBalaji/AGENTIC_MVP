from sqlalchemy import Column, String, Float, Integer, DateTime
from backend.config.database import Base
from datetime import datetime


class VehicleTelemetry(Base):
    __tablename__ = "vehicle_telemetry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(String)
    rpm = Column(Float)
    speed = Column(Float)
    coolant_temp = Column(Float)
    battery_voltage = Column(Float)
    fuel_level = Column(Float)
    tyre_pressure_fl = Column(Float)
    tyre_pressure_fr = Column(Float)
    tyre_pressure_rl = Column(Float)
    tyre_pressure_rr = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)