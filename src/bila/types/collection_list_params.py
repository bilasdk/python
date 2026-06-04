# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """Filter by account ID"""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Filter by end date (ISO 8601)"""

    page: float
    """Page number (default: 1)"""

    per_page: Annotated[float, PropertyInfo(alias="perPage")]
    """Items per page (default: 50)"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Filter by start date (ISO 8601)"""

    status: Literal["pending", "successful", "failed", "otp-required", "pay-offline"]
    """Filter by collection status"""
