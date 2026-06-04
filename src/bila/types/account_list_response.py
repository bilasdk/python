# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = [
    "AccountListResponse",
    "AccountListResponseData",
    "AccountListResponseDataData",
    "AccountListResponseDataDataDetails",
    "AccountListResponseDataMeta",
]


class AccountListResponseDataDataDetails(BaseModel):
    """Account details"""

    account_name: str = FieldInfo(alias="accountName")
    """Account holder name"""

    type: str
    """Account detail type"""

    till_number: Optional[str] = FieldInfo(alias="tillNumber", default=None)
    """Till number (for mobile money)"""


class AccountListResponseDataData(BaseModel):
    id: str
    """Account UUID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Account creation timestamp"""

    currency: str
    """Currency code"""

    details: AccountListResponseDataDataDetails
    """Account details"""

    status: Literal["active", "inactive", "suspended"]
    """Account status"""

    type: Literal["main", "sub", "virtual"]
    """Account type"""

    available_balance: Optional[str] = FieldInfo(alias="availableBalance", default=None)
    """Available balance"""

    ledger_balance: Optional[str] = FieldInfo(alias="ledgerBalance", default=None)
    """Ledger balance"""


class AccountListResponseDataMeta(BaseModel):
    """Pagination metadata"""

    current_page: float = FieldInfo(alias="currentPage")
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    per_page: float = FieldInfo(alias="perPage")
    """Items per page"""

    total: float
    """Total number of records"""


class AccountListResponseData(BaseModel):
    data: List[AccountListResponseDataData]
    """List of accounts"""

    meta: AccountListResponseDataMeta
    """Pagination metadata"""


class AccountListResponse(BilaResponse):
    data: Optional[AccountListResponseData] = None
