#!/usr/bin/env -S uv run python
"""
Banks examples

To demonstrate how to list supported banks
and financial institutions.
"""

import os

from usebila import Bila
from usebila.types import BankListParams, BankListResponse

client = Bila(
    api_key=os.environ.get("BILA_API_KEY", "sk_test_your_api_key_here"),
    environment="sandbox",
)


def main() -> None:
    list_params: BankListParams = {
        "country": "zm",
    }

    banks: BankListResponse = client.banks.list(**list_params)
    print("list:", banks.to_json())


if __name__ == "__main__":
    main()
