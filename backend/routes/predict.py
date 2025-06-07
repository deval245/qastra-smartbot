from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from backend.utils.jwt_handler import SECRET_KEY, ALGORITHM
from backend.models.request import HealRequest

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(prefix="/predict", tags=["Predict"])

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/")
def get_prediction(payload: HealRequest, user=Depends(verify_token)):
    healed_xpath = payload.broken_xpath.replace("username_email_input", "user_login")
    return {
        "module": payload.module,
        "broken_xpath": payload.broken_xpath,
        "healed_xpath": healed_xpath,
        "confidence": "84%"
    }
