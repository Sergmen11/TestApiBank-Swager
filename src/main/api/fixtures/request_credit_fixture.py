import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.request_credit_request import RequestCreditRequest


@pytest.fixture
def request_credit_request(api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest, create_account_secret: CreateAccountResponse):
    request_credit = RequestCreditRequest(accountId=create_account_secret.id, amount=5000, termMonths=12)
    return request_credit