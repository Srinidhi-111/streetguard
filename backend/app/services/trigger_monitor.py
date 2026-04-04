import asyncio
import requests
import os
from datetime import datetime

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY", "demo")
WAQI_KEY = os.getenv("WAQI_KEY", "demo")

THRESHOLDS = {
    "rainfall": 20,
    "temperature": 43,
    "aqi": 300,
}

async def check_weather(city: str = "Chennai") -> dict:
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric",
            timeout=5
        )
        data = r.json()
        return {
            "rainfall": data.get("rain", {}).get("1h", 0),
            "temp": data["main"]["temp"],
            "city": city
        }
    except:
        return {"rainfall": 0, "temp": 35, "city": city}

async def check_aqi(city: str = "Chennai") -> dict:
    try:
        r = requests.get(
            f"https://api.waqi.info/feed/{city}/?token={WAQI_KEY}",
            timeout=5
        )
        data = r.json()
        return {"aqi": data["data"]["aqi"], "city": city}
    except:
        return {"aqi": 150, "city": city}

async def evaluate_triggers(city: str = "Chennai") -> list:
    weather = await check_weather(city)
    aqi = await check_aqi(city)
    triggers = []

    if weather["rainfall"] > THRESHOLDS["rainfall"]:
        triggers.append({
            "type": "heavy_rain",
            "value": weather["rainfall"],
            "payout_percent": 50
        })
    if weather["temp"] > THRESHOLDS["temperature"]:
        triggers.append({
            "type": "extreme_heat",
            "value": weather["temp"],
            "payout_percent": 30
        })
    if aqi["aqi"] > THRESHOLDS["aqi"]:
        triggers.append({
            "type": "severe_aqi",
            "value": aqi["aqi"],
            "payout_percent": 40
        })
    return triggers

async def monitor_loop(interval_minutes: int = 30):
    print(f"[{datetime.now()}] Trigger monitor started — polling every {interval_minutes} mins")
    while True:
        triggers = await evaluate_triggers("Chennai")
        if triggers:
            print(f"[{datetime.now()}] TRIGGERS FIRED: {triggers}")
        else:
            print(f"[{datetime.now()}] All clear — no triggers")
        await asyncio.sleep(interval_minutes * 60)