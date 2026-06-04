# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferInitiateBankTransferParams"]


class TransferInitiateBankTransferParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """Source account UUID"""

    amount: Required[float]
    """Transfer amount"""

    reference: Required[str]
    """Unique client reference (alphanumeric, dots, underscores, hyphens)"""

    account_number: Annotated[str, PropertyInfo(alias="accountNumber")]
    """Bank account number (required if no transferRecipientId)"""

    bank_id: Annotated[str, PropertyInfo(alias="bankId")]
    """Bank ID (required if no transferRecipientId)"""

    country: Literal["zm", "ng"]
    """Country code"""

    narration: str
    """Transfer narration"""

    recipient_name: Annotated[str, PropertyInfo(alias="recipientName")]
    """Recipient name for the transaction record"""

    transfer_recipient_id: Annotated[str, PropertyInfo(alias="transferRecipientId")]
    """Transfer recipient UUID (use this OR accountNumber+bankId)"""

    wallet_id: Annotated[str, PropertyInfo(alias="walletId")]
    """Source wallet ID to debit (optional, uses main wallet if not specified)"""
