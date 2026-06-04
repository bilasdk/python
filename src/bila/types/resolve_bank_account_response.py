# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["ResolveBankAccountResponse", "ResolveBankAccountResponseData"]


class ResolveBankAccountResponseData(BaseModel):
    account_name: str = FieldInfo(alias="accountName")
    """Account holder name"""

    country: str
    """Country code"""

    account_number: Optional[str] = FieldInfo(alias="accountNumber", default=None)
    """Bank account number"""

    bank_id: Optional[str] = FieldInfo(alias="bankId", default=None)
    """Bank ID"""

    bank_name: Optional[str] = FieldInfo(alias="bankName", default=None)
    """Bank name"""

    operator: Optional[str] = None
    """Mobile money operator"""

    phone: Optional[str] = None
    """Phone number"""


class ResolveBankAccountResponse(BilaResponse):
    data: Optional[ResolveBankAccountResponseData] = None
