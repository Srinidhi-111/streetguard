from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkerCreate(BaseModel):
    name: str
    phone: str
    platform: str
    city: str
    zone: str
    daily_hours: float
    weekly_earnings: float

class WorkerResponse(BaseModel):
    id: str
    name: str
    phone: str
    platform: str
    city: str
    zone: str
    daily_hours: float
    weekly_earnings: float
    risk_score: int
    weekly_premium: int
    created_at: Optional[str] = None