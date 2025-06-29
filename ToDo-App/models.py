"""
This module defines the different models for the To-Do application.
here model represents the database schema. Each model corresponds to a table in the database.
It uses SQLAlchemy to define the structure of the To-Do items.
"""

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # Primary key for the Users table
    email = Column(String, unique=True, index=True)  # Unique email for the user
    username = Column(String, unique=True) # Unique username for the user
    first_name = Column(String, nullable=True) 
    last_name = Column(String, nullable=True)  
    hashed_password = Column(String)  
    is_active = Column(Boolean, default=True)
    role = Column(String)
    



class ToDoItem(Base):
    __tablename__ = "todos"
    todo_id = Column(Integer, primary_key=True, index=True)   # Primary key for the ToDos table
    title = Column(String) # Title of the ToDo item
    description = Column(String, nullable=True)  
    completed = Column(Boolean, default=False)  
    priority = Column(Integer, default=1)  
    owner_id = Column(Integer, ForeignKey("users.user_id"))  # Foreign key to the Users table, linking the ToDo item to a user
   
        
