# components/logger.py

import logging
import re

# Redaction patterns (PII masking)
REDACTION_PATTERNS = {
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+": "[REDACTED_EMAIL]",
    r"xox[baprs]-[a-zA-Z0-9-]+": "[REDACTED_TOKEN]",
    r"\b(?:\d[ -]*?){13,16}\b": "[REDACTED_CREDIT_CARD]",
    r"\b\d{3}-\d{2}-\d{4}\b": "[REDACTED_SSN]",
    r"(?:API|api|Api)[ _-]?[Kk]ey[ =:]?[a-zA-Z0-9_\-]+" : "[REDACTED_API_KEY]"
}

# Setup logger
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger("gdpr-safe-logger")

def secure_log(level, message):
    redacted_message = message
    for pattern, replacement in REDACTION_PATTERNS.items():
        redacted_message = re.sub(pattern, replacement, redacted_message, flags=re.IGNORECASE)

    if redacted_message != message:
        final_message = f"🔒 [GDPR-SAFE] → {redacted_message}"
    else:
        final_message = f"🚨 [UNSAFE] → {message}"

    if hasattr(logger, level):
        getattr(logger, level)(final_message)
    else:
        logger.info(final_message)
