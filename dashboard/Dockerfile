FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./dashboard /app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
