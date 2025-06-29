"""
This module defines the different models for the To-Do application.
here model represents the database schema. Each model corresponds to a table in the database.
It uses SQLAlchemy to define the structure of the To-Do items.
"""

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class ToDoItem(Base):
    __tablename__ = "todos"
    todo_id = Column(Integer, primary_key=True, index=True)   # Primary key for the ToDos table
    title = Column(String) # Title of the ToDo item
    description = Column(String, nullable=True)  # Description of the ToDo item
    completed = Column(Boolean, default=False)  # Status of the ToDo item, default is False (not completed)
    priority = Column(Integer, default=1)  # Priority of the ToDo item, default is 1
    
    def __init__(self, title: str, description: str = None, completed: bool = False, priority: int = 1):
        self.title = title
        self.description = description
        self.completed = completed
        self.priority = priority