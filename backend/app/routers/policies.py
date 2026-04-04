from fastapi import APIRouter, HTTPException
from app.models.policy import PolicyCreate, PolicyResponse
from datetime import datetime, timedelta

router = APIRouter(prefix="/policies", tags=["policies"])

policies_db = {}

@router.post("/create", response_model=PolicyResponse)
def create_policy(policy: PolicyCreate):
    policy_id = f"GS-{datetime.now().strftime('%Y-%m%d%H%M%S')}"
    renewal = (datetime.now() + timedelta(days=7)).strftime("%b %d, %Y")
    policy_data = {
        "id": policy_id,
        **policy.dict(),
        "max_payout": round(policy.weekly_earnings * 0.7),
        "status": "active",
        "created_at": datetime.now().isoformat(),
        "renewal_date": renewal
    }
    policies_db[policy_id] = policy_data
    return PolicyResponse(**policy_data)

@router.get("/{policy_id}", response_model=PolicyResponse)
def get_policy(policy_id: str):
    if policy_id not in policies_db:
        raise HTTPException(status_code=404, detail="Policy not found")
    return PolicyResponse(**policies_db[policy_id])

@router.get("/worker/{worker_id}")
def get_worker_policies(worker_id: str):
    worker_policies = [p for p in policies_db.values() if p["worker_id"] == worker_id]
    return {"policies": worker_policies, "total": len(worker_policies)}