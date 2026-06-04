# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["CollectionRetrieveResponse", "CollectionRetrieveResponseData", "CollectionRetrieveResponseDataCustomer"]


class CollectionRetrieveResponseDataCustomer(BaseModel):
    """Customer details"""

    name: str
    """Customer name"""

    operator: str
    """Mobile money operator"""

    phone: str
    """Customer phone number"""


class CollectionRetrieveResponseData(BaseModel):
    id: str
    """Collection ID"""

    amount: float
    """Collection amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Collection creation timestamp"""

    currency: str
    """Currency code"""

    customer: CollectionRetrieveResponseDataCustomer
    """Customer details"""

    reference: str
    """Client reference"""

    status: Literal["pending", "successful", "failed", "otp-required", "pay-offline"]
    """Collection status"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Collection completion timestamp"""

    fee_bearer: Optional[Literal["merchant", "customer"]] = FieldInfo(alias="feeBearer", default=None)
    """Who bears the collection platform fee"""

    narration: Optional[str] = None
    """Collection narration"""


class CollectionRetrieveResponse(BilaResponse):
    data: Optional[CollectionRetrieveResponseData] = None
