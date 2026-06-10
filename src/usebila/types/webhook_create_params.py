# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    events: Required[
        List[
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
    ]
    """Event types to subscribe to"""

    url: Required[str]
    """Webhook endpoint URL"""
