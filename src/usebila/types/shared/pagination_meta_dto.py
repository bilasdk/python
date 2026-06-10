# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaginationMetaDto"]


class PaginationMetaDto(BaseModel):
    current_page: float = FieldInfo(alias="currentPage")
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    per_page: float = FieldInfo(alias="perPage")
    """Items per page"""

    total: float
    """Total number of records"""
