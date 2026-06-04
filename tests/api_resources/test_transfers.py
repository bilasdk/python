# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bila import Bila, AsyncBila
from bila.types import (
    TransferListResponse,
    TransferRetrieveResponse,
    TransferGetStatusByReferenceResponse,
    TransferInitiateBankTransferResponse,
    TransferInitiateMobileMoneyTransferResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bila) -> None:
        transfer = client.transfers.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bila) -> None:
        response = client.transfers.with_raw_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bila) -> None:
        with client.transfers.with_streaming_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.transfers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bila) -> None:
        transfer = client.transfers.list()
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bila) -> None:
        transfer = client.transfers.list(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            end_date="2024-12-31T23:59:59Z",
            page=1,
            per_page=50,
            start_date="2024-01-01T00:00:00Z",
            status="pending",
            type="bank-account",
        )
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bila) -> None:
        response = client.transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bila) -> None:
        with client.transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferListResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_by_reference(self, client: Bila) -> None:
        transfer = client.transfers.get_status_by_reference(
            "transfer-001",
        )
        assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status_by_reference(self, client: Bila) -> None:
        response = client.transfers.with_raw_response.get_status_by_reference(
            "transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status_by_reference(self, client: Bila) -> None:
        with client.transfers.with_streaming_response.get_status_by_reference(
            "transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status_by_reference(self, client: Bila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reference` but received ''"):
            client.transfers.with_raw_response.get_status_by_reference(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_bank_transfer(self, client: Bila) -> None:
        transfer = client.transfers.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        )
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_bank_transfer_with_all_params(self, client: Bila) -> None:
        transfer = client.transfers.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
            account_number="1234567890",
            bank_id="bank-001",
            country="zm",
            narration="Payment for services",
            recipient_name="Jane Doe",
            transfer_recipient_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            wallet_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_bank_transfer(self, client: Bila) -> None:
        response = client.transfers.with_raw_response.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_bank_transfer(self, client: Bila) -> None:
        with client.transfers.with_streaming_response.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_mobile_money_transfer(self, client: Bila) -> None:
        transfer = client.transfers.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        )
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_mobile_money_transfer_with_all_params(self, client: Bila) -> None:
        transfer = client.transfers.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
            narration="Mobile money payout",
            recipient_name="Jane Doe",
            wallet_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_mobile_money_transfer(self, client: Bila) -> None:
        response = client.transfers.with_raw_response.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_mobile_money_transfer(self, client: Bila) -> None:
        with client.transfers.with_streaming_response.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBila) -> None:
        response = await async_client.transfers.with_raw_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBila) -> None:
        async with async_client.transfers.with_streaming_response.retrieve(
            "68f11209-451f-4a15-bfcd-d916eb8b09f4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferRetrieveResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.transfers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.list()
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.list(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            end_date="2024-12-31T23:59:59Z",
            page=1,
            per_page=50,
            start_date="2024-01-01T00:00:00Z",
            status="pending",
            type="bank-account",
        )
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBila) -> None:
        response = await async_client.transfers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferListResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBila) -> None:
        async with async_client.transfers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferListResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_by_reference(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.get_status_by_reference(
            "transfer-001",
        )
        assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status_by_reference(self, async_client: AsyncBila) -> None:
        response = await async_client.transfers.with_raw_response.get_status_by_reference(
            "transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status_by_reference(self, async_client: AsyncBila) -> None:
        async with async_client.transfers.with_streaming_response.get_status_by_reference(
            "transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferGetStatusByReferenceResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status_by_reference(self, async_client: AsyncBila) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reference` but received ''"):
            await async_client.transfers.with_raw_response.get_status_by_reference(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_bank_transfer(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        )
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_bank_transfer_with_all_params(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
            account_number="1234567890",
            bank_id="bank-001",
            country="zm",
            narration="Payment for services",
            recipient_name="Jane Doe",
            transfer_recipient_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            wallet_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_bank_transfer(self, async_client: AsyncBila) -> None:
        response = await async_client.transfers.with_raw_response.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_bank_transfer(self, async_client: AsyncBila) -> None:
        async with async_client.transfers.with_streaming_response.initiate_bank_transfer(
            account_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
            amount=1000,
            reference="transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferInitiateBankTransferResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_mobile_money_transfer(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        )
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_mobile_money_transfer_with_all_params(self, async_client: AsyncBila) -> None:
        transfer = await async_client.transfers.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
            narration="Mobile money payout",
            recipient_name="Jane Doe",
            wallet_id="68f11209-451f-4a15-bfcd-d916eb8b09f4",
        )
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_mobile_money_transfer(self, async_client: AsyncBila) -> None:
        response = await async_client.transfers.with_raw_response.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_mobile_money_transfer(self, async_client: AsyncBila) -> None:
        async with async_client.transfers.with_streaming_response.initiate_mobile_money_transfer(
            amount=250,
            country="zm",
            operator="airtel",
            phone="0977433571",
            reference="mobile-transfer-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert_matches_type(TransferInitiateMobileMoneyTransferResponse, transfer, path=["response"])

        assert cast(Any, response.is_closed) is True
