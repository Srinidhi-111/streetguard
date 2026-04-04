from pydantic import BaseModel
from typing import Optional, List

class ClaimCreate(BaseModel):
    worker_id: str
    policy_id: str
    trigger_type: str
    trigger_value: float
    zone: str

class ClaimResponse(BaseModel):
    id: str
    worker_id: str
    policy_id: str
    trigger_type: str
    trigger_value: float
    zone: str
    payout_amount: float
    status: str
    fraud_score: int
    flags: List[str] = []
    created_at: Optional[str] = None