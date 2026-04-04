from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/stats")
def get_stats():
    return {
        "total_workers": 247,
        "active_policies": 231,
        "claims_today": 12,
        "total_paid_out": 8600,
        "active_triggers": 1,
        "timestamp": datetime.now().isoformat()
    }

@router.get("/claims/recent")
def get_recent_claims():
    return {
        "claims": [
            {"worker": "Murugan R", "zone": "Tambaram", "trigger": "Heavy Rain", "amount": 720, "status": "paid"},
            {"worker": "Ravi K", "zone": "Tambaram", "trigger": "Heavy Rain", "amount": 650, "status": "processing"},
            {"worker": "Selvam P", "zone": "Chromepet", "trigger": "Heavy Rain", "amount": 580, "status": "flagged"},
        ]
    }

@router.get("/triggers/active")
def get_active_triggers():
    return {
        "active_triggers": [
            {
                "type": "heavy_rain",
                "zone": "Tambaram",
                "value": "35mm/hr",
                "workers_affected": 47,
                "fired_at": datetime.now().isoformat()
            }
        ]
    }