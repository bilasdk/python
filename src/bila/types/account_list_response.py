# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_response_dto import AccountResponseDto
from .shared.pagination_meta_dto import PaginationMetaDto

__all__ = ["AccountListResponse", "Data"]


class Data(BaseModel):
    data: List[AccountResponseDto]
    """List of accounts"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class AccountListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
