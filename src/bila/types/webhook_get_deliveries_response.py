# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = [
    "WebhookGetDeliveriesResponse",
    "WebhookGetDeliveriesResponseData",
    "WebhookGetDeliveriesResponseDataData",
    "WebhookGetDeliveriesResponseDataMeta",
]


class WebhookGetDeliveriesResponseDataData(BaseModel):
    id: str
    """Delivery UUID"""

    attempts: float
    """Number of delivery attempts"""

    created_at: datetime = FieldInfo(alias="createdAt")

    delivered_at: Optional[datetime] = FieldInfo(alias="deliveredAt", default=None)
    """When the delivery succeeded"""

    event_type: str = FieldInfo(alias="eventType")
    """Webhook event type"""

    failed_at: Optional[datetime] = FieldInfo(alias="failedAt", default=None)
    """When the delivery permanently failed"""

    max_attempts: float = FieldInfo(alias="maxAttempts")
    """Maximum delivery attempts"""

    next_retry_at: Optional[datetime] = FieldInfo(alias="nextRetryAt", default=None)
    """When the next retry is scheduled"""

    payload: Dict[str, object]
    """Event payload JSON as stored for delivery"""

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)
    """Response body from the merchant endpoint (truncated)"""

    response_status: Optional[float] = FieldInfo(alias="responseStatus", default=None)
    """HTTP status code from the merchant endpoint"""

    status: Literal["QUEUED", "DELIVERED", "FAILED", "RETRYING"]
    """Delivery status"""

    webhook_config_id: str = FieldInfo(alias="webhookConfigId")
    """Webhook config UUID"""


class WebhookGetDeliveriesResponseDataMeta(BaseModel):
    """Pagination metadata"""

    current_page: float = FieldInfo(alias="currentPage")
    """Current page number"""

    page_count: float = FieldInfo(alias="pageCount")
    """Total number of pages"""

    per_page: float = FieldInfo(alias="perPage")
    """Items per page"""

    total: float
    """Total number of records"""


class WebhookGetDeliveriesResponseData(BaseModel):
    data: List[WebhookGetDeliveriesResponseDataData]
    """List of webhook deliveries"""

    meta: WebhookGetDeliveriesResponseDataMeta
    """Pagination metadata"""


class WebhookGetDeliveriesResponse(BilaResponse):
    data: Optional[WebhookGetDeliveriesResponseData] = None
