from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
import pytest


"""тесты на пополнение аккаунта"""
@pytest.mark.api
class TestDepositAccount:
    # позитивный тест на пополнение аккаунта
    def test_deposit_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):

        response = api_manager.user_steps.deposit_account(create_user_request, deposit_account_request)

        # проверка аккаунта id
        assert response.id == deposit_account_request.accountId


    # негативный тест на пополнение аккаунта (проверка прав доступа)
    def test_deposit_account_invalid(self, api_manager: ApiManager, deposit_account_request: DepositAccountRequest):

        response = api_manager.user_steps.deposit_account_invalid(deposit_account_request)