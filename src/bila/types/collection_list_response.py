# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.pagination_meta_dto import PaginationMetaDto
from .bila_collection_response_dto import BilaCollectionResponseDto

__all__ = ["CollectionListResponse", "Data"]


class Data(BaseModel):
    data: List[BilaCollectionResponseDto]
    """List of collections"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class CollectionListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
