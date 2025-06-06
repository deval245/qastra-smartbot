# visual_validator/validator.py

import os
import sys
import argparse
from PIL import Image
import imagehash
import pandas as pd
from datetime import datetime

from components.report_writer import save_report  # ✅ import reporting layer

BASELINE_DIR = "visual_validator/baseline_store"
CAPTURED_DIR = "visual_validator/captured_screens"
THRESHOLD = 5  # max hash distance allowed


def load_image(path):
    if not os.path.exists(path):
        print(f"[❌ ERROR] Image not found: {path}")
        sys.exit(1)
    return Image.open(path)


def compare_images(baseline_path, captured_path):
    baseline = load_image(baseline_path)
    captured = load_image(captured_path)

    baseline_hash = imagehash.phash(baseline)
    captured_hash = imagehash.phash(captured)

    distance = baseline_hash - captured_hash
    print(f"[🔍 Hash Distance] = {distance}")

    return distance <= THRESHOLD, distance


def main():
    parser = argparse.ArgumentParser(description="QAstra Visual Validator")
    parser.add_argument("--module", required=True, help="Module name to validate (e.g., test_login)")
    args = parser.parse_args()

    module = args.module
    baseline_img = os.path.join(BASELINE_DIR, f"{module}.png")
    captured_img = os.path.join(CAPTURED_DIR, f"{module}.png")

    print(f"[🖼] Comparing images for module: {module}")
    print(f"[📂] Baseline: {baseline_img}")
    print(f"[📸] Captured: {captured_img}")

    result, distance = compare_images(baseline_img, captured_img)

    status = "PASS" if result else "FAIL"
    print(f"[{status}] Visual match {'within' if result else 'exceeded'} threshold (distance: {distance})")

    # ✅ Build a report row and save
    report_df = pd.DataFrame([{
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "module": module,
        "baseline_path": baseline_img,
        "captured_path": captured_img,
        "hash_distance": distance,
        "status": status
    }])

    save_report(report_df, "visual")  # ✅ Save to reports/visual/


if __name__ == "__main__":
    main()
