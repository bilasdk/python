# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RecipientResponseDto"]


class RecipientResponseDto(BaseModel):
    id: str
    """Recipient UUID"""

    account_name: str = FieldInfo(alias="accountName")
    """Account holder name"""

    country: str
    """Country code"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp"""

    type: Literal["bank-account", "mobile-money"]
    """Transfer recipient type"""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """Bank account number (bank-account only)"""

    bank_id: Optional[str] = FieldInfo(alias="bankId", default=None)
    """Bank ID (bank-account only)"""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """Bank name (bank-account only)"""

    operator: Optional[str] = None
    """Mobile money operator (mobile-money only)"""

    phone: Optional[str] = None
    """Phone number (mobile-money only)"""
