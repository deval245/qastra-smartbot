# run_dom_agent.py

from genai_healer.dom_agent.watcher import DOMChangeWatcher

if __name__ == "__main__":
    try:
        agent = DOMChangeWatcher(
            url="https://rahulshettyacademy.com/loginpagePractise/",
            interval=86400,  # default to 24 hrs
            snapshot_dir="snapshots/latest",
            retention_limit=5
        )
        agent.watch()
    except KeyboardInterrupt:
        print("[🛑] Agent stopped manually.")
        agent.stop()
