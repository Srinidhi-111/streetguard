from fastapi import APIRouter, HTTPException
from app.models.claim import ClaimCreate, ClaimResponse
from app.ml.fraud_detection import detect_fraud
from datetime import datetime

router = APIRouter(prefix="/claims", tags=["claims"])

claims_db = {}

PAYOUT_RATES = {
    "heavy_rain": 0.50,
    "extreme_heat": 0.30,
    "severe_aqi": 0.40,
    "bandh": 1.00,
    "platform_downtime": 0.60
}

@router.post("/create", response_model=ClaimResponse)
def create_claim(claim: ClaimCreate):
    hour = datetime.now().hour
    existing = [c for c in claims_db.values() if c["worker_id"] == claim.worker_id]
    fraud_result = detect_fraud(
        hour_of_day=hour,
        days_since_registration=30,
        claims_this_month=len(existing),
        trigger_value=claim.trigger_value
    )

    payout_rate = PAYOUT_RATES.get(claim.trigger_type, 0.5)
    payout = round(claim.trigger_value * payout_rate * 10)

    claim_id = f"GS-CLAIM-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    status = "flagged" if fraud_result["is_anomaly"] else "processing"

    claim_data = {
        "id": claim_id,
        **claim.dict(),
        "payout_amount": payout,
        "status": status,
        "fraud_score": abs(int(fraud_result["anomaly_score"] * 100)),
        "flags": fraud_result["flags"],
        "created_at": datetime.now().isoformat()
    }
    claims_db[claim_id] = claim_data
    return ClaimResponse(**claim_data)

@router.get("/{claim_id}", response_model=ClaimResponse)
def get_claim(claim_id: str):
    if claim_id not in claims_db:
        raise HTTPException(status_code=404, detail="Claim not found")
    return ClaimResponse(**claims_db[claim_id])

@router.get("/worker/{worker_id}")
def get_worker_claims(worker_id: str):
    worker_claims = [c for c in claims_db.values() if c["worker_id"] == worker_id]
    return {"claims": worker_claims, "total": len(worker_claims)}

@router.patch("/{claim_id}/approve")
def approve_claim(claim_id: str):
    if claim_id not in claims_db:
        raise HTTPException(status_code=404, detail="Claim not found")
    claims_db[claim_id]["status"] = "approved"
    return {"message": "Claim approved", "claim_id": claim_id}