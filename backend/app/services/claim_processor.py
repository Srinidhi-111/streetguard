from datetime import datetime
from app.ml.fraud_detection import detect_fraud

PAYOUT_RATES = {
    "heavy_rain": 0.50,
    "extreme_heat": 0.30,
    "severe_aqi": 0.40,
    "bandh": 1.00,
    "platform_downtime": 0.60
}

def process_claim(worker_id: str, trigger_type: str, trigger_value: float,
                  weekly_earnings: float, claims_this_month: int = 1) -> dict:
    hour = datetime.now().hour
    fraud_result = detect_fraud(
        hour_of_day=hour,
        days_since_registration=30,
        claims_this_month=claims_this_month,
        trigger_value=trigger_value
    )

    payout_rate = PAYOUT_RATES.get(trigger_type, 0.5)
    daily_earning = weekly_earnings / 6
    payout_amount = round(daily_earning * payout_rate)

    claim_id = f"GS-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    status = "flagged" if fraud_result["is_anomaly"] else "approved"

    return {
        "claim_id": claim_id,
        "worker_id": worker_id,
        "trigger_type": trigger_type,
        "trigger_value": trigger_value,
        "payout_amount": payout_amount,
        "status": status,
        "fraud_check": fraud_result,
        "created_at": datetime.now().isoformat()
    }