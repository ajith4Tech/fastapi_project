from .utils import *
from routers.auth import get_db, get_current_user, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import timedelta
from fastapi import status
import pytest
from fastapi import HTTPException

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    authenticated_user = authenticate_user("ajith", "password", db)
    assert authenticated_user is not None
    assert authenticated_user.user_id == 1
    assert authenticated_user.username == "ajith"
    
    non_existent_user = authenticate_user("nonexistent", "password", db)
    assert non_existent_user is False
    
    wrong_password_user = authenticate_user("ajith", "wrongpassword", db)
    assert wrong_password_user is False

def test_create_access_token():
    username = 'ajith'
    user_id = 1
    role = 'admin'
    expires_delta = timedelta(minutes=15)
    access_token = create_access_token(username, user_id, role, expires_delta)
    decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_signature": False})
    assert decoded_token["sub"] == username
    assert decoded_token["id"] == user_id
    assert decoded_token["role"] == role
 
@pytest.mark.asyncio    
async def test_get_current_user_valid_token(test_user):  # Pass fixture
    db = TestingSessionLocal()
    encode = {'sub': 'ajith', 'id': 1, 'role': 'admin'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    authenticated_user = await get_current_user(token=token, db=db)
    
    assert authenticated_user["username"] == "ajith"
    assert authenticated_user["user_role"] == "admin"
    assert authenticated_user["user_id"] == 1
    

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    db = TestingSessionLocal()
    encode = {'role': 'user'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=token, db=db)
    
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert exc_info.value.detail == "Could not validate credentials"