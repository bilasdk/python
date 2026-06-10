# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from usebila import Bila, AsyncBila
from tests.utils import assert_matches_type
from usebila.types import BankListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBanks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bila) -> None:
        bank = client.banks.list()
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bila) -> None:
        bank = client.banks.list(
            country="zm",
        )
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bila) -> None:
        response = client.banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank = response.parse()
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bila) -> None:
        with client.banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank = response.parse()
            assert_matches_type(BankListResponse, bank, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBanks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBila) -> None:
        bank = await async_client.banks.list()
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBila) -> None:
        bank = await async_client.banks.list(
            country="zm",
        )
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBila) -> None:
        response = await async_client.banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bank = await response.parse()
        assert_matches_type(BankListResponse, bank, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBila) -> None:
        async with async_client.banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bank = await response.parse()
            assert_matches_type(BankListResponse, bank, path=["response"])

        assert cast(Any, response.is_closed) is True
