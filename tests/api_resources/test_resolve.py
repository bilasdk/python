# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bila import Bila, AsyncBila
from bila.types import (
    ResolveBankAccountResponse,
    ResolveMobileMoneyResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResolve:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bank_account(self, client: Bila) -> None:
        resolve = client.resolve.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bank_account_with_all_params(self, client: Bila) -> None:
        resolve = client.resolve.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
            country="zm",
        )
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bank_account(self, client: Bila) -> None:
        response = client.resolve.with_raw_response.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = response.parse()
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bank_account(self, client: Bila) -> None:
        with client.resolve.with_streaming_response.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = response.parse()
            assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mobile_money(self, client: Bila) -> None:
        resolve = client.resolve.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )
        assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mobile_money(self, client: Bila) -> None:
        response = client.resolve.with_raw_response.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = response.parse()
        assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mobile_money(self, client: Bila) -> None:
        with client.resolve.with_streaming_response.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = response.parse()
            assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResolve:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bank_account(self, async_client: AsyncBila) -> None:
        resolve = await async_client.resolve.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bank_account_with_all_params(self, async_client: AsyncBila) -> None:
        resolve = await async_client.resolve.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
            country="zm",
        )
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bank_account(self, async_client: AsyncBila) -> None:
        response = await async_client.resolve.with_raw_response.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = await response.parse()
        assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bank_account(self, async_client: AsyncBila) -> None:
        async with async_client.resolve.with_streaming_response.bank_account(
            account_number="1234567890",
            bank_id="bank-001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = await response.parse()
            assert_matches_type(ResolveBankAccountResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mobile_money(self, async_client: AsyncBila) -> None:
        resolve = await async_client.resolve.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )
        assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mobile_money(self, async_client: AsyncBila) -> None:
        response = await async_client.resolve.with_raw_response.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resolve = await response.parse()
        assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mobile_money(self, async_client: AsyncBila) -> None:
        async with async_client.resolve.with_streaming_response.mobile_money(
            country="zm",
            operator="airtel",
            phone="0977433571",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resolve = await response.parse()
            assert_matches_type(ResolveMobileMoneyResponse, resolve, path=["response"])

        assert cast(Any, response.is_closed) is True
