# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    transfer_list_params,
    transfer_initiate_bank_transfer_params,
    transfer_initiate_mobile_money_transfer_params,
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
from ..types.transfer_list_response import TransferListResponse
from ..types.transfer_retrieve_response import TransferRetrieveResponse
from ..types.transfer_initiate_bank_transfer_response import TransferInitiateBankTransferResponse
from ..types.transfer_get_status_by_reference_response import TransferGetStatusByReferenceResponse
from ..types.transfer_initiate_mobile_money_transfer_response import TransferInitiateMobileMoneyTransferResponse

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    """Payout/transfer operation endpoints"""

    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

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
    ) -> TransferRetrieveResponse:
        """
        Retrieve a single transfer by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/bila/transfers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        end_date: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["pending", "successful", "failed"] | Omit = omit,
        type: Literal["bank-account", "mobile-money"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferListResponse:
        """
        Retrieve a paginated list of transfers/payouts for the authenticated merchant

        Args:
          account_id: Filter by account ID

          end_date: Filter by end date (ISO 8601)

          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          start_date: Filter by start date (ISO 8601)

          status: Filter by transfer status

          type: Filter by transfer type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/bila/transfers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "end_date": end_date,
                        "page": page,
                        "per_page": per_page,
                        "start_date": start_date,
                        "status": status,
                        "type": type,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=TransferListResponse,
        )

    def get_status_by_reference(
        self,
        reference: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferGetStatusByReferenceResponse:
        """
        Retrieve transfer status by client reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference:
            raise ValueError(f"Expected a non-empty value for `reference` but received {reference!r}")
        return self._get(
            path_template("/api/v1/bila/transfers/status/{reference}", reference=reference),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferGetStatusByReferenceResponse,
        )

    def initiate_bank_transfer(
        self,
        *,
        account_id: str,
        amount: float,
        reference: str,
        account_number: str | Omit = omit,
        bank_id: str | Omit = omit,
        country: Literal["zm", "ng"] | Omit = omit,
        narration: str | Omit = omit,
        recipient_name: str | Omit = omit,
        transfer_recipient_id: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferInitiateBankTransferResponse:
        """Initiate a transfer to a bank account.

        Creates a transaction record in your
        dashboard.

        Args:
          account_id: Source account UUID

          amount: Transfer amount

          reference: Unique client reference (alphanumeric, dots, underscores, hyphens)

          account_number: Bank account number (required if no transferRecipientId)

          bank_id: Bank ID (required if no transferRecipientId)

          country: Country code

          narration: Transfer narration

          recipient_name: Recipient name for the transaction record

          transfer_recipient_id: Transfer recipient UUID (use this OR accountNumber+bankId)

          wallet_id: Source wallet ID to debit (optional, uses main wallet if not specified)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/transfers/bank-account",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "reference": reference,
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "country": country,
                    "narration": narration,
                    "recipient_name": recipient_name,
                    "transfer_recipient_id": transfer_recipient_id,
                    "wallet_id": wallet_id,
                },
                transfer_initiate_bank_transfer_params.TransferInitiateBankTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferInitiateBankTransferResponse,
        )

    def initiate_mobile_money_transfer(
        self,
        *,
        amount: float,
        country: Literal["zm", "ng"],
        operator: Literal["airtel", "mtn", "zamtel", "vodacom"],
        phone: str,
        reference: str,
        narration: str | Omit = omit,
        recipient_name: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferInitiateMobileMoneyTransferResponse:
        """Initiate a transfer to a mobile money account.

        Creates a transaction record in
        your dashboard.

        Args:
          amount: Transfer amount

          country: Country code

          operator: Mobile money operator

          phone: Recipient phone number

          reference: Unique client reference

          narration: Transfer narration

          recipient_name: Recipient name for the transaction record

          wallet_id: Source wallet ID to debit (defaults to main wallet if omitted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/transfers/mobile-money",
            body=maybe_transform(
                {
                    "amount": amount,
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "reference": reference,
                    "narration": narration,
                    "recipient_name": recipient_name,
                    "wallet_id": wallet_id,
                },
                transfer_initiate_mobile_money_transfer_params.TransferInitiateMobileMoneyTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferInitiateMobileMoneyTransferResponse,
        )


class AsyncTransfersResource(AsyncAPIResource):
    """Payout/transfer operation endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

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
    ) -> TransferRetrieveResponse:
        """
        Retrieve a single transfer by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/bila/transfers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        end_date: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["pending", "successful", "failed"] | Omit = omit,
        type: Literal["bank-account", "mobile-money"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferListResponse:
        """
        Retrieve a paginated list of transfers/payouts for the authenticated merchant

        Args:
          account_id: Filter by account ID

          end_date: Filter by end date (ISO 8601)

          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          start_date: Filter by start date (ISO 8601)

          status: Filter by transfer status

          type: Filter by transfer type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/bila/transfers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "end_date": end_date,
                        "page": page,
                        "per_page": per_page,
                        "start_date": start_date,
                        "status": status,
                        "type": type,
                    },
                    transfer_list_params.TransferListParams,
                ),
            ),
            cast_to=TransferListResponse,
        )

    async def get_status_by_reference(
        self,
        reference: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferGetStatusByReferenceResponse:
        """
        Retrieve transfer status by client reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference:
            raise ValueError(f"Expected a non-empty value for `reference` but received {reference!r}")
        return await self._get(
            path_template("/api/v1/bila/transfers/status/{reference}", reference=reference),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferGetStatusByReferenceResponse,
        )

    async def initiate_bank_transfer(
        self,
        *,
        account_id: str,
        amount: float,
        reference: str,
        account_number: str | Omit = omit,
        bank_id: str | Omit = omit,
        country: Literal["zm", "ng"] | Omit = omit,
        narration: str | Omit = omit,
        recipient_name: str | Omit = omit,
        transfer_recipient_id: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferInitiateBankTransferResponse:
        """Initiate a transfer to a bank account.

        Creates a transaction record in your
        dashboard.

        Args:
          account_id: Source account UUID

          amount: Transfer amount

          reference: Unique client reference (alphanumeric, dots, underscores, hyphens)

          account_number: Bank account number (required if no transferRecipientId)

          bank_id: Bank ID (required if no transferRecipientId)

          country: Country code

          narration: Transfer narration

          recipient_name: Recipient name for the transaction record

          transfer_recipient_id: Transfer recipient UUID (use this OR accountNumber+bankId)

          wallet_id: Source wallet ID to debit (optional, uses main wallet if not specified)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/transfers/bank-account",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "amount": amount,
                    "reference": reference,
                    "account_number": account_number,
                    "bank_id": bank_id,
                    "country": country,
                    "narration": narration,
                    "recipient_name": recipient_name,
                    "transfer_recipient_id": transfer_recipient_id,
                    "wallet_id": wallet_id,
                },
                transfer_initiate_bank_transfer_params.TransferInitiateBankTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferInitiateBankTransferResponse,
        )

    async def initiate_mobile_money_transfer(
        self,
        *,
        amount: float,
        country: Literal["zm", "ng"],
        operator: Literal["airtel", "mtn", "zamtel", "vodacom"],
        phone: str,
        reference: str,
        narration: str | Omit = omit,
        recipient_name: str | Omit = omit,
        wallet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransferInitiateMobileMoneyTransferResponse:
        """Initiate a transfer to a mobile money account.

        Creates a transaction record in
        your dashboard.

        Args:
          amount: Transfer amount

          country: Country code

          operator: Mobile money operator

          phone: Recipient phone number

          reference: Unique client reference

          narration: Transfer narration

          recipient_name: Recipient name for the transaction record

          wallet_id: Source wallet ID to debit (defaults to main wallet if omitted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/transfers/mobile-money",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "reference": reference,
                    "narration": narration,
                    "recipient_name": recipient_name,
                    "wallet_id": wallet_id,
                },
                transfer_initiate_mobile_money_transfer_params.TransferInitiateMobileMoneyTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransferInitiateMobileMoneyTransferResponse,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.retrieve = to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transfers.list,
        )
        self.get_status_by_reference = to_raw_response_wrapper(
            transfers.get_status_by_reference,
        )
        self.initiate_bank_transfer = to_raw_response_wrapper(
            transfers.initiate_bank_transfer,
        )
        self.initiate_mobile_money_transfer = to_raw_response_wrapper(
            transfers.initiate_mobile_money_transfer,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.retrieve = async_to_raw_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transfers.list,
        )
        self.get_status_by_reference = async_to_raw_response_wrapper(
            transfers.get_status_by_reference,
        )
        self.initiate_bank_transfer = async_to_raw_response_wrapper(
            transfers.initiate_bank_transfer,
        )
        self.initiate_mobile_money_transfer = async_to_raw_response_wrapper(
            transfers.initiate_mobile_money_transfer,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.retrieve = to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transfers.list,
        )
        self.get_status_by_reference = to_streamed_response_wrapper(
            transfers.get_status_by_reference,
        )
        self.initiate_bank_transfer = to_streamed_response_wrapper(
            transfers.initiate_bank_transfer,
        )
        self.initiate_mobile_money_transfer = to_streamed_response_wrapper(
            transfers.initiate_mobile_money_transfer,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.retrieve = async_to_streamed_response_wrapper(
            transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transfers.list,
        )
        self.get_status_by_reference = async_to_streamed_response_wrapper(
            transfers.get_status_by_reference,
        )
        self.initiate_bank_transfer = async_to_streamed_response_wrapper(
            transfers.initiate_bank_transfer,
        )
        self.initiate_mobile_money_transfer = async_to_streamed_response_wrapper(
            transfers.initiate_mobile_money_transfer,
        )
