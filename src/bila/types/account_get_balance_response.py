# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["AccountGetBalanceResponse", "AccountGetBalanceResponseData"]


class AccountGetBalanceResponseData(BaseModel):
    available_balance: str = FieldInfo(alias="availableBalance")
    """Available balance"""

    currency: str
    """Currency code"""

    ledger_balance: str = FieldInfo(alias="ledgerBalance")
    """Ledger balance"""


class AccountGetBalanceResponse(BilaResponse):
    data: Optional[AccountGetBalanceResponseData] = None
