# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BilaCollectionCustomerDto"]


class BilaCollectionCustomerDto(BaseModel):
    name: str
    """Customer name"""

    operator: str
    """Mobile money operator"""

    phone: str
    """Customer phone number"""
