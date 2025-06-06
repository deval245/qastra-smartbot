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

