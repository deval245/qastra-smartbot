# Makefile for QAstra SmartBot - FAANG-Level Automation

# ----------- Project Setup & Dev Utilities -----------

# 🔄 Create & activate virtualenv + install dependencies
setup:
	python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# 📦 Install pre-commit hooks, useful in teams
hooks:
	pre-commit install

# 🧪 Run Pytest with CLI or UI mode test trigger
test-cli:
	python -m runner.test_runner --type cli --module test_login

test-ui:
	python -m runner.test_runner --type ui --module test_login

# 🔁 Run retry engine (retries flaky tests based on flake predictor)
retry:
	python runner/retry_engine.py --module test_login

# 🖼️ Run visual diff validator (Testron style)
visual-validate:
	python visual_validator/validator.py --module test_login

# 📝 Generate flaky test report in CSV
report:
	python components/report_writer.py --type flaky --module test_login

# 📊 Generate visual dashboard (Streamlit)
dashboard:
	streamlit run dashboard/app.py

# 🧹 Clean all .pyc, __pycache__, temp files
clean:
	find . -name '*.pyc' -delete && find . -name '__pycache__' -delete


# ----------- Docker & Deployment -----------

# 🐳 Docker build (for prod/testing usage)
docker-build:
	docker build -t qastra-smartbot .

# 🚀 Run container locally for Streamlit
# Ports: 8501 (streamlit), 8080 (jenkins if applicable)
docker-run:
	docker run -p 8501:8501 qastra-smartbot

# 📦 Push docker image to registry (future scope)
docker-push:
	docker tag qastra-smartbot <your-dockerhub-username>/qastra:latest && docker push <your-dockerhub-username>/qastra:latest


# ----------- Git & CI/CD Utilities -----------

# 🔀 Raise PR via GitHub CLI
gh-pr:
	gh pr create --base dev --head ci/github-actions-phase2 --title "🚀 Phase 5: Flaky CLI + Reports" --body "Includes retry engine, validator, CSV reporting, CI support"

# 👀 See GitHub Actions run logs
ci-log:
	open https://github.com/deval245/qastra-smartbot/actions

# 🧪 Manual trigger GitHub Actions (via curl - if needed)
ci-trigger:
	curl -X POST -H "Authorization: token $(GITHUB_TOKEN)" \
		-H "Accept: application/vnd.github.v3+json" \
		https://api.github.com/repos/deval245/qastra-smartbot/actions/workflows/test.yml/dispatches \
		-d '{"ref":"dev"}'


# ----------- Jenkins (Optional Future Scope) -----------

# 🔧 Jenkins logs & job URL open
jenkins-log:
	open http://localhost:8080/job/qastra-smartbot/

# Trigger job from CLI (authenticated)
jenkins-run:
	curl -X POST http://localhost:8080/job/qastra-smartbot/build --user admin:<your_api_token>


# ----------- Extras & Shortcuts -----------

# 🧭 All-in-one test + report + dashboard run
all:
	make test-ui && make retry && make visual-validate && make report && make dashboard

# 📖 Show available tasks with descriptions	help:
	@grep -E '(^[a-zA-Z_-]+:)|(#)' Makefile | awk '{print $$1 "\t" $$2}'
