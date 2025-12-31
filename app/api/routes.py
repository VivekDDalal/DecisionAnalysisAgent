from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.decision import DecisionCreate, DecisionResponse
from app.models.decision import Decision
from app.core.database import SessionLocal
from app.ai.decision_agents import build_decision_graph

# -----------------------------
# Router MUST be defined first
# -----------------------------
router = APIRouter()

decision_graph = build_decision_graph()

# -----------------------------
# Database Dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Create Decision
# -----------------------------
@router.post("/decisions", response_model=DecisionResponse)
def create_decision(decision: DecisionCreate, db: Session = Depends(get_db)):
    new_decision = Decision(
        goal=decision.goal,
        proposal=decision.proposal
    )
    db.add(new_decision)
    db.commit()
    db.refresh(new_decision)
    return new_decision

# -----------------------------
# Get All Decisions
# -----------------------------
@router.get("/decisions", response_model=list[DecisionResponse])
def get_decisions(db: Session = Depends(get_db)):
    return db.query(Decision).all()

# -----------------------------
# Analyze Decision (AI)
# -----------------------------
@router.post("/decisions/analyze/{decision_id}", response_model=DecisionResponse)
def analyze_decision(decision_id: int, db: Session = Depends(get_db)):
    decision = db.query(Decision).filter(Decision.id == decision_id).first()

    if not decision:
        return {"error": "Decision not found"}

    result = decision_graph.invoke({
        "goal": decision.goal,
        "proposal": decision.proposal
    })

    decision.pros = result["pros"]
    decision.cons = result["cons"]
    decision.risks = result["risks"]
    decision.final_decision = result["final_decision"]

    db.commit()
    db.refresh(decision)

    return decision
