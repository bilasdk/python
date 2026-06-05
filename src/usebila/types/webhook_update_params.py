# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    events: List[
        Literal[
            "order.created",
            "order.paid",
            "order.cancelled",
            "stock.low",
            "payment.created",
            "payment.completed",
            "payment.failed",
            "collection.pending",
            "collection.completed",
            "collection.failed",
            "withdrawal.created",
            "withdrawal.completed",
            "withdrawal.failed",
            "transaction.updated",
            "transfer.pending",
            "transfer.completed",
            "transfer.failed",
            "settlement.completed",
        ]
    ]
    """Event types to subscribe to"""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether the webhook is active"""

    url: str
    """Webhook endpoint URL"""
