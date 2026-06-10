from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from backend.config.database import Base


class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"

    id = Column(Integer, primary_key=True)

    policy_number = Column(String)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    provider = Column(String)
    premium = Column(Float)

    start_date = Column(Date)
    end_date = Column(Date)