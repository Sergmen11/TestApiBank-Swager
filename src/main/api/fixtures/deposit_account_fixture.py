import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def deposit_account_request(api_manager: ApiManager, create_user_request: CreateUserRequest, create_account_response: CreateAccountResponse):
    account_request = RandomModelGenerator.generate(DepositAccountRequest, accountId=create_account_response.id)
    api_manager.user_steps.deposit_account(create_user_request, account_request)
    return account_request