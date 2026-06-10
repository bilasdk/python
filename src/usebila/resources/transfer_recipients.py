# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    transfer_recipient_list_params,
    transfer_recipient_create_bank_account_params,
    transfer_recipient_create_mobile_money_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.transfer_recipient_list_response import TransferRecipientListResponse
from ..types.transfer_recipient_retrieve_response import TransferRecipientRetrieveResponse
from ..types.transfer_recipient_create_bank_account_response import TransferRecipientCreateBankAccountResponse
from ..types.transfer_recipient_create_mobile_money_response import TransferRecipientCreateMobileMoneyResponse

__all__ = ["TransferRecipientsResource", "AsyncTransferRecipientsResource"]


class TransferRecipientsResource(SyncAPIResource):
    """Transfer recipient management endpoints"""

    @cached_property
    def with_raw_response(self) -> TransferRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return TransferRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransferRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return TransferRecipientsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientRetrieveResponse:
        """
        Retrieve a single transfer recipient by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/bila/transfer-recipients/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientRetrieveResponse,
        )

    def list(
        self,
        *,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        type: Literal["bank-account", "mobile-money"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientListResponse:
        """
        Retrieve a paginated list of saved transfer recipients

        Args:
          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          type: Filter by recipient type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/bila/transfer-recipients",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    transfer_recipient_list_params.TransferRecipientListParams,
                ),
            ),
            cast_to=TransferRecipientListResponse,
        )

    def create_bank_account(
        self,
        *,
        account_number: str,
        bank_id: str,
        account_name: str | Omit = omit,
        country: Literal["zm"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientCreateBankAccountResponse:
        """
        Create a new bank account transfer recipient

        Args:
          account_number: Bank account number

          bank_id: Bank ID

          account_name: Account holder name (optional, will be resolved)

          country: Country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/transfer-recipients/bank-account",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "account_name": account_name,
                    "country": country,
                },
                transfer_recipient_create_bank_account_params.TransferRecipientCreateBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientCreateBankAccountResponse,
        )

    def create_mobile_money(
        self,
        *,
        country: Literal["zm"],
        operator: Literal["airtel", "mtn", "zamtel"],
        phone: str,
        account_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientCreateMobileMoneyResponse:
        """
        Create a new mobile money transfer recipient

        Args:
          country: Country code

          operator: Mobile money operator

          phone: Mobile phone number

          account_name: Account holder name (optional, will be resolved)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/transfer-recipients/mobile-money",
            body=maybe_transform(
                {
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "account_name": account_name,
                },
                transfer_recipient_create_mobile_money_params.TransferRecipientCreateMobileMoneyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientCreateMobileMoneyResponse,
        )


class AsyncTransferRecipientsResource(AsyncAPIResource):
    """Transfer recipient management endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncTransferRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransferRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransferRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return AsyncTransferRecipientsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientRetrieveResponse:
        """
        Retrieve a single transfer recipient by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/bila/transfer-recipients/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        type: Literal["bank-account", "mobile-money"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientListResponse:
        """
        Retrieve a paginated list of saved transfer recipients

        Args:
          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          type: Filter by recipient type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/bila/transfer-recipients",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    transfer_recipient_list_params.TransferRecipientListParams,
                ),
            ),
            cast_to=TransferRecipientListResponse,
        )

    async def create_bank_account(
        self,
        *,
        account_number: str,
        bank_id: str,
        account_name: str | Omit = omit,
        country: Literal["zm"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientCreateBankAccountResponse:
        """
        Create a new bank account transfer recipient

        Args:
          account_number: Bank account number

          bank_id: Bank ID

          account_name: Account holder name (optional, will be resolved)

          country: Country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/transfer-recipients/bank-account",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "account_name": account_name,
                    "country": country,
                },
                transfer_recipient_create_bank_account_params.TransferRecipientCreateBankAccountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientCreateBankAccountResponse,
        )

    async def create_mobile_money(
        self,
        *,
        country: Literal["zm"],
        operator: Literal["airtel", "mtn", "zamtel"],
        phone: str,
        account_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferRecipientCreateMobileMoneyResponse:
        """
        Create a new mobile money transfer recipient

        Args:
          country: Country code

          operator: Mobile money operator

          phone: Mobile phone number

          account_name: Account holder name (optional, will be resolved)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/transfer-recipients/mobile-money",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "account_name": account_name,
                },
                transfer_recipient_create_mobile_money_params.TransferRecipientCreateMobileMoneyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRecipientCreateMobileMoneyResponse,
        )


class TransferRecipientsResourceWithRawResponse:
    def __init__(self, transfer_recipients: TransferRecipientsResource) -> None:
        self._transfer_recipients = transfer_recipients

        self.retrieve = to_raw_response_wrapper(
            transfer_recipients.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transfer_recipients.list,
        )
        self.create_bank_account = to_raw_response_wrapper(
            transfer_recipients.create_bank_account,
        )
        self.create_mobile_money = to_raw_response_wrapper(
            transfer_recipients.create_mobile_money,
        )


class AsyncTransferRecipientsResourceWithRawResponse:
    def __init__(self, transfer_recipients: AsyncTransferRecipientsResource) -> None:
        self._transfer_recipients = transfer_recipients

        self.retrieve = async_to_raw_response_wrapper(
            transfer_recipients.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transfer_recipients.list,
        )
        self.create_bank_account = async_to_raw_response_wrapper(
            transfer_recipients.create_bank_account,
        )
        self.create_mobile_money = async_to_raw_response_wrapper(
            transfer_recipients.create_mobile_money,
        )


class TransferRecipientsResourceWithStreamingResponse:
    def __init__(self, transfer_recipients: TransferRecipientsResource) -> None:
        self._transfer_recipients = transfer_recipients

        self.retrieve = to_streamed_response_wrapper(
            transfer_recipients.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transfer_recipients.list,
        )
        self.create_bank_account = to_streamed_response_wrapper(
            transfer_recipients.create_bank_account,
        )
        self.create_mobile_money = to_streamed_response_wrapper(
            transfer_recipients.create_mobile_money,
        )


class AsyncTransferRecipientsResourceWithStreamingResponse:
    def __init__(self, transfer_recipients: AsyncTransferRecipientsResource) -> None:
        self._transfer_recipients = transfer_recipients

        self.retrieve = async_to_streamed_response_wrapper(
            transfer_recipients.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transfer_recipients.list,
        )
        self.create_bank_account = async_to_streamed_response_wrapper(
            transfer_recipients.create_bank_account,
        )
        self.create_mobile_money = async_to_streamed_response_wrapper(
            transfer_recipients.create_mobile_money,
        )
