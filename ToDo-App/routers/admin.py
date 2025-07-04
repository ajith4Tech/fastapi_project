from typing import Annotated, List
from fastapi import  APIRouter, Depends, HTTPException, Path
from models import ToDoItem, Users  # Import the Todos model
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field  # Import BaseModel for request validation
from .auth import get_current_user
from .users import UserResponse
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
) 



def get_db():
    db = SessionLocal()  # Create a new session for each request
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after the request is completed


DB_DEPENDENCY = Annotated[Session, Depends(get_db)] # Annotated type for dependency injection of the database session
USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]

@router.get('/todo', status_code=status.HTTP_200_OK)
async def read_all(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    if user is None :
        raise HTTPException(status_code=401, detail="Authentication Failed")
    if user.get('user_role') != 'admin':
        raise HTTPException(status_code=403, detail="Access Denied")
    todos = db.query(ToDoItem).all()
    return todos

@router.delete('/todo/{todo_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: DB_DEPENDENCY,
                      user: USER_DEPENDENCY, 
                      todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    if user.get('user_role') != 'admin':
        raise HTTPException(status_code=403, detail="Access Denied")
    todo = db.query(ToDoItem).filter(ToDoItem.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do item not found for deletion")
    db.delete(todo)
    db.commit()
    
@router.get('/users/', response_model=List[UserResponse],status_code=status.HTTP_200_OK)
async def read_all_users(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    if user is None :
        raise HTTPException(status_code=401, detail="Authentication Failed")
    if user.get('user_role') != 'admin':
        raise HTTPException(status_code=403, detail="Access Denied")
    users = db.query(Users).all()
    return users