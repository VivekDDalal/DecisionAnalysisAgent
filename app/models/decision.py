from sqlalchemy import Column, Integer, Text
from app.core.database import Base

class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    goal = Column(Text, nullable=False)
    proposal = Column(Text, nullable=False)

    pros = Column(Text)
    cons = Column(Text)
    risks = Column(Text)
    final_decision = Column(Text)
