# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookRotateSecretResponse", "Data"]


class Data(BaseModel):
    secret: str
    """New signing secret (64-character hex, shown once)"""


class WebhookRotateSecretResponse(BaseModel):
    message: str
    """Response message"""

    status: bool
    """Request success status"""

    data: Optional[Data] = None
