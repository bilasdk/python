#!/usr/bin/env -S uv run python
"""
Accounts examples

To demonstrate how to retrieve accounts,
list accounts, and check balances.
"""

import os

from usebila import Bila
from usebila.types import (
    AccountGetBalanceResponse,
    AccountListParams,
    AccountListResponse,
    AccountRetrieveResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

ACCOUNT_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"


def main() -> None:
    # Retrieve account
    account: AccountRetrieveResponse = client.accounts.retrieve(ACCOUNT_ID)
    print("retrieve:", account.to_json())

    # List accounts
    list_params: AccountListParams = {
        "page": 1,
        "per_page": 50,
    }

    accounts: AccountListResponse = client.accounts.list(**list_params)
    print("list:", accounts.to_json())

    # Get account balance
    balance: AccountGetBalanceResponse = client.accounts.get_balance(ACCOUNT_ID)
    print("get_balance:", balance.to_json())


if __name__ == "__main__":
    main()
