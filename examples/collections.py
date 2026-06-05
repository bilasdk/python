#!/usr/bin/env -S uv run python
"""
Collections examples

To demonstrate how to collect payments
via mobile money.
"""

import os

from usebila import Bila
from usebila.types import (
    CollectionGetStatusByReferenceResponse,
    CollectionInitiateMobileMoneyCollectionResponse,
    CollectionListParams,
    CollectionListResponse,
    CollectionRetrieveResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

COLLECTION_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
WALLET_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
REFERENCE = "collection-001"


def main() -> None:
    # Retrieve collection
    collection: CollectionRetrieveResponse = client.collections.retrieve(COLLECTION_ID)
    print("retrieve:", collection.to_json())

    # List collections
    list_params: CollectionListParams = {
        "account_id": WALLET_ID,
        "start_date": "2024-01-01T00:00:00Z",
        "end_date": "2024-12-31T23:59:59Z",
        "page": 1,
        "per_page": 50,
        "status": "pending",
    }

    collections: CollectionListResponse = client.collections.list(**list_params)
    print("list:", collections.to_json())

    # Get collection status by reference
    status: CollectionGetStatusByReferenceResponse = client.collections.get_status_by_reference(REFERENCE)
    print("get_status_by_reference:", status.to_json())

    # Initiate mobile money collection
    initiated: CollectionInitiateMobileMoneyCollectionResponse = client.collections.initiate_mobile_money_collection(
        amount=100.5,
        country="zm",
        operator="airtel",
        phone="0977433571",
        reference=REFERENCE,
        wallet_id=WALLET_ID,
        bearer="customer",
        customer_name="John Doe",
        narration="Payment for subscription",
    )
    print("initiate_mobile_money_collection:", initiated.to_json())


if __name__ == "__main__":
    main()
