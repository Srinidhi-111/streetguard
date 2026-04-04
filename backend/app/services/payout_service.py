from datetime import datetime
import os

RAZORPAY_KEY = os.getenv("RAZORPAY_KEY_ID", "demo")

def initiate_payout(worker_id: str, amount: float, upi_id: str = "test@upi") -> dict:
    reference_id = f"GS-PAY-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    # Razorpay test mode simulation
    return {
        "worker_id": worker_id,
        "amount": amount,
        "upi_id": upi_id,
        "reference_id": reference_id,
        "status": "processing",
        "estimated_time": "2 hours",
        "mode": "UPI",
        "timestamp": datetime.now().isoformat()
    }

def get_payout_status(reference_id: str) -> dict:
    return {
        "reference_id": reference_id,
        "status": "completed",
        "timestamp": datetime.now().isoformat()
    }