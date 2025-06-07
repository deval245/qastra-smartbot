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

# 🐳 Build Docker image
docker-build:
	docker build -t qastra-smartbot .

# 🚀 Run Docker container (FastAPI - port 8000)
docker-run:
	docker run -p 8000:8000 qastra-smartbot

# ✅ Smoke test to validate FastAPI endpoints
docker-test:
	curl --fail http://localhost:8000/ || (echo "❌ Root endpoint failed" && exit 1)
	curl --fail http://localhost:8000/docs || (echo "❌ Swagger UI failed" && exit 1)

# 📦 Push Docker image to DockerHub
docker-push:
	@test "$(DOCKER_USER)" != "" || (echo "❌ Provide DOCKER_USER: make docker-push DOCKER_USER=username" && exit 1)
	docker tag qastra-smartbot $(DOCKER_USER)/qastra:latest
	docker push $(DOCKER_USER)/qastra:latest


# ----------- Git & CI/CD Utilities -----------

# 🔀 Raise PR via GitHub CLI
.PHONY: gh-pr
gh-pr:
	@test "$(BASE)" != "" || (echo "❌ Please provide BASE branch: make gh-pr BASE=dev HEAD=feature-branch ..." && exit 1)
	@test "$(HEAD)" != "" || (echo "❌ Please provide HEAD branch: make gh-pr BASE=... HEAD=..." && exit 1)
	@test "$(TITLE)" != "" || (echo "❌ Please provide TITLE: make gh-pr TITLE='...'" && exit 1)
	@test "$(BODY)" != "" || (echo "❌ Please provide BODY: make gh-pr BODY='...'" && exit 1)
	gh pr create --base $(BASE) --head $(HEAD) --title "$(TITLE)" --body "$(BODY)"

# 👀 View GitHub Actions logs
ci-log:
	open https://github.com/deval245/qastra-smartbot/actions

# 🧪 Trigger GitHub Actions manually (example only)
ci-trigger:
	curl -X POST -H "Authorization: token $(GITHUB_TOKEN)" \
		-H "Accept: application/vnd.github.v3+json" \
		https://api.github.com/repos/deval245/qastra-smartbot/actions/workflows/test.yml/dispatches \
		-d '{"ref":"dev"}'


# ----------- Jenkins (Optional Future Scope) -----------

# 🔧 Jenkins job logs
jenkins-log:
	open http://localhost:8080/job/qastra-smartbot/

# ▶️ Trigger Jenkins job (CLI)
jenkins-run:
	curl -X POST http://localhost:8080/job/qastra-smartbot/build --user admin:<your_api_token>


# ----------- Extras & Shortcuts -----------

# 🧭 End-to-end test & report generation
all:
	make test-ui && make retry && make visual-validate && make report && make dashboard

# 🚀 End-to-end Docker setup: build, run, test
all-docker:
	make clean && make docker-build && make docker-run && sleep 5 && make docker-test

# 📖 Help menu
help:
	@grep -E '(^[a-zA-Z_-]+:)|(#)' Makefile | awk '{print $$1 "\t" $$2}'

# 🛡️ Secure logger test
secure-log-test:
	python -c "from compliance.secure_logger import SecureLogger; logger=SecureLogger(); logger.info('User email: john@example.com'); logger.error('token=abcd1234supersecret')"

# 🔐 Run secure logger with redaction
log-test:
	python3 -c "from components.logger import secure_log; secure_log('info', 'User email: john.doe@example.com, Token: xoxb-abc123456789'); print('✅ Logged with PII scrubbing')"

# 🔐 GDPR-safe logging demo
gdpr-sample-log:
	@echo "🔒 Running GDPR-safe log demonstration...\n"
	python3 gdpr_test.py

# 🔐 Load env vars if .env present
ifneq (,$(wildcard .env))
    include .env
    export
endif

# 🔐 Test loading secrets from .env
env-check:
	set -a && source .env && set +a && \
	echo "API_KEY: $$API_KEY" && \
	echo "SLACK_TOKEN: $$SLACK_TOKEN"

# 🗝️ SSH Agent utility (if needed for git clone/push)
ssh-add:
	eval "$$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519

# 🔮 Train ML flake predictor
train-ml:
	python3 ml/train_flake_predictor.py

# 🧠 Print predicted flake score (for module=...)
predict-flake:
	python3 -c "from runner.flake_predictor import predict_flakiness; print('Flake Score:', predict_flakiness('test_login'))"
dom-watch:
	python run_dom_agent.py

