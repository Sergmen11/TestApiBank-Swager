import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_account_response(api_manager: ApiManager, create_user_request: CreateUserRequest):
    response = api_manager.user_steps.create_account(create_user_request)
    return response