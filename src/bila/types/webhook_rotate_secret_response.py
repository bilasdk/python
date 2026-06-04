# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bila_response import BilaResponse

__all__ = ["WebhookRotateSecretResponse", "WebhookRotateSecretResponseData"]


class WebhookRotateSecretResponseData(BaseModel):
    secret: str
    """New signing secret (64-character hex, shown once)"""


class WebhookRotateSecretResponse(BilaResponse):
    data: Optional[WebhookRotateSecretResponseData] = None
