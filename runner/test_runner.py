# runner/test_runner.py

import argparse
import pandas as pd
from runner.retry_engine import retry_test
from runner.flake_predictor import predict_flakiness
from components.report_writer import save_report

def main():
    parser = argparse.ArgumentParser(description="QAstra Smart Test Runner")
    parser.add_argument("--type", required=True, choices=["api", "ui", "genai"], help="Type of test to run")
    parser.add_argument("--module", required=True, help="Test module name (e.g., test_login)")
    args = parser.parse_args()

    print(f"\n[QAstra] Running {args.type.upper()} test for module: {args.module}")

    flake_score = predict_flakiness(args.module)
    print(f"[Flake Predictor] Estimated flakiness score: {flake_score}%")

    result = retry_test(args.module, max_retries=2, flake_score=flake_score)

    print(f"\n[QAstra] Final Result: {'✅ PASS' if result else '❌ FAIL'}")

    # ✅ Create report entry
    results_df = pd.DataFrame([{
        "module": args.module,
        "type": args.type,
        "flake_score": flake_score,
        "final_result": "PASS" if result else "FAIL"
    }])

    # ✅ Save report under reports/flaky
    save_report(results_df, report_type="flaky")


if __name__ == "__main__":
    main()
