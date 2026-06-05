# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BankListResponse", "Data"]


class Data(BaseModel):
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


class BankListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[List[Data]] = None
