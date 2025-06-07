# runner/flake_predictor.py

import joblib
import os

# Load the trained ML model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../ml/flake_model.pkl")
model = joblib.load(MODEL_PATH)

def predict_flakiness(module_name):
    # Placeholder logic to map metadata; can be replaced with DB/log lookup
    features_map = {
        "test_login":     [1, 1, 1, 12],  # [failures, retries, error_type, duration]
        "test_checkout":  [2, 2, 2, 22],
        "test_dashboard": [0, 0, 0, 5]
    }
    features = features_map.get(module_name.lower(), [1, 1, 1, 10])  # default fallback
    flake_prob = model.predict_proba([features])[0][1]  # Probability of flakiness
    return round(flake_prob * 100, 2)
