# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_collection_customer_dto import BilaCollectionCustomerDto

__all__ = ["BilaCollectionResponseDto"]


class BilaCollectionResponseDto(BaseModel):
    id: str
    """Collection ID"""

    amount: float
    """Collection amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Collection creation timestamp"""

    currency: str
    """Currency code"""

    customer: BilaCollectionCustomerDto
    """Customer details"""

    reference: str
    """Client reference"""

    status: Literal["pending", "successful", "failed", "otp-required", "pay-offline"]
    """Collection status"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Collection completion timestamp"""

    fee_bearer: Optional[Literal["merchant", "customer"]] = FieldInfo(alias="feeBearer", default=None)
    """Who bears the transaction fee"""

    narration: Optional[str] = None
    """Collection narration"""
