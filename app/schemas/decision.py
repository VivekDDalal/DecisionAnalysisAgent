from pydantic import BaseModel

class DecisionCreate(BaseModel):
    goal: str
    proposal: str

class DecisionResponse(BaseModel):
    id: int
    goal: str
    proposal: str
    pros: str | None = None
    cons: str | None = None
    risks: str | None = None
    final_decision: str | None = None
