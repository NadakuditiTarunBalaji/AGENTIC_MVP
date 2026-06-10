from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class VehicleTelemetry(Base):
    __tablename__ = "vehicle_telemetry"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    rpm = Column(Float)
    speed = Column(Float)

    coolant_temp = Column(Float)
    battery_temp = Column(Float)
    battery_voltage = Column(Float)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )