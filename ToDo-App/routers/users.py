from typing import Annotated, Optional
from fastapi import  APIRouter, Depends, HTTPException, Path
from models import ToDoItem, Users # Import the Todos model
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field  # Import BaseModel for request validation
from .auth import get_current_user, bcrypt_context

router = APIRouter(
    prefix="/user",
    tags=["user_details"],
) 

class PasswordUpdate(BaseModel):
    old_password: str 
    new_password: str = Field(min_length=8)


class UserResponse(BaseModel):
    user_id: int
    email: str
    username: str
    role: str
    first_name: str
    last_name: str
    is_active: bool
    phone_number: Optional[str]
    
    class Config:
        orm_mode = True
def get_db():
    db = SessionLocal()  # Create a new session for each request
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after the request is completed


DB_DEPENDENCY = Annotated[Session, Depends(get_db)] # Annotated type for dependency injection of the database session
USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]

@router.get("/", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def read_user_information(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_details = db.query(Users).filter(Users.user_id == user.get("user_id")).first()
    if user_details:
        return user_details

    raise HTTPException(status_code=404, detail="User not found")


@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_password(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    password_update: PasswordUpdate
):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    user_id = user.get("user_id")
    user_details = db.query(Users).filter(Users.user_id == user_id).first()

    if user_details:
        if not bcrypt_context.verify(password_update.old_password, user_details.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect old password")

        user_details.hashed_password = bcrypt_context.hash(password_update.new_password)
        db.commit()
        return {"message": "Password updated successfully"}

    raise HTTPException(status_code=404, detail="User not found")


@router.put("/add-phone", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_phone(user: USER_DEPENDENCY,
                            db: DB_DEPENDENCY,
                            phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    user_id = user.get("user_id")
    user_details = db.query(Users).filter(Users.user_id == user_id).first()
    if user_details:
        user_details.phone_number = phone_number
        db.commit()
        return {"message": "Phone number updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")
