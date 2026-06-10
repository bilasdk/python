# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .transfer_response_dto import TransferResponseDto
from .shared.pagination_meta_dto import PaginationMetaDto

__all__ = ["TransferListResponse", "Data"]


class Data(BaseModel):
    data: List[TransferResponseDto]
    """List of transfers"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class TransferListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
