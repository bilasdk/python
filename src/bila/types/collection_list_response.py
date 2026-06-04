# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = [
    "CollectionListResponse",
    "CollectionListResponseData",
    "CollectionListResponseDataData",
    "CollectionListResponseDataDataCustomer",
    "CollectionListResponseDataMeta",
]


class CollectionListResponseDataDataCustomer(BaseModel):
    """Customer details"""

    name: str
    """Customer name"""

    operator: str
    """Mobile money operator"""

    phone: str
    """Customer phone number"""


class CollectionListResponseDataData(BaseModel):
    id: str
    """Collection ID"""

    amount: float
    """Collection amount"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Collection creation timestamp"""

    currency: str
    """Currency code"""

    customer: CollectionListResponseDataDataCustomer
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


class CollectionListResponseDataMeta(BaseModel):
    """Pagination metadata"""

    current_page: float = FieldInfo(alias="currentPage")
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    per_page: float = FieldInfo(alias="perPage")
    """Items per page"""

    total: float
    """Total number of records"""


class CollectionListResponseData(BaseModel):
    data: List[CollectionListResponseDataData]
    """List of collections"""

    meta: CollectionListResponseDataMeta
    """Pagination metadata"""


class CollectionListResponse(BilaResponse):
    data: Optional[CollectionListResponseData] = None
