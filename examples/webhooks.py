#!/usr/bin/env -S uv run python
"""
Webhooks examples

To demonstrate how to configure webhooks
and manage delivery history.
"""

import os

from usebila import Bila
from usebila.types import (
    WebhookCreateParams,
    WebhookCreateResponse,
    WebhookDeactivateResponse,
    WebhookGetDeliveriesParams,
    WebhookGetDeliveriesResponse,
    WebhookListEventsResponse,
    WebhookListResponse,
    WebhookRotateSecretResponse,
    WebhookUpdateParams,
    WebhookUpdateResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

WEBHOOK_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"


def main() -> None:
    # Create webhook
    create_params: WebhookCreateParams = {
        "events": ["payment.completed", "withdrawal.completed", "transfer.completed"],
        "url": "https://example.com/webhooks",
    }

    created: WebhookCreateResponse = client.webhooks.create(**create_params)
    print("create:", created.to_json())

    # Update webhook
    update_params: WebhookUpdateParams = {
        "events": ["payment.completed", "collection.completed", "transfer.failed"],
        "url": "https://example.com/webhooks/v2",
        "is_active": True,
    }

    updated: WebhookUpdateResponse = client.webhooks.update(WEBHOOK_ID, **update_params)
    print("update:", updated.to_json())

    # List webhooks
    webhooks: WebhookListResponse = client.webhooks.list()
    print("list:", webhooks.to_json())

    # Get webhook deliveries
    deliveries_params: WebhookGetDeliveriesParams = {
        "start_date": "2026-04-01T00:00:00.000Z",
        "end_date": "2026-04-30T23:59:59.999Z",
        "event_type": "payment.completed",
        "page": 1,
        "per_page": 20,
        "status": "DELIVERED",
    }

    deliveries: WebhookGetDeliveriesResponse = client.webhooks.get_deliveries(WEBHOOK_ID, **deliveries_params)
    print("get_deliveries:", deliveries.to_json())

    # List webhook events
    events: WebhookListEventsResponse = client.webhooks.list_events()
    print("list_events:", events.to_json())

    # Rotate webhook secret
    rotated: WebhookRotateSecretResponse = client.webhooks.rotate_secret(WEBHOOK_ID)
    print("rotate_secret:", rotated.to_json())

    # Deactivate webhook
    deactivated: WebhookDeactivateResponse = client.webhooks.deactivate(WEBHOOK_ID)
    print("deactivate:", deactivated.to_json())


if __name__ == "__main__":
    main()
