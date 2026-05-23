from jose import jwt
from datetime import datetime,timedelta,timezone
from jose import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
import os

ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token:str):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email=payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        return email
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
    
def get_current_user(token:str=Depends(oauth2_scheme)):
    return verify_access_token(token)


