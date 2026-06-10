# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .resolved_account_response_dto import ResolvedAccountResponseDto

__all__ = ["ResolveMobileMoneyResponse"]


class ResolveMobileMoneyResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[ResolvedAccountResponseDto] = None
