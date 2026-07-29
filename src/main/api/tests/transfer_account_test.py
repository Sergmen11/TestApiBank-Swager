from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
import pytest
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction
from src.main.api.fixtures.db_fixture import db_session
from src.main.api.models.transfer_fixture_model import TransferFixtureModel
from src.main.api.models.transfer_fixture_model_invalid import TransferFixtureModelInvalid

"""тесты для перевода средств между аккаунтами"""
@pytest.mark.api
class TestTransferAccount:
    # позитивный тест на перевод средств
    def test_transfer_account(self, db_session: Session, api_manager: ApiManager,  transfer_account_request: TransferFixtureModel):

        response = api_manager.user_steps.transfer_account(transfer_account_request.sender_request, transfer_account_request.transfer_request)

        # проверяем id аккаунтов
        assert transfer_account_request.sender_account_id == response.fromAccountId, "id аккаунта отправителя не соответствует id в ответе, ошибка"
        assert transfer_account_request.receiver_account_id == response.toAccountId, "id аккаунта получателя не соответствует id в ответе, ошибка"

        # подключение к базе данных, проверка суммы перевода
        transaction_from_db = Transaction.get_transaction_by_amount(db_session, transfer_account_request.transfer_request.amount)

        # проверяем сумму перевода на другой аккаунт
        assert transaction_from_db.amount == transfer_account_request.transfer_request.amount, "Сумма перевода не соответствует сумме в базе данных, ошибка"

    # негативный тест на перевод средств(Недостаточно средств или сумма перевода превышена)
    def test_transfer_account_invalid(self, db_session: Session, api_manager: ApiManager, transfer_account_request_invalid: TransferFixtureModelInvalid):

        api_manager.user_steps.transfer_account_invalid(transfer_account_request_invalid.sender_request, transfer_account_request_invalid.transfer_request)

        assert transfer_account_request_invalid.sender_account_id is not None, "Аккаунт отправителя не создан в фикстуре"
        assert transfer_account_request_invalid.receiver_account_id is not None, "Аккаунт получателя не создан в фикстуре"


        # подключение к базе данных, проверка суммы перевода
        transaction_from_db = Transaction.get_transaction_by_amount(db_session, transfer_account_request_invalid.transfer_request.amount)

        assert transaction_from_db is None, "Сумма перевода зарегистрирована в базе данных, ошибка"