# tests/dom_agent/test_snapshotter.py
from genai_healer.dom_agent.snapshotter import save_dom_snapshot
import os

def test_snapshot_creation():
    url = "https://rahulshettyacademy.com/loginpagePractise/"
    path = save_dom_snapshot(url)
    assert os.path.exists(path)
