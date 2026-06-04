# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bank_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.bank_list_response import BankListResponse

__all__ = ["BanksResource", "AsyncBanksResource"]


class BanksResource(SyncAPIResource):
    """Bank reference data endpoints"""

    @cached_property
    def with_raw_response(self) -> BanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return BanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return BanksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        country: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankListResponse:
        """
        Retrieve a list of all supported banks and financial institutions

        Args:
          country: Filter banks by country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/bila/banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"country": country}, bank_list_params.BankListParams),
            ),
            cast_to=BankListResponse,
        )


class AsyncBanksResource(AsyncAPIResource):
    """Bank reference data endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncBanksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return AsyncBanksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBanksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return AsyncBanksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        country: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankListResponse:
        """
        Retrieve a list of all supported banks and financial institutions

        Args:
          country: Filter banks by country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/bila/banks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"country": country}, bank_list_params.BankListParams),
            ),
            cast_to=BankListResponse,
        )


class BanksResourceWithRawResponse:
    def __init__(self, banks: BanksResource) -> None:
        self._banks = banks

        self.list = to_raw_response_wrapper(
            banks.list,
        )


class AsyncBanksResourceWithRawResponse:
    def __init__(self, banks: AsyncBanksResource) -> None:
        self._banks = banks

        self.list = async_to_raw_response_wrapper(
            banks.list,
        )


class BanksResourceWithStreamingResponse:
    def __init__(self, banks: BanksResource) -> None:
        self._banks = banks

        self.list = to_streamed_response_wrapper(
            banks.list,
        )


class AsyncBanksResourceWithStreamingResponse:
    def __init__(self, banks: AsyncBanksResource) -> None:
        self._banks = banks

        self.list = async_to_streamed_response_wrapper(
            banks.list,
        )
