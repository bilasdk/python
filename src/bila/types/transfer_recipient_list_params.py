# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransferRecipientListParams"]


class TransferRecipientListParams(TypedDict, total=False):
    page: float
    """Page number (default: 1)"""

    per_page: Annotated[float, PropertyInfo(alias="perPage")]
    """Items per page (default: 50)"""

    type: Literal["bank-account", "mobile-money"]
    """Filter by recipient type"""
