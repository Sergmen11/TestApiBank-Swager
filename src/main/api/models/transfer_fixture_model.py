from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from pydantic import Field


class TransferFixtureModel(BaseModel):
    sender_request: CreateUserRequest
    sender_account_id: int = Field(gt=0)
    receiver_request: CreateUserRequest
    receiver_account_id: int = Field(gt=0)
    deposit_amount: float = Field(gt=0)
    transfer_request: TransferAccountRequest