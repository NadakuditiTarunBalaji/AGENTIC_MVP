from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class AgentResult(Base):
    __tablename__ = "agent_results"

    id = Column(Integer, primary_key=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    agent_name = Column(String)

    prediction = Column(String)

    confidence = Column(Float)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )