from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from models.user_model import User
from schemas.user_schema import UserCreate
from security import hash_password,verify_password
from auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(tags=["Auth"])

#Register
@router.post("/register")
def register(user:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    hashed_password=hash_password(user.password)
    new_user=User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created"}

#Login
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()
    if not existing_user:

        raise HTTPException(
            status_code=400,
            detail="Invalid email"
        )
    valid_password = verify_password(
        form_data.password,
        existing_user.password
    )
    if not valid_password:

        raise HTTPException(
            status_code=400,
            detail="Invalid password"
        )
    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }