from pydantic import BaseModel
from typing import Optional

class PolicyCreate(BaseModel):
    worker_id: str
    zone: str
    platform: str
    weekly_earnings: float
    weekly_premium: int

class PolicyResponse(BaseModel):
    id: str
    worker_id: str
    zone: str
    platform: str
    weekly_earnings: float
    weekly_premium: int
    max_payout: float
    status: str
    created_at: Optional[str] = None
    renewal_date: Optional[str] = None