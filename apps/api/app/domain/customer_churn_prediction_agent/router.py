from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.customer_churn_prediction_agent.schemas import AgenticCustomerChurnPredictionAgentSessionCreate, AgenticCustomerChurnPredictionAgentSessionResponse
from app.domain.customer_churn_prediction_agent.service import AgenticCustomerChurnPredictionAgentService

router = APIRouter(prefix="/api/v1/customer_churn_prediction_agent", tags=["Agentic Customer Churn Prediction Agent Domain"])

@router.post("/sessions", response_model=AgenticCustomerChurnPredictionAgentSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCustomerChurnPredictionAgentSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Customer Churn Prediction Agent.
    """
    return AgenticCustomerChurnPredictionAgentService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCustomerChurnPredictionAgentSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCustomerChurnPredictionAgentService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
