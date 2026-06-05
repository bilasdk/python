# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from usebila import Bila, AsyncBila
from tests.utils import assert_matches_type
from usebila.types import (
    TransferRecipientListResponse,
    TransferRecipientRetrieveResponse,
    TransferRecipientCreateBankAccountResponse,
    TransferRecipientCreateMobileMoneyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransferRecipients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bila) -> None:
        response = client.transfer_recipients.with_raw_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = response.parse()
        assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bila) -> None:
        with client.transfer_recipients.with_streaming_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = response.parse()
            assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transfer_recipients.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.list()
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.list(
            page=1,
            per_page=50,
            type="bank-account",
        )
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bila) -> None:
        response = client.transfer_recipients.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = response.parse()
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bila) -> None:
        with client.transfer_recipients.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = response.parse()
            assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_bank_account(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_bank_account_with_all_params(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
            account_name="John Doe",
            country="zm",
        )
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_bank_account(self, client: Bila) -> None:
        response = client.transfer_recipients.with_raw_response.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = response.parse()
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_bank_account(self, client: Bila) -> None:
        with client.transfer_recipients.with_streaming_response.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = response.parse()
            assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mobile_money(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mobile_money_with_all_params(self, client: Bila) -> None:
        transfer_recipient = client.transfer_recipients.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
            account_name="John Doe",
        )
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_mobile_money(self, client: Bila) -> None:
        response = client.transfer_recipients.with_raw_response.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = response.parse()
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_mobile_money(self, client: Bila) -> None:
        with client.transfer_recipients.with_streaming_response.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = response.parse()
            assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransferRecipients:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBila) -> None:
        response = await async_client.transfer_recipients.with_raw_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = await response.parse()
        assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBila) -> None:
        async with async_client.transfer_recipients.with_streaming_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = await response.parse()
            assert_matches_type(TransferRecipientRetrieveResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transfer_recipients.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.list()
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.list(
            page=1,
            per_page=50,
            type="bank-account",
        )
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBila) -> None:
        response = await async_client.transfer_recipients.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = await response.parse()
        assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBila) -> None:
        async with async_client.transfer_recipients.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = await response.parse()
            assert_matches_type(TransferRecipientListResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_bank_account(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_bank_account_with_all_params(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
            account_name="John Doe",
            country="zm",
        )
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_bank_account(self, async_client: AsyncBila) -> None:
        response = await async_client.transfer_recipients.with_raw_response.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = await response.parse()
        assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_bank_account(self, async_client: AsyncBila) -> None:
        async with async_client.transfer_recipients.with_streaming_response.create_bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = await response.parse()
            assert_matches_type(TransferRecipientCreateBankAccountResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mobile_money(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mobile_money_with_all_params(self, async_client: AsyncBila) -> None:
        transfer_recipient = await async_client.transfer_recipients.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
            account_name="John Doe",
        )
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_mobile_money(self, async_client: AsyncBila) -> None:
        response = await async_client.transfer_recipients.with_raw_response.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_recipient = await response.parse()
        assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_mobile_money(self, async_client: AsyncBila) -> None:
        async with async_client.transfer_recipients.with_streaming_response.create_mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_recipient = await response.parse()
            assert_matches_type(TransferRecipientCreateMobileMoneyResponse, transfer_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True
