# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .transaction_response_dto import TransactionResponseDto
from .shared.pagination_meta_dto import PaginationMetaDto

__all__ = ["TransactionListResponse", "Data"]


class Data(BaseModel):
    data: List[TransactionResponseDto]
    """List of transactions"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class TransactionListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
