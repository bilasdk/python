# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .transfer_response_dto import TransferResponseDto

__all__ = ["TransferInitiateMobileMoneyTransferResponse"]


class TransferInitiateMobileMoneyTransferResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[TransferResponseDto] = None
