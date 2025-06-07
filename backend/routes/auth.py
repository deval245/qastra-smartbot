from fastapi import APIRouter
from backend.utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str):
    # Dummy check
    if username == "admin" and password == "secret":
        token = create_access_token({"sub": username})
        return {"access_token": token}
    return {"error": "Invalid credentials"}
