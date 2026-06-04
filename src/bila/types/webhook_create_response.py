# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["WebhookCreateResponse", "WebhookCreateResponseData"]


class WebhookCreateResponseData(BaseModel):
    id: str
    """Webhook config UUID"""

    created_at: datetime = FieldInfo(alias="createdAt")

    events: List[str]
    """Subscribed event types"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the webhook is active"""

    merchant_id: str = FieldInfo(alias="merchantId")
    """Merchant UUID"""

    secret: str
    """Signing secret; plaintext only on create/rotate-secret, otherwise masked"""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
    """Webhook endpoint URL"""


class WebhookCreateResponse(BilaResponse):
    data: Optional[WebhookCreateResponseData] = None
