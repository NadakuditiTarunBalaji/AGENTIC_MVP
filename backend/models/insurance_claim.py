from sqlalchemy import Column, String
from backend.config.database import Base

class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"

    claim_id = Column(String, primary_key=True)
    status = Column(String)
    description = Column(String)