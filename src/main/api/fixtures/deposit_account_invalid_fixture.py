import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.fixture
def deposit_account_invalid_request(api_manager: ApiManager, create_user_request: CreateUserRequest, create_account_response: CreateAccountResponse, request):
    amount = request.param
    account_request_invalid = DepositAccountRequest.model_construct(accountId=create_account_response.id, amount=amount)
    return account_request_invalid