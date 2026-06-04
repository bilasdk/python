# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["AccountRetrieveResponse", "AccountRetrieveResponseData", "AccountRetrieveResponseDataDetails"]


class AccountRetrieveResponseDataDetails(BaseModel):
    """Account details"""

    account_name: str = FieldInfo(alias="accountName")
    """Account holder name"""

    type: str
    """Account detail type"""

    till_number: Optional[str] = FieldInfo(alias="tillNumber", default=None)
    """Till number (for mobile money)"""


class AccountRetrieveResponseData(BaseModel):
    id: str
    """Account UUID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Account creation timestamp"""

    currency: str
    """Currency code"""

    details: AccountRetrieveResponseDataDetails
    """Account details"""

    status: Literal["active", "inactive", "suspended"]
    """Account status"""

    type: Literal["main", "sub", "virtual"]
    """Account type"""

    available_balance: Optional[str] = FieldInfo(alias="availableBalance", default=None)
    """Available balance"""

    ledger_balance: Optional[str] = FieldInfo(alias="ledgerBalance", default=None)
    """Ledger balance"""


class AccountRetrieveResponse(BilaResponse):
    data: Optional[AccountRetrieveResponseData] = None
