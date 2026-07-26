import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.request_credit_request import RequestCreditRequest


@pytest.fixture
def repay_credit_request(api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest, request_credit_request: RequestCreditRequest):
    credit_response = api_manager.secret_user_steps.request_credit(create_secret_user_request, request_credit_request)
    repay_credit = RepayCreditRequest(creditId=credit_response.creditId, accountId=credit_response.id, amount=5000)
    return repay_credit