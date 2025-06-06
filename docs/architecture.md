# 🧱 Qastra SmartBot Architecture

## 📍 Phase 1: Flaky Test Predictor

- Uses historical test outcomes to identify flaky patterns
- `runner/flake_predictor.py`: scoring logic
- `runner/test_runner.py`: CLI for execution
- `runner/retry_engine.py`: retries failed tests with delay logic

## 🔍 Phase 2: Visual Validator

- `visual_validator/validator.py`
- Compares baseline vs. captured screenshots using perceptual hashing
- Automatically flags UI drifts

## 🧠 Phase 3: GenAI Locator Healer

- `genai_healer/locator_healer.py`
- Matches broken locator with closest working XPath using fuzzy logic
- Smart fallback mechanism for resilient tests

## 🔜 Phase 4: Dashboard + Analytics (Coming Soon)

- Planned: Streamlit dashboard for report visualization

## 🔁 Git Flow

- `main`: production
- `dev`: integration
- `feature/*`: individual features
- `docs/*`: documentation updates

## 👨‍💻 Dependencies

- Python ≥ 3.9
- Pillow, imagehash
- FuzzyWuzzy, Langchain, etc.


---

## ✅ 2. Update `docs/architecture.md` ➕ Phase 4 Summary

Append this to the bottom of `architecture.md`:

```markdown
---

## 🖥️ Phase 4: Streamlit-Based Dashboard

The Qastra SmartBot Dashboard offers a modern, developer-friendly interface to:

- 📊 View flaky test prediction metrics
- 🖼️ Visually compare baseline vs captured screenshots
- 🤖 See GenAI-powered healed locator logs with confidence scores

Built using `streamlit`, it's modular and extendable for further analytics.
# 🔎 Qastra SmartBot Automation Suite

![CI](https://github.com/deval245/qastra-smartbot/actions/workflows/python-ci.yml/badge.svg)
🛠️ CI/CD Section (Add under 📦 Features or at bottom)
markdown
Copy
Edit
## 🔁 CI/CD Integration

This project uses **GitHub Actions** for continuous integration:

- ✅ Automatically runs tests on every push & pull request
- ✅ Ensures code quality and fast feedback
- ✅ Integrates with modular CLI and dashboard components