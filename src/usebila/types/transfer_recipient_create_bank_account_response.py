# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .recipient_response_dto import RecipientResponseDto

__all__ = ["TransferRecipientCreateBankAccountResponse"]


class TransferRecipientCreateBankAccountResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[RecipientResponseDto] = None
