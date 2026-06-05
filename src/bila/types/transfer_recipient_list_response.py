# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .recipient_response_dto import RecipientResponseDto
from .shared.pagination_meta_dto import PaginationMetaDto

__all__ = ["TransferRecipientListResponse", "Data"]


class Data(BaseModel):
    data: List[RecipientResponseDto]
    """List of recipients"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class TransferRecipientListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
