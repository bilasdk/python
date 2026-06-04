# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["TransferRetrieveResponse", "TransferRetrieveResponseData", "TransferRetrieveResponseDataRecipient"]


class TransferRetrieveResponseDataRecipient(BaseModel):
    """Recipient details"""

    account_name: str = FieldInfo(alias="accountName")
    """Account holder / recipient name"""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """Bank account number (bank-account only)"""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """Bank name (bank-account only)"""

    operator: Optional[str] = None
    """Mobile money operator (mobile-money only)"""

    phone: Optional[str] = None
    """Phone number (mobile-money only)"""


class TransferRetrieveResponseData(BaseModel):
    id: str
    """Transfer ID"""

    amount: float
    """Transfer amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp (from Payment)"""

    currency: str
    """Currency code"""

    recipient: TransferRetrieveResponseDataRecipient
    """Recipient details"""

    reference: str
    """Client reference"""

    status: Literal["pending", "successful", "failed"]
    """Transfer status"""

    type: Literal["bank-account", "mobile-money"]
    """Transfer type"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Completion timestamp (from Payment.processedAt)"""

    narration: Optional[str] = None
    """Transfer narration"""


class TransferRetrieveResponse(BilaResponse):
    data: Optional[TransferRetrieveResponseData] = None
