# runner/test_runner.py

import argparse
import os
import pandas as pd
from dotenv import load_dotenv
from runner.retry_engine import retry_test
from runner.flake_predictor import predict_flakiness
from components.report_writer import save_report
from components.logger import secure_log as log


def main():
    load_dotenv()  # ✅ Load environment variables from .env file

    parser = argparse.ArgumentParser(description="QAstra Smart Test Runner")
    parser.add_argument("--type", required=True, choices=["api", "ui", "genai"], help="Type of test to run")
    parser.add_argument("--module", required=True, help="Test module name (e.g., test_login)")
    args = parser.parse_args()

    # 🔐 GDPR-safe logging with masked API_KEY
    log('info', f"Triggering test for module: {args.module} using API_KEY: {os.getenv('API_KEY')}")

    print(f"\n[QAstra] Running {args.type.upper()} test for module: {args.module}")

    # 🔮 Predict flakiness
    flake_score = predict_flakiness(args.module)
    print(f"[Flake Predictor] Estimated flakiness score: {flake_score}%")

    # 🔁 Retry mechanism
    result = retry_test(args.module, max_retries=2, flake_score=flake_score)

    # 🟢 Final outcome
    print(f"\n[QAstra] Final Result: {'✅ PASS' if result else '❌ FAIL'}")

    # 📝 Prepare report
    results_df = pd.DataFrame([{
        "module": args.module,
        "type": args.type,
        "flake_score": flake_score,
        "final_result": "PASS" if result else "FAIL"
    }])

    # 💾 Save report as CSV
    save_report(results_df, report_type="flaky")


if __name__ == "__main__":
    main()
