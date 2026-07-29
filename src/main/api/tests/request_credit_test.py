from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.request_credit_invalid_fixture import request_credit_invalid_request
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.request_credit_request import RequestCreditRequest
import pytest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from sqlalchemy.orm import Session


"""тест для запроса на кредит"""
@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(self, api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest,
                            request_credit_request: RequestCreditRequest, db_session: Session):

        # позитивный тест на получение кредита
        response = api_manager.secret_user_steps.request_credit(create_secret_user_request, request_credit_request)

        # проверка срока кредита
        assert request_credit_request.termMonths == response.termMonths, "срок кредита не совпадает, ошибка"
        # проверка суммы кредита
        assert request_credit_request.amount == response.amount, "суммы кредита не совпадают, ошибка"

        # проверка создания кредита в базе данных
        credit_from_db = Credit.get_credit_by_id(db_session, request_credit_request.accountId)
        # проверка создания id кредита в базе данных
        assert credit_from_db.account_id == response.id, "кредитного Id нет в БД"


    def test_request_credit_invalid(self, db_session: Session, api_manager: ApiManager, create_secret_user_request: CreateSecretUserRequest,
                                    request_credit_invalid_request: RequestCreditRequest):
        # негативный тест на получение кредита
        response = api_manager.secret_user_steps.request_credit_invalid(create_secret_user_request, request_credit_invalid_request)

        if hasattr(response, 'creditId'):
            assert response.creditId is None, "creditId не должен создаваться при ошибке"

        credit_from_db = Credit.get_credit_by_id(db_session, request_credit_invalid_request.accountId)
        # проверка создания кредита в базе данных
        assert credit_from_db is None, "id кредита создан, ошибка"