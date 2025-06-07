# genai_healer/dom_agent/utils.py

import os
from datetime import datetime

def save_snapshot(html, directory):
    os.makedirs(directory, exist_ok=True)
    filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    path = os.path.join(directory, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[📸] Snapshot saved: {path}")

def cleanup_old_snapshots(directory, limit=5):
    files = sorted(
        [f for f in os.listdir(directory) if f.endswith(".html")],
        key=lambda f: os.path.getmtime(os.path.join(directory, f))
    )
    while len(files) > limit:
        to_remove = os.path.join(directory, files.pop(0))
        os.remove(to_remove)
        print(f"[🧹] Removed old snapshot: {to_remove}")
