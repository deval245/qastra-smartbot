import logging
import re

from compliance.pii_scrubber import redact_sensitive_data

class SecureLogger:
    def __init__(self, log_file="logs/secure.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        self.logger = logging.getLogger()

    def info(self, message):
        safe_msg = redact_sensitive_data(message)
        self.logger.info(safe_msg)

    def error(self, message):
        safe_msg = redact_sensitive_data(message)
        self.logger.error(safe_msg)
