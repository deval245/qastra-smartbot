from fastapi import FastAPI
from backend.routes import auth, predict

app = FastAPI(title="QAstra SmartBot API", version="1.0.0")

app.include_router(auth.router)
app.include_router(predict.router)
