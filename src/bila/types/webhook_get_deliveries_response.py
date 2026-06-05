# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination_meta_dto import PaginationMetaDto

__all__ = ["WebhookGetDeliveriesResponse", "Data", "DataData"]


class DataData(BaseModel):
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


class Data(BaseModel):
    data: List[DataData]
    """List of webhook deliveries"""

    meta: PaginationMetaDto
    """Pagination metadata"""


class WebhookGetDeliveriesResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
