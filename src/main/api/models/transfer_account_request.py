from src.main.api.models.base_model import BaseModel
from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule


class TransferAccountRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: Annotated[float, CreationRule(regex='^([1-8]\d{3}|9000)(\.\d+)?$')]