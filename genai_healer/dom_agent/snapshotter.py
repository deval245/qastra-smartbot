import os
import hashlib
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SNAPSHOT_DIR = "snapshots/latest"

class DOMSnapshotter:
    def __init__(self, url):
        self.url = url
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        return webdriver.Chrome(options=options)

    def capture_snapshot(self):
        self.driver.get(self.url)
        dom = self.driver.execute_script("return document.documentElement.outerHTML")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SNAPSHOT_DIR}/snapshot_{timestamp}.html"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(dom)

        print(f"[📸] Snapshot saved: {filename}")
        return dom

    def get_hash(self, dom):
        return hashlib.sha256(dom.encode('utf-8')).hexdigest()

    def close(self):
        self.driver.quit()
