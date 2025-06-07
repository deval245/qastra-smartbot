from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample Pydantic model for testing
class Item(BaseModel):
    name: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "🚀 Smart ML+AI QA Bot is alive!"}

@app.post("/predict")
def fake_predict(item: Item):
    # This is a placeholder for ML prediction logic
    return {"prediction": f"Predicted class for '{item.name}'"}



