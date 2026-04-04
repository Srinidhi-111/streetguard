from fastapi import APIRouter
from datetime import datetime
import requests, os

router = APIRouter(prefix="/trigger-events", tags=["triggers"])

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY", "demo")
WAQI_KEY = os.getenv("WAQI_KEY", "demo")

THRESHOLDS = {
    "rainfall": {"value": 20, "payout_percent": 50, "type": "heavy_rain"},
    "temperature": {"value": 43, "payout_percent": 30, "type": "extreme_heat"},
    "aqi": {"value": 300, "payout_percent": 40, "type": "severe_aqi"},
}

@router.get("/evaluate/{city}")
def evaluate_triggers(city: str = "Chennai"):
    triggers_fired = []
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric",
            timeout=5
        )
        data = r.json()
        rainfall = data.get("rain", {}).get("1h", 0)
        temp = data["main"]["temp"]

        if rainfall > THRESHOLDS["rainfall"]["value"]:
            triggers_fired.append({
                "type": "heavy_rain",
                "value": rainfall,
                "threshold": THRESHOLDS["rainfall"]["value"],
                "payout_percent": THRESHOLDS["rainfall"]["payout_percent"]
            })
        if temp > THRESHOLDS["temperature"]["value"]:
            triggers_fired.append({
                "type": "extreme_heat",
                "value": temp,
                "threshold": THRESHOLDS["temperature"]["value"],
                "payout_percent": THRESHOLDS["temperature"]["payout_percent"]
            })
    except:
        pass

    return {
        "city": city,
        "triggers_fired": triggers_fired,
        "triggered": len(triggers_fired) > 0,
        "timestamp": datetime.now().isoformat()
    }

@router.post("/manual")
def fire_manual_trigger(zone: str, trigger_type: str = "bandh"):
    return {
        "zone": zone,
        "trigger_type": trigger_type,
        "payout_percent": 100,
        "status": "fired",
        "message": f"Manual {trigger_type} trigger fired for {zone}",
        "timestamp": datetime.now().isoformat()
    }