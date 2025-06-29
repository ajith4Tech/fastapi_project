"""
This module sets up the database connection and session management for the FastAPI application.
Primarily, it uses SQLAlchemy to create an SQLite database connection and manage sessions.
It defines the database URL, creates an engine, and establishes a session factory.
It also defines a base class for declarative models.
"""


from sqlalchemy import create_engine    #create engine is used to create a connection to the database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = "sqlite:///./todoapp.db" #location of the database file

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  #SessionLocal is a class that will be used to create a new session for each request

Base = declarative_base()  #Base is a class that will be used to create the tables in the database
