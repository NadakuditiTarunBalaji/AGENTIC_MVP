from sqlalchemy import Column, Integer, String, ForeignKey

from backend.config.database import Base


class KGRelation(Base):
    __tablename__ = "kg_relations"

    id = Column(Integer, primary_key=True)

    source_node = Column(
        Integer,
        ForeignKey("kg_nodes.id")
    )

    target_node = Column(
        Integer,
        ForeignKey("kg_nodes.id")
    )

    relation_type = Column(String)