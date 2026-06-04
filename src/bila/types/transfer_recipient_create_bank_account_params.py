# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferRecipientCreateBankAccountParams"]


class TransferRecipientCreateBankAccountParams(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]
    """Bank account number"""

    bank_id: Required[Annotated[str, PropertyInfo(alias="bankId")]]
    """Bank ID"""

    account_name: Annotated[str, PropertyInfo(alias="accountName")]
    """Account holder name (optional, will be resolved)"""

    country: Literal["zm", "ng"]
    """Country code"""
