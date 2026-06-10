from sqlalchemy import Column, Integer, String

from backend.config.database import Base


class KGNode(Base):
    __tablename__ = "kg_nodes"

    id = Column(Integer, primary_key=True)

    node_type = Column(String)

    node_name = Column(String)