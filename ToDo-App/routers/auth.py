#Handle all authentication-related routes in a this module.

from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, Request
from starlette import status  
from pydantic import BaseModel  
from models import Users
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError #json web-token for authorization and authentication jose provides jwt, jws, jse 
from fastapi.templating import Jinja2Templates
"""
APIRouter is a FastAPI class used to create route groups in a modular way,
improving code readability, organization, and scalability of the application.
"""

router = APIRouter(
    prefix="/auth", #prefix is a string that will be prepended to all the routes in this router
    tags=["auth"], #tags is a list of strings that will be used to group routes in the OpenAPI documentation
    )

# JWT configuration, Secret Key and Algorithm for generating signatures
SECRET_KEY = 'e4dd5148d49c824fc212f5f1a2e830c9ba942becd926d9ed53ff31ecb4202e06'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bear = OAuth2PasswordBearer(tokenUrl='auth/token')



class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name : str
    last_name: str
    role: str
    password: str
    phone_number: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "role": "user",
                "password": "securepassword123",
                "phone_number": "9876543210"
            }
        }
    }

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()  # Create a new session for each request
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after the request is completed


DB_DEPENDENCY = Annotated[Session, Depends(get_db)] # Annotated type for dependency injection of the database session

templates = Jinja2Templates(directory="templates")

@router.get("/login-page")
def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register-page")
def render_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

###ENDPOINTS####
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, role: str ,expires_delta: timedelta):
    encode = {
        "sub": username,
        "id": user_id,
        "role": role
        }
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bear)], db: DB_DEPENDENCY):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role : str = payload.get("role")
        if username is None or user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(Users).filter(Users.username == username).first()
    if user is None:
        raise credentials_exception
    return {"username": user.username, "user_id": user.user_id, "user_role": user.role}


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db: DB_DEPENDENCY, 
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
        phone_number=create_user_request.phone_number
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)

@router.post("/token", response_model=Token, status_code=status.HTTP_201_CREATED)
async def login_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                             db: DB_DEPENDENCY):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(form_data.username, user.user_id, user.role,timedelta(minutes=15))
    return {"access_token": token, "token_type": "bearer"}


        