import json
from datetime import date
import pytest
import app.handlers as handlers
from app.model import UserLoginSchema, UserSchema, EventSchema
from app.database.mongo import MongoDBManager
from fastapi.testclient import TestClient
from main import app


TEST_USER_EMAIL = "test@email.com"
TEST_USER_PASSWORD = "random-passW0rd"
TEST_CLIENT = TestClient(app=app)
TODAY = date.today()
MONGODB = MongoDBManager('lisa')


@pytest.fixture(scope="module")
def normal_user_token_headers():
    return authentication_token_from_email()


def user_authentication_headers():
    data = {"email": TEST_USER_EMAIL, "password": TEST_USER_PASSWORD}
    r = TEST_CLIENT.post("/user/login", data=json.dumps(data))
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email():
    user = UserLoginSchema(email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)

    if not handlers.is_user_exists(user):
        user = UserSchema(email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD, fullname="Test User")
        handlers.create_user(user)

    return user_authentication_headers()


def test_greet():
    response = TEST_CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world!."}


def test_get_events():
    response = TEST_CLIENT.get("/events")
    assert response.status_code == 200


def test_create_event():
    event_data = {"title": "test_event", "organizer_email": TEST_USER_EMAIL,
                  "date": TODAY.strftime("%d/%m/%Y"), "description": "the test event"}

    response = TEST_CLIENT.post("/events", json=event_data, headers=authentication_token_from_email())
    assert response.status_code == 200
    assert response.json() == {"data": "event created."}


def test_user_login():
    login_data = {"email": TEST_USER_EMAIL, "password": TEST_USER_PASSWORD}
    response = TEST_CLIENT.post("/user/login", json=login_data)

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"


def test_create_user():
    return
