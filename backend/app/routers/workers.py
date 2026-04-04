from fastapi import APIRouter, HTTPException
from app.models.worker import WorkerCreate, WorkerResponse
from datetime import datetime

router = APIRouter(prefix="/workers", tags=["workers"])

workers_db = {}

@router.post("/register", response_model=WorkerResponse)
def register_worker(worker: WorkerCreate):
    zone_risk = {
        "tambaram": 75, "chromepet": 75, "adyar": 75,
        "velachery": 50, "t. nagar": 50, "omr": 50,
        "anna nagar": 25, "porur": 25
    }
    risk_score = zone_risk.get(worker.zone.lower(), 25)

    base = 49
    zone_adj = 25 if risk_score == 75 else 15 if risk_score == 50 else 0
    season_adj = 10
    premium = base + zone_adj + season_adj

    worker_id = f"W-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    worker_data = {
        "id": worker_id,
        **worker.dict(),
        "risk_score": risk_score,
        "weekly_premium": premium,
        "created_at": datetime.now().isoformat()
    }
    workers_db[worker_id] = worker_data
    return WorkerResponse(**worker_data)

@router.get("/{worker_id}", response_model=WorkerResponse)
def get_worker(worker_id: str):
    if worker_id not in workers_db:
        raise HTTPException(status_code=404, detail="Worker not found")
    return WorkerResponse(**workers_db[worker_id])

@router.get("/")
def list_workers():
    return {"workers": list(workers_db.values()), "total": len(workers_db)}