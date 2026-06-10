# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookGetDeliveriesParams"]


class WebhookGetDeliveriesParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """ISO 8601 end of createdAt range (inclusive)"""

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """Filter by event type"""

    page: float
    """Page number"""

    per_page: Annotated[float, PropertyInfo(alias="perPage")]
    """Items per page"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """ISO 8601 start of createdAt range (inclusive)"""

    status: str
    """Filter by status (QUEUED, DELIVERED, FAILED, RETRYING)"""
