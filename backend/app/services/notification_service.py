from datetime import datetime

def send_trigger_notification(worker_name: str, trigger_type: str,
                               payout_amount: float, zone: str) -> dict:
    messages = {
        "heavy_rain": f"🌧️ Heavy rain in {zone}. Claim initiated. ₹{payout_amount} will reach your UPI in 2 hours.",
        "extreme_heat": f"🌡️ Extreme heat in {zone}. Claim initiated. ₹{payout_amount} will reach your UPI in 2 hours.",
        "severe_aqi": f"💨 Poor air quality in {zone}. Claim initiated. ₹{payout_amount} will reach your UPI in 2 hours.",
        "bandh": f"🚫 Bandh detected in {zone}. Full day claim initiated. ₹{payout_amount} will reach your UPI in 2 hours.",
    }
    message = messages.get(trigger_type, f"Disruption detected. ₹{payout_amount} claim initiated.")
    print(f"[NOTIFICATION] → {worker_name}: {message}")
    return {
        "worker": worker_name,
        "message": message,
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    }

def send_payout_confirmation(worker_name: str, amount: float, reference_id: str) -> dict:
    message = f"✅ ₹{amount} credited to your UPI. Ref: {reference_id}"
    print(f"[NOTIFICATION] → {worker_name}: {message}")
    return {
        "worker": worker_name,
        "message": message,
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    }