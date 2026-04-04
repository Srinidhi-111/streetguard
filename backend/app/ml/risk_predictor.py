import numpy as np
from sklearn.ensemble import RandomForestClassifier

X_train = np.array([
    [75, 10, 1, 35],
    [75, 10, 2, 30],
    [50, 5, 1, 25],
    [50, 0, 1, 20],
    [25, 10, 1, 22],
    [25, 0, 1, 18],
    [75, 5, 2, 32],
    [50, 10, 2, 28],
])
# Risk levels: 0=low, 1=medium, 2=high
y_train = np.array([2, 2, 1, 1, 0, 0, 2, 1])

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

RISK_LABELS = {0: "Low", 1: "Medium", 2: "High"}
RISK_SCORES = {0: 25, 1: 50, 2: 75}

def predict_risk(zone_score: int, month: int,
                 platform_code: int, avg_rainfall: float) -> dict:
    X = np.array([[zone_score, month, platform_code, avg_rainfall]])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    return {
        "risk_level": RISK_LABELS[prediction],
        "risk_score": RISK_SCORES[prediction],
        "confidence": round(float(max(probabilities)) * 100, 1),
        "recommendation": f"Weekly premium starting at ₹{49 + (25 if prediction == 2 else 15 if prediction == 1 else 0)}"
    }