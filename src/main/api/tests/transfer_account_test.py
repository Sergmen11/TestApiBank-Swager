from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
import pytest
from src.main.api.db.crud.transaction_crud import Transaction
from src.main.api.fixtures.db_fixture import db_session

"""тесты для перевода средств между аккаунтами"""
@pytest.mark.api
class TestTransferAccount:
    # позитивный тест на перевод средств
    def test_transfer_account(self, db_session: Session, api_manager: ApiManager,  transfer_account_request: dict):
        sender_request = transfer_account_request["sender_request"]
        transfer_req = transfer_account_request["transfer_request"]

        response = api_manager.user_steps.transfer_account(sender_request, transfer_req)

        transaction_from_db = db_session.query(Transaction).filter_by(
            from_account_id=response.fromAccountId,
            to_account_id=response.toAccountId,
            amount=transfer_req.amount
        ).first()

        # Проверяем, что транзакция вообще создалась
        assert transaction_from_db is not None, "Транзакция не найдена в базе данных!"
        # Проверяем, что все поля соответствуют запросу
        assert transfer_account_request["sender_account_id"] == transaction_from_db.from_account_id
        assert transfer_account_request["receiver_account_id"] == transaction_from_db.to_account_id
        assert transfer_req.amount == transaction_from_db.amount

    # негативный тест на перевод средств(Недостаточно средств или сумма перевода превышена)
    def test_transfer_account_invalid(self, api_manager: ApiManager, transfer_account_request_invalid: dict):
        sender_request = transfer_account_request_invalid["sender_request"]
        transfer_req = transfer_account_request_invalid["transfer_request"]
        response = api_manager.user_steps.transfer_account_invalid(sender_request, transfer_req)