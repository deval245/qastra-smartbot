# runner/flake_predictor.py

def predict_flakiness(module_name):
    # Dummy flake score mapping (replace with ML later)
    fake_scores = {
        "test_login": 80,
        "test_checkout": 60,
        "test_dashboard": 40
    }
    return fake_scores.get(module_name.lower(), 50)  # Default to 50%
