from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class CANFrame(Base):
    __tablename__ = "can_frames"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    can_id = Column(String)

    dlc = Column(Integer)

    payload = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )