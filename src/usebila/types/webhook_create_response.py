# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .webhook_config_response_dto import WebhookConfigResponseDto

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[WebhookConfigResponseDto] = None
