# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BilaResponse"]


class BilaResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""
