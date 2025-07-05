from database import Base
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from main import app
from models import ToDoItem, Users
import pytest
from routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
    poolclass = StaticPool,
)
#testing session local is isolated from production database
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
Base.metadata.create_all(bind=test_engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

def override_current_user():
    return {
        'username': 'ajith',
        'user_id': 1,
        'user_role': 'admin'
    }

client = TestClient(app)
@pytest.fixture
def test_todo():
    todo = ToDoItem(
        title="Test Todo",
        description="This is a test todo",
        completed=False,
        priority=1,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield db
    with test_engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()
        
@pytest.fixture
def test_user():
    user = Users(
        username="ajith",
        email="ajithbm01@gmail.com",
        first_name="Ajith",
        last_name="B M",
        phone_number="9876543210",
        role="admin",
        hashed_password=bcrypt_context.hash("password"),
        is_active=True
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield db
    with test_engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()