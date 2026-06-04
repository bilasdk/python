# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .bila_response import BilaResponse

__all__ = ["WebhookListEventsResponse"]


class WebhookListEventsResponse(BilaResponse):
    data: Optional[List[str]] = None
