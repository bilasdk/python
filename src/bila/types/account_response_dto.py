# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .account_details_dto import AccountDetailsDto

__all__ = ["AccountResponseDto"]


class AccountResponseDto(BaseModel):
    id: str
    """Account UUID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Account creation timestamp"""

    currency: str
    """Currency code"""

    details: AccountDetailsDto
    """Account details"""

    status: Literal["active", "inactive", "suspended"]
    """Account status"""

    type: Literal["main", "sub", "virtual"]
    """Account type"""

    available_balance: Optional[str] = FieldInfo(alias="availableBalance", default=None)
    """Available balance"""

    ledger_balance: Optional[str] = FieldInfo(alias="ledgerBalance", default=None)
    """Ledger balance"""
