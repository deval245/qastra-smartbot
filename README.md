# 🤖 Qastra SmartBot – AI-Augmented Test Automation Suite

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> Scalable | Modular | AI-Driven | CLI Friendly

Qastra SmartBot is a modern Python-based test automation framework built for scale. It augments traditional test workflows with Machine Learning & GenAI capabilities to ensure test reliability, visual accuracy, and maintainability.

---

## 🚀 Why Qastra SmartBot?

- 🔮 **Predict flaky tests** using ML techniques
- 🧠 **Heal broken locators** using GenAI suggestions
- 🎨 **Validate visual changes** via ImageHash matching
- 🛠️ **Modular CLI-based design**
- 🔗 **CI/CD ready** (GitHub Actions)

---

## 🔧 Features by Phase

| Phase | Feature                          | Status |
|-------|----------------------------------|--------|
| 1     | CLI Retry Runner                 | ✅ Done |
| 2     | Visual Validator (ImageHash)     | ✅ Done |
| 3     | GenAI-based Locator Healer       | ✅ Done |
| 4     | Reporting Dashboard (Streamlit)  | 🔜 TBD |
| 5     | GitHub Actions CI Integration    | 🔜 TBD |

---

## 📁 Project Structure

qastra-smartbot/
│
├── runner/ # CLI, Retry, Flake ML
├── visual_validator/ # Visual Testing Engine
├── genai_healer/ # AI-based Locator Healer
├── docs/ # Architecture Docs
├── requirements.txt
├── .env.example
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup

```bash
git clone https://github.com/deval245/qastra-smartbot.git
cd qastra-smartbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
⚙️ Usage
➤ Predict Flaky Tests
bash
Copy
Edit
python runner/test_runner.py --module test_login
➤ Visual Validation
bash
Copy
Edit
python visual_validator/validator.py --module test_login
➤ GenAI Locator Healing
python
Copy
Edit
from genai_healer.locator_healer import heal_locator
healed = heal_locator("//input[@id='username_email_input']", module="test_login")
📸 Sample Output (Demo)


🧠 Architecture

See: docs/architecture.md

📄 .env Example
env
Copy
Edit
ENV=dev
BASELINE_DIR=visual_validator/baseline_store
CAPTURED_DIR=visual_validator/captured_screens
🤝 Contribution Guidelines
Create a new branch feature/<your-feature>

Use proper commit prefix (feat:, fix:, docs:)

PR should go to dev branch only

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

### 🔧 Optional: Add These Files Too

```bash
mkdir -p docs/assets
# Place demo screenshots or architecture diagrams here


