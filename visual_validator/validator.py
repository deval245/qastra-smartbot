# visual_validator/validator.py

import os
import sys
import argparse
from PIL import Image, ImageChops
import imagehash

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

    baseline_img = os.path.join(BASELINE_DIR, f"{args.module}.png")
    captured_img = os.path.join(CAPTURED_DIR, f"{args.module}.png")

    print(f"[🖼] Comparing images for module: {args.module}")
    print(f"[📂] Baseline: {baseline_img}")
    print(f"[📸] Captured: {captured_img}")

    result, distance = compare_images(baseline_img, captured_img)

    if result:
        print(f"[✅ PASS] Visual match within threshold (distance: {distance})")
    else:
        print(f"[❌ FAIL] Visual mismatch detected! (distance: {distance})")


if __name__ == "__main__":
    main()
