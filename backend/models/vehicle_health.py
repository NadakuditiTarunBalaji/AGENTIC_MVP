from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class VehicleHealth(Base):
    __tablename__ = "vehicle_health"

    id = Column(Integer, primary_key=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    health_score = Column(Float)

    status = Column(String)

    recommendation = Column(String)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )