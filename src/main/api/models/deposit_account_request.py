from src.main.api.models.base_model import BaseModel
from src.main.api.generators.creation_rule import CreationRule
from typing import Annotated


class DepositAccountRequest(BaseModel):
    accountId: int
    amount: Annotated[float, CreationRule(regex=r'^([1-8]\d{3}|9000)(\.\d+)?$')]