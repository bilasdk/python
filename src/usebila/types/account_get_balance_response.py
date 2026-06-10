# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountGetBalanceResponse", "Data"]


class Data(BaseModel):
    available_balance: str = FieldInfo(alias="availableBalance")
    """Available balance"""

    currency: str
    """Currency code"""

    ledger_balance: str = FieldInfo(alias="ledgerBalance")
    """Ledger balance"""


class AccountGetBalanceResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
