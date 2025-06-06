import re

# Regex patterns to detect emails, keys, tokens
PII_PATTERNS = [
    r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',  # Email
    r'(token|key|password|secret)[=:]\s*[a-zA-Z0-9_\-]{10,}',  # Key-value secrets
]

def redact_sensitive_data(text):
    for pattern in PII_PATTERNS:
        text = re.sub(pattern, '***REDACTED***', text, flags=re.IGNORECASE)
    return text
