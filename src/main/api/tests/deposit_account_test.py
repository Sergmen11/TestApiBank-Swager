from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
import pytest
from sqlalchemy.orm import Session
from src.main.api.db.crud.account_crud import AccountCrudDb as Account

"""тесты на пополнение аккаунта"""
@pytest.mark.api
class TestDepositAccount:
    # позитивный тест на пополнение аккаунта
    def test_deposit_account(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):

        deposit_amount = deposit_account_request.amount

        # 1. Получаем баланс до пополнения
        account_before = Account.get_account_by_id(db_session, deposit_account_request.accountId)
        balance_before = account_before.balance

        response = api_manager.user_steps.deposit_account(create_user_request, deposit_account_request)

        # проверка аккаунта id
        assert response.id == deposit_account_request.accountId, "Аккаунт id не совпадает, ошибка"

        db_session.expire_all()

        # подключение к БД
        from_deposit_account_db = Account.get_account_by_id(db_session, deposit_account_request.accountId)

        # 4. Получаем аккаунт ПОСЛЕ пополнения
        from_deposit_account_db = Account.get_account_by_id(db_session, deposit_account_request.accountId)

        expected_balance = balance_before + deposit_amount
        assert from_deposit_account_db.balance == expected_balance, f"Баланс не обновился! Ожидалось: {expected_balance}, получено: {from_deposit_account_db.balance}"




    # негативный тест на пополнение аккаунта (неверное тело запроса)
    @pytest.mark.parametrize(
        "deposit_account_invalid_request, description",
        [
            (-1, "отрицательное значение"),
            ("123", "строка"),
            (12944127490712471221442, "длинное значение"),
            (0, "нулевое значение"),
            ("asdsfaf", "строка"),
            ("", "пустая строка")
        ],
        indirect=["deposit_account_invalid_request"],
        ids=["negative", "string", "zero", "too_large", "string", "empty"]
    )
    def test_deposit_account_invalid(self, api_manager: ApiManager, db_session: Session, create_user_request: CreateUserRequest,
                                     deposit_account_invalid_request: DepositAccountRequest, description: str):

        response = api_manager.user_steps.deposit_account_invalid(create_user_request, deposit_account_invalid_request)

        assert response is None, f"Запрос должен быть отвергнут, но прошел успешно. Описание: {description}"

        from_deposit_account_db = Account.get_account_by_id(db_session, deposit_account_invalid_request.accountId)

        assert from_deposit_account_db is not None, "id аккаунта создано в бд, ошибка"