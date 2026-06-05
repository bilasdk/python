#!/usr/bin/env -S uv run python
"""
Resolve examples

To demonstrate how to verify bank account
and mobile money account details.
"""

import os

from usebila import Bila
from usebila.types import (
    ResolveBankAccountParams,
    ResolveBankAccountResponse,
    ResolveMobileMoneyParams,
    ResolveMobileMoneyResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)


def main() -> None:
    # Resolve bank account
    resolve_bank_params: ResolveBankAccountParams = {
        "account_number": "1234567890",
        "bank_id": "bank-001",
        "country": "zm",
    }

    bank_account: ResolveBankAccountResponse = client.resolve.bank_account(**resolve_bank_params)
    print("bank_account:", bank_account.to_json())

    # Resolve mobile money
    resolve_mobile_params: ResolveMobileMoneyParams = {
        "country": "zm",
        "operator": "airtel",
        "phone": "0977433571",
    }

    mobile_money: ResolveMobileMoneyResponse = client.resolve.mobile_money(**resolve_mobile_params)
    print("mobile_money:", mobile_money.to_json())


if __name__ == "__main__":
    main()
