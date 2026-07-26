import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest

@pytest.fixture
def create_secret_user_request(api_manager: ApiManager):
    user_secret = RandomModelGenerator.generate(CreateSecretUserRequest)
    api_manager.admin_steps.create_user_secret(user_secret)
    return user_secret