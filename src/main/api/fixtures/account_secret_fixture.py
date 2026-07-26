import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest


@pytest.fixture
def create_account_secret(api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest):
    response = api_manager.user_steps.create_account(create_secret_user_request)
    return response