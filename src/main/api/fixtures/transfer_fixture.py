import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_fixture_model import TransferFixtureModel
from src.main.api.models.transfer_account_request import TransferAccountRequest


@pytest.fixture
def transfer_account_request(api_manager: ApiManager) -> TransferFixtureModel  :
    """Создаёт двух пользователей, два счёта, пополняет счёт отправителя"""

    # === ОТПРАВИТЕЛЬ ===
    sender_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(sender_request)

    account_sender = api_manager.user_steps.create_account(sender_request)
    sender_account_id = account_sender.id if hasattr(account_sender, 'id') else account_sender.json()["id"]

    deposit_request = RandomModelGenerator.generate(DepositAccountRequest, accountId=sender_account_id)
    api_manager.user_steps.deposit_account(sender_request, deposit_request)

    # === ПОЛУЧАТЕЛЬ ===
    receiver_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(receiver_request)

    account_receiver = api_manager.user_steps.create_account(receiver_request)
    receiver_account_id = account_receiver.id if hasattr(account_receiver, 'id') else account_receiver.json()["id"]

    # === ЗАПРОС НА ПЕРЕВОД ===
    # Сумма перевода должна быть <= баланса отправителя (5000)
    transfer_req = RandomModelGenerator.generate(
        TransferAccountRequest,
        fromAccountId=sender_account_id,
        toAccountId=receiver_account_id,
        amount=1000.0  # безопасная сумма, точно меньше баланса
    )

    # Возвращаем pydantic модель
    return TransferFixtureModel(
        sender_request=sender_request,
        sender_account_id=sender_account_id,
        receiver_request=receiver_request,
        receiver_account_id=receiver_account_id,
        deposit_amount=deposit_request.amount,
        transfer_request=transfer_req,
    )