# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .account_response_dto import AccountResponseDto

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[AccountResponseDto] = None
