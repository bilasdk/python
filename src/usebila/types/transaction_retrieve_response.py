# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .transaction_response_dto import TransactionResponseDto

__all__ = ["TransactionRetrieveResponse"]


class TransactionRetrieveResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[TransactionResponseDto] = None
