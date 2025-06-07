# genai_healer/dom_agent/watcher.py

import time
import hashlib
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .utils import save_snapshot, cleanup_old_snapshots

class DOMChangeWatcher:
    def __init__(self, url, interval=86400, snapshot_dir="snapshots/latest", retention_limit=5):
        self.url = url
        self.interval = interval
        self.snapshot_dir = snapshot_dir
        self.retention_limit = retention_limit
        self.last_dom_hash = None
        self.driver = self._start_driver()

    def _start_driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        return webdriver.Chrome(options=options)

    def _get_dom_hash(self):
        dom = self.driver.execute_script("return document.documentElement.outerHTML")
        return hashlib.sha256(dom.encode('utf-8')).hexdigest(), dom

    def watch(self):
        print(f"[🔍] Monitoring: {self.url}")
        self.driver.get(self.url)

        while True:
            current_hash, dom = self._get_dom_hash()

            if self.last_dom_hash and self.last_dom_hash != current_hash:
                print("[⚠️] DOM changed detected!")
                save_snapshot(dom, self.snapshot_dir)
                cleanup_old_snapshots(self.snapshot_dir, self.retention_limit)
            else:
                print("[✅] DOM is stable.")

            self.last_dom_hash = current_hash
            time.sleep(self.interval)

    def stop(self):
        self.driver.quit()
