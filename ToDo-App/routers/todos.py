"""
This is the main routerlication file for the To-Do routerlication using FastAPI.
It defines the API endpoints for managing To-Do items, including creating, reading, updating, and deleting To-Do items.
It uses SQLAlchemy for database interactions and Pydantic for request validation.
The routerlication is structured to handle dependencies, such as database sessions, using FastAPI's dependency
"""
from typing import Annotated
from fastapi import  APIRouter, Depends, HTTPException, Path
from models import ToDoItem  # Import the Todos model
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field  # Import BaseModel for request validation
from .auth import get_current_user
router = APIRouter(
    prefix="/todos",
    tags=["todos"],
) 



def get_db():
    db = SessionLocal()  # Create a new session for each request
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after the request is completed


DB_DEPENDENCY = Annotated[Session, Depends(get_db)] # Annotated type for dependency injection of the database session
USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]
class ToDoRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100, description="Title of the To-Do item")
    description: str = Field(default=None, max_length=500, description="Description of the To-Do item")
    completed: bool = Field(default=False, description="Status of the To-Do item, default is False (not completed)")
    priority: int = Field(default=1, ge=1, le=5, description="Priority of the To-Do item, default is 1, must be between 1 and 5")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Sample To-Do",
                "description": "This is a sample To-Do item.",
                "completed": False,
                "priority": 1
            }
        }
        }


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_todos(user: USER_DEPENDENCY, db: DB_DEPENDENCY): #depends is used to inject the database session into the route handler
    """
    Returns all the To-Do items.
    """
    todos = db.query(ToDoItem).filter(ToDoItem.owner_id == user.get('user_id')).all()
    return todos

@router.get("/todos/{todo_id}",  status_code=status.HTTP_200_OK)
async def read_todo(user: USER_DEPENDENCY,
                    db: DB_DEPENDENCY,
                    todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo = db.query(ToDoItem).filter(ToDoItem.todo_id == todo_id and 
                                     ToDoItem.owner_id == user.get('user_id')).first()
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="To-Do item not found")

@router.post("/todos/add-todo", status_code=status.HTTP_201_CREATED)
async def add_todo(user: USER_DEPENDENCY, 
                   db: DB_DEPENDENCY, 
                   new_todo: ToDoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo = ToDoItem(**new_todo.model_dump(), owner_id=user.get('user_id'))  # Create a new To-Do item instance
    db.add(todo)
    db.commit()  # Commit the transaction to save the new To-Do item
    db.refresh(todo)  # Refresh the instance to get the updated data from the database
    return {"message": "To-Do item added successfully", "todo": todo}

@router.put("/todos/update-todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,  
    updated_todo: ToDoRequest,
    todo_id: int = Path(gt=0)
):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    todo = db.query(ToDoItem).filter(ToDoItem.todo_id == todo_id
                                     and ToDoItem.owner_id == user.get('user_id')).first()
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do item not found for update")

    for key, value in updated_todo.model_dump().items():
        setattr(todo, key, value)

    db.add(todo)
    db.commit()
    db.refresh(todo)

@router.delete("/todos/delete-todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: DB_DEPENDENCY,
                      user: USER_DEPENDENCY, 
                      todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    todo = db.query(ToDoItem).filter(ToDoItem.todo_id == todo_id
                                     and ToDoItem.owner_id == user.get('user_id')).first()
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do item not found for deletion")
    db.query(ToDoItem).filter(ToDoItem.todo_id == todo_id).delete()
    db.commit()