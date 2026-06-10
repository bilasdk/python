# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .webhook_config_response_dto import WebhookConfigResponseDto

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[List[WebhookConfigResponseDto]] = None
