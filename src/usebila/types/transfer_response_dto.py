# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transfer_recipient_dto import TransferRecipientDto

__all__ = ["TransferResponseDto"]


class TransferResponseDto(BaseModel):
    id: str
    """Transfer ID"""

    amount: float
    """Transfer amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation timestamp (from Payment)"""

    currency: str
    """Currency code"""

    recipient: TransferRecipientDto
    """Recipient details"""

    reference: str
    """Client reference"""

    status: Literal["pending", "successful", "failed"]
    """Transfer status"""

    type: Literal["bank-account", "mobile-money"]
    """Transfer recipient type"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Completion timestamp (from Payment.processedAt)"""

    narration: Optional[str] = None
    """Transfer narration"""
