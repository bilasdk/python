#!/usr/bin/env -S uv run python
"""
Transactions examples

To demonstrate how to retrieve and list
transaction history.
"""

import os

from usebila import Bila
from usebila.types import (
    TransactionListParams,
    TransactionListResponse,
    TransactionRetrieveResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

TRANSACTION_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
ACCOUNT_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"


def main() -> None:
    # Retrieve transaction
    transaction: TransactionRetrieveResponse = client.transactions.retrieve(TRANSACTION_ID)
    print("retrieve:", transaction.to_json())

    # List transactions
    list_params: TransactionListParams = {
        "account_id": ACCOUNT_ID,
        "start_date": "2024-01-01T00:00:00Z",
        "end_date": "2024-12-31T23:59:59Z",
        "page": 1,
        "per_page": 50,
        "type": "credit",
    }

    transactions: TransactionListResponse = client.transactions.list(**list_params)
    print("list:", transactions.to_json())


if __name__ == "__main__":
    main()
