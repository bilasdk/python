# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountDetailsDto"]


class AccountDetailsDto(BaseModel):
    account_name: str = FieldInfo(alias="accountName")
    """Account holder name"""

    type: str
    """Account detail type"""

    till_number: Optional[str] = FieldInfo(alias="tillNumber", default=None)
    """Till number (for mobile money)"""
