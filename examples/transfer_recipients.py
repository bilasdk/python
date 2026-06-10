#!/usr/bin/env -S uv run python
"""
Transfer recipients examples

To demonstrate how to manage payout recipients
for bank accounts and mobile money.
"""

import os

from usebila import Bila
from usebila.types import (
    TransferRecipientListParams,
    TransferRecipientListResponse,
    TransferRecipientRetrieveResponse,
    TransferRecipientCreateBankAccountParams,
    TransferRecipientCreateMobileMoneyParams,
    TransferRecipientCreateBankAccountResponse,
    TransferRecipientCreateMobileMoneyResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

RECIPIENT_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"


def main() -> None:
    # Retrieve transfer recipient
    recipient: TransferRecipientRetrieveResponse = client.transfer_recipients.retrieve(RECIPIENT_ID)
    print("retrieve:", recipient.to_json())

    # List transfer recipients
    list_params: TransferRecipientListParams = {
        "page": 1,
        "per_page": 50,
        "type": "bank-account",
    }

    recipients: TransferRecipientListResponse = client.transfer_recipients.list(**list_params)
    print("list:", recipients.to_json())

    # Create bank account recipient
    bank_params: TransferRecipientCreateBankAccountParams = {
        "account_number": "1234567890",
        "bank_id": "bank-001",
        "account_name": "John Doe",
        "country": "zm",
    }

    bank_recipient: TransferRecipientCreateBankAccountResponse = client.transfer_recipients.create_bank_account(
        **bank_params
    )
    print("create_bank_account:", bank_recipient.to_json())

    # Create mobile money recipient
    mobile_params: TransferRecipientCreateMobileMoneyParams = {
        "country": "zm",
        "operator": "airtel",
        "phone": "0977433571",
        "account_name": "John Doe",
    }

    mobile_recipient: TransferRecipientCreateMobileMoneyResponse = client.transfer_recipients.create_mobile_money(
        **mobile_params
    )
    print("create_mobile_money:", mobile_recipient.to_json())


if __name__ == "__main__":
    main()
