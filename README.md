🤖 Qastra SmartBot – AI-Augmented Test Automation Suite




Scalable | Modular | AI-Driven | CLI Friendly

Qastra SmartBot is a modern Python-based test automation framework built for scale. It augments traditional test workflows with Machine Learning & GenAI to ensure test reliability, visual accuracy, and intelligent healing.

🚀 Why Qastra SmartBot?
🔮 Predict flaky tests using ML-based heuristics

🧠 Heal broken locators via GenAI suggestions

🎨 Validate visual regressions using ImageHash

🔒 GDPR-safe logging to auto-scrub PII data

🔔 Slack alerts (upcoming)

🛠️ Modular CLI-based design

🔗 CI/CD ready (GitHub Actions)

🔧 Features by Phase
Phase	Feature	Status
1	CLI Retry Runner	✅ Done
2	Visual Validator (ImageHash)	✅ Done
3	GenAI-based Locator Healer	✅ Done
4	GDPR-safe Logger	✅ Done
5	Slack Notifier	🔜 Next
6	Reporting Dashboard (Streamlit)	🔜 WIP
7	GitHub Actions CI Integration	🔜 WIP

📁 Project Structure
bash
Copy
Edit
qastra-smartbot/
├── runner/                 # CLI runner, retry engine, flake predictor
├── visual_validator/       # Image-based comparison engine
├── genai_healer/           # GenAI-based locator healer
├── components/             # Shared utilities (logger, reporter)
├── dashboard/              # Streamlit-based UI dashboard
├── reports/                # Auto-generated flaky reports
├── .env.example            # Environment variable template
├── Makefile                # Automation tasks
└── README.md
⚙️ Setup Instructions
bash
Copy
Edit
git clone https://github.com/deval245/qastra-smartbot.git
cd qastra-smartbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
🚦 Usage Guide
➤ Run CLI Test with Retry Engine
bash
Copy
Edit
python -m runner.test_runner --type ui --module test_login
➤ Visual Validation with ImageHash
bash
Copy
Edit
python visual_validator/validator.py --module test_login
➤ Heal Locators via GenAI (LLM-integrated)
python
Copy
Edit
from genai_healer.locator_healer import heal_locator
healed = heal_locator("//input[@id='username']", module="test_login")
➤ Run GDPR-Safe Log Demo
bash
Copy
Edit
make gdpr-sample-log
🛡️ Logs will automatically redact:

Emails ✅

Slack tokens ✅

Credit card numbers ✅

SSNs ✅

API keys ✅

Example:

text
Copy
Edit
[INFO] 🔒 [GDPR-SAFE] → User email: [REDACTED_EMAIL]
[WARNING] 🔒 [GDPR-SAFE] → Token: [REDACTED_TOKEN]
📊 Qastra Dashboard (Coming Soon – Phase 4)
A Streamlit-based UI to visualize:

Flaky predictions

GenAI locator suggestions

Image comparison diffs

Launch command:

bash
Copy
Edit
streamlit run dashboard/app.py
📜 .env File Example
env
Copy
Edit
ENV=dev
API_KEY=your_api_key_here
SLACK_TOKEN=xoxb-xxxxxx
BASELINE_DIR=visual_validator/baseline_store
CAPTURED_DIR=visual_validator/captured_screens
🔁 CI/CD Integration
This project supports GitHub Actions (WIP):

✅ Lint, test, and report on every PR or commit

🧪 Automatically runs flaky predictions

🔐 Secure handling of environment secrets

📊 Dashboard deploy on CI trigger (Phase 5)

🤝 Contribution Guidelines
🔀 Create a new branch: feature/<your-feature>

✅ Use proper commit prefix: feat:, fix:, docs:

🚫 PRs should only target dev branch

🧠 Documentation
docs/architecture.md – Full architecture & phase breakdown

docs/assets/ – Screenshots, diagrams, and flow visuals

📜 License
This project is licensed under the MIT License – see LICENSE file.

