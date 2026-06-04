# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["BankListResponse", "BankListResponseData"]


class BankListResponseData(BaseModel):
    id: str
    """Bank ID"""

    code: str
    """Bank code"""

    country: str
    """Country code"""

    name: str
    """Bank name"""

    type: Optional[str] = None
    """Bank type"""


class BankListResponse(BilaResponse):
    data: Optional[List[BankListResponseData]] = None
