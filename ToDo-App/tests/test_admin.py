from .utils import *
from routers.admin import get_db, get_current_user
from fastapi import status
from models import ToDoItem


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_current_user

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        "title": "Test Todo",
        "description": "This is a test todo",
        "completed": False,
        "priority": 1,
        "todo_id": 1,
        "owner_id": 1
    }]


def test_admin_delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    test_model = db.query(ToDoItem).filter(ToDoItem.todo_id == 1).first()
    assert test_model is None

def test_admin_delete_todo_not_found(test_todo):
    response = client.delete("/admin/todo/2")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': "To-Do item not found for deletion"}
    
def test_admin_read_all_users():
    response = client.get("/admin/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []