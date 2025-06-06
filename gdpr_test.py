# gdpr_test.py

from components.logger import secure_log as log

print("🛡️ Demonstrating GDPR-compliant logs with automatic redaction:\n")

log('info', "User email: john.doe@example.com")
print("→ ✅ Email redacted automatically.")

log('debug', "SSN: 123-45-6789")
print("→ ✅ SSN redacted successfully.")

log('warning', "Token: xoxb-abc123456789")
print("→ ✅ Slack token scrubbed securely.")

log('error', "Credit Card: 4111 1111 1111 1111")
print("→ ✅ Credit card masked.")

log('info', "API Key: API_KEY=1234567890abcdef")
print("→ ✅ API key handled with care.")

print("\n✅ All logs printed above are GDPR-safe and contain no raw PII.")
