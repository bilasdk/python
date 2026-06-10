#!/usr/bin/env -S uv run python
"""
Transfers examples

To demonstrate how to send payouts via
bank transfer and mobile money.
"""

import os

from usebila import Bila
from usebila.types import (
    TransferListParams,
    TransferListResponse,
    TransferRetrieveResponse,
    TransferInitiateBankTransferParams,
    TransferGetStatusByReferenceResponse,
    TransferInitiateBankTransferResponse,
    TransferInitiateMobileMoneyTransferParams,
    TransferInitiateMobileMoneyTransferResponse,
)

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)

TRANSFER_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
ACCOUNT_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
TRANSFER_RECIPIENT_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
WALLET_ID = "68f11209-451f-4a15-bfcd-d916eb8b09f4"
BANK_REFERENCE = "transfer-001"
MOBILE_REFERENCE = "mobile-transfer-001"


def main() -> None:
    # Retrieve transfer
    transfer: TransferRetrieveResponse = client.transfers.retrieve(TRANSFER_ID)
    print("retrieve:", transfer.to_json())

    # List transfers
    list_params: TransferListParams = {
        "account_id": ACCOUNT_ID,
        "start_date": "2024-01-01T00:00:00Z",
        "end_date": "2024-12-31T23:59:59Z",
        "page": 1,
        "per_page": 50,
        "status": "pending",
        "type": "bank-account",
    }

    transfers: TransferListResponse = client.transfers.list(**list_params)
    print("list:", transfers.to_json())

    # Get transfer status by reference
    status: TransferGetStatusByReferenceResponse = client.transfers.get_status_by_reference(BANK_REFERENCE)
    print("get_status_by_reference:", status.to_json())

    # Initiate bank transfer
    bank_params: TransferInitiateBankTransferParams = {
        "account_id": ACCOUNT_ID,
        "amount": 1000,
        "reference": BANK_REFERENCE,
        "account_number": "1234567890",
        "bank_id": "bank-001",
        "country": "zm",
        "narration": "Payment for services",
        "recipient_name": "Jane Doe",
        "transfer_recipient_id": TRANSFER_RECIPIENT_ID,
        "wallet_id": WALLET_ID,
    }

    bank_transfer: TransferInitiateBankTransferResponse = client.transfers.initiate_bank_transfer(**bank_params)
    print("initiate_bank_transfer:", bank_transfer.to_json())

    # Initiate mobile money transfer
    mobile_params: TransferInitiateMobileMoneyTransferParams = {
        "amount": 250,
        "country": "zm",
        "operator": "airtel",
        "phone": "0977433571",
        "reference": MOBILE_REFERENCE,
        "narration": "Mobile money payout",
        "recipient_name": "Jane Doe",
        "wallet_id": WALLET_ID,
    }

    mobile_transfer: TransferInitiateMobileMoneyTransferResponse = client.transfers.initiate_mobile_money_transfer(
        **mobile_params
    )
    print("initiate_mobile_money_transfer:", mobile_transfer.to_json())


if __name__ == "__main__":
    main()
