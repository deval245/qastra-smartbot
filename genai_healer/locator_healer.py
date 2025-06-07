# genai_healer/locator_healer.py

import json
import os
from thefuzz import fuzz

FALLBACK_DATA_PATH = "genai_healer/sample_locators.json"
CONFIDENCE_THRESHOLD = 70  # Tuneable threshold


def load_fallback_locators():
    if not os.path.exists(FALLBACK_DATA_PATH):
        print(f"[⚠️] Fallback data file not found: {FALLBACK_DATA_PATH}")
        return {}
    with open(FALLBACK_DATA_PATH, "r") as file:
        return json.load(file)


def heal_locator(failed_locator: str, module: str = "default", html_snippet: str = None):
    print(f"[🛠️] Attempting to heal locator: {failed_locator}")
    if html_snippet:
        print(f"[📄] HTML context provided: {html_snippet[:100]}...")

    fallback_data = load_fallback_locators()
    candidates = fallback_data.get(module, [])

    best_match = None
    highest_score = 0

    for alt in candidates:
        score = fuzz.partial_ratio(failed_locator, alt)
        print(f"🔍 Comparing to: {alt} | Score: {score}")
        if score > highest_score:
            highest_score = score
            best_match = alt

    if best_match and highest_score >= CONFIDENCE_THRESHOLD:
        print(f"[✅] Healed! Using: {best_match} (Score: {highest_score})")
        return best_match
    else:
        print(f"[❌] No suitable fallback found.")
        return None
