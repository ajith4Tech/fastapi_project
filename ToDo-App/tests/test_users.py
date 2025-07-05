from .utils import *
from routers.users import get_db, UserResponse
from routers.auth import get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_current_user

def test_read_users(test_user):
    response = client.get("/user/")  # Corrected path
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "user_id": 1,
        "username": "ajith",
        "email": "ajithbm01@gmail.com",
        "first_name": "Ajith",
        "last_name": "B M",
        "phone_number": "9876543210",
        "role": "admin",
        "is_active": True
    }

def test_update_user_password(test_user):
    update_user_request = {
        "old_password": "password",
        "new_password": "newpassword"
    }
    response = client.put("/user/", json=update_user_request)
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_update_user_password_invalid(test_user):
    update_user_request = {
        "old_password": "wrongpassword",
        "new_password": "newpassword"
    }
    response = client.put("/user/", json=update_user_request)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {
        "detail": "Incorrect old password"
    }

def test_update_user_phone_number(test_user):
    response = client.put("/user/add-phone", params={"phone_number": "9878900912"})
    assert response.status_code == status.HTTP_204_NO_CONTENT
