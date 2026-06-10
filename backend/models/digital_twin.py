from sqlalchemy import Column, Integer, JSON, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class DigitalTwin(Base):
    __tablename__ = "digital_twins"

    id = Column(Integer, primary_key=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    twin_state = Column(JSON)

    last_sync = Column(
        DateTime,
        default=datetime.utcnow
    )