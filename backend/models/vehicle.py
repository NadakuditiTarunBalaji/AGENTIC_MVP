from sqlalchemy import Column, Integer, String
from backend.config.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)

    vin = Column(String, unique=True)
    vehicle_number = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    year = Column(Integer)

    customer_name = Column(String)