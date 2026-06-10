from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from backend.config.database import Base


class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"

    id = Column(Integer, primary_key=True)

    claim_number = Column(String, unique=True)

    policy_id = Column(Integer, ForeignKey("insurance_policies.id"))

    amount = Column(Float)

    status = Column(String)

    description = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)