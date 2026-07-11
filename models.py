from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcpName = Column(String)
    date = Column(String)
    product = Column(String)
    sentiment = Column(String)

    brochure = Column(Boolean)
    followup = Column(Boolean)

    summary = Column(String)