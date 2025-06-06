# runner/retry_engine.py

import random

def retry_test(module, max_retries=2, flake_score=50):
    for attempt in range(max_retries + 1):
        print(f"[Retry Engine] Attempt {attempt + 1} for {module}...")

        # Logic: if flake_score is high, simulate flakiness
        passed = random.choice([True, False]) if flake_score > 50 else True

        if passed:
            print("[Retry Engine] ✅ Passed")
            return True
        else:
            print("[Retry Engine] ❌ Failed")

    return False
