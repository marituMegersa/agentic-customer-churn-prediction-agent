from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.customer_churn_prediction_agent.models import AgenticCustomerChurnPredictionAgentSession, AgenticCustomerChurnPredictionAgentItem
from app.domain.customer_churn_prediction_agent.schemas import AgenticCustomerChurnPredictionAgentSessionCreate, AgenticCustomerChurnPredictionAgentItemCreate

class AgenticCustomerChurnPredictionAgentService:
    @staticmethod
    def create_session(db: Session, data: AgenticCustomerChurnPredictionAgentSessionCreate) -> AgenticCustomerChurnPredictionAgentSession:
        db_obj = AgenticCustomerChurnPredictionAgentSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticCustomerChurnPredictionAgentSession:
        return db.query(AgenticCustomerChurnPredictionAgentSession).filter(AgenticCustomerChurnPredictionAgentSession.id == session_id).first()
