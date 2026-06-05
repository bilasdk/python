# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bila_collection_response_dto import BilaCollectionResponseDto

__all__ = ["CollectionInitiateMobileMoneyCollectionResponse"]


class CollectionInitiateMobileMoneyCollectionResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[BilaCollectionResponseDto] = None
