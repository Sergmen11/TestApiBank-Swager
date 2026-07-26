from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
import pytest


"""тест на погашение кредита"""
@pytest.mark.api
class TestRepayCredit:
    # позитивный тест на погашение кредита
    def test_repay_credit(self, api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest, repay_credit_request: RepayCreditRequest):
        response = api_manager.secret_user_steps.repay_credit(create_secret_user_request, repay_credit_request)

        # проверка id кредита
        assert repay_credit_request.creditId == response.creditId

    # негативный тест на погашение кредита
    def test_repay_credit_invalid(self, api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest, repay_credit_invalid_request: RepayCreditRequest):

        response = api_manager.secret_user_steps.repay_credit_invalid(create_secret_user_request, repay_credit_invalid_request)