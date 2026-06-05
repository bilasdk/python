# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferInitiateMobileMoneyTransferParams"]


class TransferInitiateMobileMoneyTransferParams(TypedDict, total=False):
    amount: Required[float]
    """Transfer amount"""

    country: Required[Literal["zm"]]
    """Country code"""

    operator: Required[Literal["airtel", "mtn", "zamtel"]]
    """Mobile money operator"""

    phone: Required[str]
    """Recipient phone number"""

    reference: Required[str]
    """Unique client reference"""

    narration: str
    """Transfer narration"""

    recipient_name: Annotated[str, PropertyInfo(alias="recipientName")]
    """Recipient name for the transaction record"""

    wallet_id: Annotated[str, PropertyInfo(alias="walletId")]
    """Source wallet ID to debit (defaults to main wallet if omitted)"""
