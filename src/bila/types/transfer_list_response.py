# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = [
    "TransferListResponse",
    "TransferListResponseData",
    "TransferListResponseDataData",
    "TransferListResponseDataDataRecipient",
    "TransferListResponseDataMeta",
]


class TransferListResponseDataDataRecipient(BaseModel):
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


class TransferListResponseDataData(BaseModel):
    id: str
    """Transfer ID"""

    amount: float
    """Transfer amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp (from Payment)"""

    currency: str
    """Currency code"""

    recipient: TransferListResponseDataDataRecipient
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


class TransferListResponseDataMeta(BaseModel):
    """Pagination metadata"""

    current_page: float = FieldInfo(alias="currentPage")
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    per_page: float = FieldInfo(alias="perPage")
    """Items per page"""

    total: float
    """Total number of records"""


class TransferListResponseData(BaseModel):
    data: List[TransferListResponseDataData]
    """List of transfers"""

    meta: TransferListResponseDataMeta
    """Pagination metadata"""


class TransferListResponse(BilaResponse):
    data: Optional[TransferListResponseData] = None
