from sqlalchemy import Column, String, Float
from backend.config.database import Base


class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"

    policy_id = Column(String, primary_key=True)
    vehicle_id = Column(String)
    provider = Column(String)
    coverage_type = Column(String)
    premium_amount = Column(Float)
    status = Column(String)