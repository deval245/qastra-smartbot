🧱 Qastra SmartBot Architecture
📍 Phase 1: Flaky Test Predictor
✅ Uses historical outcomes and simple heuristics to estimate flakiness

runner/flake_predictor.py → Flake scoring logic

runner/test_runner.py → CLI entrypoint

runner/retry_engine.py → Controlled retry logic (max 2 attempts)

🔍 Phase 2: Visual Validator
✅ Ensures UI stability with screenshot diffing

visual_validator/validator.py

Uses ImageHash for perceptual comparison

Highlights mismatches and stores results in structured reports

🧠 Phase 3: GenAI Locator Healer
✅ Prevents flaky selector issues via LLM

genai_healer/locator_healer.py

Auto-heals broken XPath/CSS selectors with confidence scoring

Supports fallback strategy if GenAI fails

🔒 Phase 4: GDPR-Safe Logger
✅ Ensures no PII leakage in logs

components/logger.py

Uses regex-based redaction for:

Emails

SSNs

Tokens (Slack, API)

Credit cards

Each log is labeled as:

🔒 [GDPR-SAFE] (if redacted)

🚨 [UNSAFE] (if untouched)

Sample:

bash
Copy
Edit
[INFO] 🔒 [GDPR-SAFE] → User email: [REDACTED_EMAIL]
[WARNING] 🔒 [GDPR-SAFE] → Token: [REDACTED_TOKEN]
📊 Phase 5: Streamlit Dashboard (WIP)
Coming soon:

dashboard/app.py

Real-time visualization for:

Flaky predictions

Visual validator outputs

GenAI healing stats

Streamlit-powered, low-code UI

🔁 CI/CD Integration
✅ GitHub Actions powered pipeline

Automatically triggers on:

PRs

Pushes to main or dev

Runs:

CLI test runner

Flake prediction

Report generation

Future scope:

Deploy dashboard

Slack alert integration

Badge:



🧬 Git Flow
Branch	Purpose
main	Stable, production-ready
dev	Ongoing development
feature/*	Individual tasks/features
docs/*	Markdown and visuals

👨‍💻 Tech Stack & Dependencies
Category	Libraries
Core Language	Python ≥ 3.9
ML/AI	scikit-learn, fuzzywuzzy, langchain
Visual Validation	Pillow, imagehash
LLM/GenAI	ollama, openai, streamlit
Logging	logging, dotenv, regex
Reporting	pandas, csv