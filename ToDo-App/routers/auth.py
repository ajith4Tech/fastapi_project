#Handle all authentication-related routes in a this module.

import random
from passlib.context import CryptContext
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from starlette import status  
from pydantic import BaseModel  
from models import Users
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
"""
APIRouter is a FastAPI class used to create route groups in a modular way,
improving code readability, organization, and scalability of the application.
"""

router = APIRouter() #router is an instance of APIRouter that will be used to define the routes for this module.

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name : str
    last_name: str
    role: str
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "role": "user",
                "password": "securepassword123"
            }
        }
    }
def get_db():
    db = SessionLocal()  # Create a new session for each request
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after the request is completed


DB_DEPENDENCY = Annotated[Session, Depends(get_db)] # Annotated type for dependency injection of the database session

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True


@router.post("/auth",status_code=status.HTTP_201_CREATED)
async def create_user(db: DB_DEPENDENCY, 
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)

@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                             db: DB_DEPENDENCY):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": "XAsnjnjnfaiwml", "token_type": "bearer"}



        