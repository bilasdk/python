# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionInitiateMobileMoneyCollectionParams"]


class CollectionInitiateMobileMoneyCollectionParams(TypedDict, total=False):
    amount: Required[float]
    """Collection amount"""

    country: Required[Literal["zm"]]
    """Country code"""

    operator: Required[Literal["airtel", "mtn", "zamtel"]]
    """Mobile money operator"""

    phone: Required[str]
    """Customer phone number"""

    reference: Required[str]
    """Unique client reference"""

    wallet_id: Required[Annotated[str, PropertyInfo(alias="walletId")]]
    """Target wallet ID to credit"""

    bearer: Literal["merchant", "customer"]
    """Who bears the transaction fee"""

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """Customer name for the transaction record"""

    narration: str
    """Collection narration"""
