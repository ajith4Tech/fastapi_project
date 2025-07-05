from routers.todos import get_db, get_current_user
from fastapi import status
from models import ToDoItem
from .utils import *



app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_current_user




        
def test_read_all_authenticated(test_todo):
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
            'completed': False,
            'title': 'Test Todo',
            'description': 'This is a test todo',
            'priority': 1,
            'owner_id': 1,
            'todo_id': 1
        }]

def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
            'completed': False,
            'title': 'Test Todo',
            'description': 'This is a test todo',
            'priority': 1,
            'owner_id': 1,
            'todo_id': 1
        }

def test_read_one_authenticated_not_found():
    response = client.get("/todos/todos/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'To-Do item not found'}
    

def test_create_todo(test_todo):
    request_body = {
        "title": "Test Todo",
        "description": "This is a test todo",
        "completed": False,
        "priority": 1
    }
    response = client.post("/todos/todos/add-todo", json=request_body)
    assert response.status_code == status.HTTP_201_CREATED
    
    # Check if the To-Do item was added to the database and Adding a new To-Do item
    db = TestingSessionLocal()
    todo_model = db.query(ToDoItem).filter(ToDoItem.todo_id == 2).first()
    assert todo_model.title == request_body['title']
    assert todo_model.description == request_body['description']
    assert todo_model.completed == request_body['completed']
    assert todo_model.priority == request_body['priority']

def test_update_todo(test_todo):
    request_body = {
        "title": "Chanhed the title",
        "description": "This is a test todo",
        "completed": False,
        "priority": 3
    }
    response = client.put("/todos/todos/update-todo/1", json=request_body)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    test_model = db.query(ToDoItem).filter(ToDoItem.todo_id == 1).first()
    assert test_model.title == request_body['title']

def test_update_todo_not_found():
    request_body = {
        "title": "Chanhed the title",
        "description": "This is a test todo",
        "completed": False,
        "priority": 3
    }
    response = client.put("/todos/todos/update-todo/99", json=request_body)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': "To-Do item not found for update"}
    

def test_delete_todo(test_todo):
    response = client.delete("/todos/todos/delete-todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    test_model = db.query(ToDoItem).filter(ToDoItem.todo_id == 1).first()
    assert test_model is None

def test_delete_todo_not_found():
    response = client.delete("/todos/todos/delete-todo/99")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': "To-Do item not found for deletion"}