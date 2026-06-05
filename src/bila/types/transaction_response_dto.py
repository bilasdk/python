# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionResponseDto"]


class TransactionResponseDto(BaseModel):
    id: str
    """Transaction UUID"""

    account_id: str = FieldInfo(alias="accountId")
    """Account / wallet ID"""

    amount: float
    """Transaction amount"""

    balance_after: float = FieldInfo(alias="balanceAfter")
    """Balance after transaction"""

    balance_before: float = FieldInfo(alias="balanceBefore")
    """Balance before transaction"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Transaction timestamp"""

    currency: str
    """Currency code"""

    status: Literal["pending", "successful", "failed", "cancelled"]
    """Transaction status"""

    type: Literal["credit", "debit"]
    """Transaction type"""

    description: Optional[str] = None
    """Transaction description"""

    reference: Optional[str] = None
    """Client reference"""
