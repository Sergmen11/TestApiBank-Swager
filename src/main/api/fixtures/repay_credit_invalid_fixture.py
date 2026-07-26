import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
from src.main.api.models.request_credit_request import RequestCreditRequest


@pytest.fixture
def repay_credit_invalid_request(api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest, request_credit_request: RequestCreditRequest):
    repay_credit_invalid = RepayCreditRequest(creditId=9999, accountId=9999, amount=5000)
    return repay_credit_invalid