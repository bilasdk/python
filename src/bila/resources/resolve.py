# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import resolve_bank_account_params, resolve_mobile_money_params
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
from ..types.resolve_bank_account_response import ResolveBankAccountResponse
from ..types.resolve_mobile_money_response import ResolveMobileMoneyResponse

__all__ = ["ResolveResource", "AsyncResolveResource"]


class ResolveResource(SyncAPIResource):
    """Account resolution/verification endpoints"""

    @cached_property
    def with_raw_response(self) -> ResolveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bila-python#accessing-raw-response-data-eg-headers
        """
        return ResolveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResolveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bila-python#with_streaming_response
        """
        return ResolveResourceWithStreamingResponse(self)

    def bank_account(
        self,
        *,
        account_number: str,
        bank_id: str,
        country: Literal["zm", "ng"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolveBankAccountResponse:
        """
        Verify and retrieve bank account holder details

        Args:
          account_number: Bank account number

          bank_id: Bank ID

          country: Country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/resolve/bank-account",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "country": country,
                },
                resolve_bank_account_params.ResolveBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveBankAccountResponse,
        )

    def mobile_money(
        self,
        *,
        country: Literal["zm", "ng"],
        operator: Literal["airtel", "mtn", "zamtel", "vodacom"],
        phone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolveMobileMoneyResponse:
        """
        Verify and retrieve mobile money account holder details

        Args:
          country: Country code

          operator: Mobile money operator

          phone: Mobile phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/resolve/mobile-money",
            body=maybe_transform(
                {
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                },
                resolve_mobile_money_params.ResolveMobileMoneyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveMobileMoneyResponse,
        )


class AsyncResolveResource(AsyncAPIResource):
    """Account resolution/verification endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncResolveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bila-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResolveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResolveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bila-python#with_streaming_response
        """
        return AsyncResolveResourceWithStreamingResponse(self)

    async def bank_account(
        self,
        *,
        account_number: str,
        bank_id: str,
        country: Literal["zm", "ng"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolveBankAccountResponse:
        """
        Verify and retrieve bank account holder details

        Args:
          account_number: Bank account number

          bank_id: Bank ID

          country: Country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/resolve/bank-account",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "country": country,
                },
                resolve_bank_account_params.ResolveBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveBankAccountResponse,
        )

    async def mobile_money(
        self,
        *,
        country: Literal["zm", "ng"],
        operator: Literal["airtel", "mtn", "zamtel", "vodacom"],
        phone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResolveMobileMoneyResponse:
        """
        Verify and retrieve mobile money account holder details

        Args:
          country: Country code

          operator: Mobile money operator

          phone: Mobile phone number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/resolve/mobile-money",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                },
                resolve_mobile_money_params.ResolveMobileMoneyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResolveMobileMoneyResponse,
        )


class ResolveResourceWithRawResponse:
    def __init__(self, resolve: ResolveResource) -> None:
        self._resolve = resolve

        self.bank_account = to_raw_response_wrapper(
            resolve.bank_account,
        )
        self.mobile_money = to_raw_response_wrapper(
            resolve.mobile_money,
        )


class AsyncResolveResourceWithRawResponse:
    def __init__(self, resolve: AsyncResolveResource) -> None:
        self._resolve = resolve

        self.bank_account = async_to_raw_response_wrapper(
            resolve.bank_account,
        )
        self.mobile_money = async_to_raw_response_wrapper(
            resolve.mobile_money,
        )


class ResolveResourceWithStreamingResponse:
    def __init__(self, resolve: ResolveResource) -> None:
        self._resolve = resolve

        self.bank_account = to_streamed_response_wrapper(
            resolve.bank_account,
        )
        self.mobile_money = to_streamed_response_wrapper(
            resolve.mobile_money,
        )


class AsyncResolveResourceWithStreamingResponse:
    def __init__(self, resolve: AsyncResolveResource) -> None:
        self._resolve = resolve

        self.bank_account = async_to_streamed_response_wrapper(
            resolve.bank_account,
        )
        self.mobile_money = async_to_streamed_response_wrapper(
            resolve.mobile_money,
        )
