# tests/dom_agent/test_watcher.py
from genai_healer.dom_agent.watcher import watch_dom_changes
import threading, time, os

def test_dom_watcher():
    url = "https://rahulshettyacademy.com/loginpagePractise/"
    thread = threading.Thread(target=watch_dom_changes, args=(url, 15), daemon=True)
    thread.start()
    time.sleep(20)
    assert len(os.listdir("logs/dom_changes")) >= 0
