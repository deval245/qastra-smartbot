# train_flake_predictor.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Step 1: Simulate or load training data
data = {
    "previous_failures": [0, 1, 2, 3, 0, 2, 3, 1, 0, 1],
    "retry_count": [0, 1, 2, 2, 0, 1, 2, 1, 0, 1],
    "error_type": [1, 2, 3, 3, 0, 2, 3, 2, 0, 1],  # 0=none, 1=timeout, etc.
    "test_duration": [5, 15, 25, 30, 4, 20, 22, 10, 3, 12],
    "is_flaky": [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Step 2: Prepare training
X = df.drop("is_flaky", axis=1)
y = df["is_flaky"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Save model to ml/flake_model.pkl
model_path = os.path.join(os.path.dirname(__file__), "flake_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Model trained and saved to: {model_path}")
