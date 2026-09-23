from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_secret_user_request import CreateSecretUserRequest
from src.main.api.models.repay_credit_request import RepayCreditRequest
import pytest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit
from sqlalchemy.orm import Session



"""тест на погашение кредита"""
@pytest.mark.api
class TestRepayCredit:
    # позитивный тест на погашение кредита
    def test_repay_credit(self, api_manager: ApiManager, db_session: Session, create_secret_user_request: CreateSecretUserRequest, repay_credit_request: RepayCreditRequest):
        response = api_manager.secret_user_steps.repay_credit(create_secret_user_request, repay_credit_request)

        # проверка id кредита
        assert repay_credit_request.creditId == response.creditId, "id кредита созданного аккаунта не совпадает, ошибка"

        repay_from_db = Credit.get_credit_by_amount(db_session, repay_credit_request.amount)

        assert repay_from_db.amount == repay_credit_request.amount, "Кредит не погашен, ошибка"

    # негативный тест на погашение кредита
    @pytest.mark.parametrize(
        "repay_credit_invalid_request, description",
        [
            (3000.0, "Частичное погашение"),
            (15000.0, "Погашение больше долга"),
            (1000.0, "Минимальное погашение"),
            (5001.0, "Погашение больше долга"),
        ],
        indirect=["repay_credit_invalid_request"],
        ids=["partial", "over", "minimal", "over_2"]
    )
    def test_repay_credit_invalid(self, api_manager: ApiManager, db_session: Session, create_secret_user_request: CreateSecretUserRequest,
                                  repay_credit_invalid_request: RepayCreditRequest, description):

        response = api_manager.secret_user_steps.repay_credit_invalid(create_secret_user_request, repay_credit_invalid_request)

        if hasattr(response, 'creditId'):
            assert response.creditId is None, f"Кредит погашен, ошибка: {description}"

        repay_from_db = Credit.get_credit_by_amount(db_session, repay_credit_invalid_request.amount)

        assert repay_from_db is None, f"Запись о погашении найдена в БД, ошибка: {description}"