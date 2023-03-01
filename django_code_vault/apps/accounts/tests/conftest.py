import pytest


@pytest.fixture
def user_details():
    return {"email": "test@gmail.com", "name": "test user"}
