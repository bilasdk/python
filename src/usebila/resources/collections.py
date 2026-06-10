# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import collection_list_params, collection_initiate_mobile_money_collection_params
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
from ..types.collection_list_response import CollectionListResponse
from ..types.collection_retrieve_response import CollectionRetrieveResponse
from ..types.collection_get_status_by_reference_response import CollectionGetStatusByReferenceResponse
from ..types.collection_initiate_mobile_money_collection_response import CollectionInitiateMobileMoneyCollectionResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    """Payment collection operation endpoints"""

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

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
    ) -> CollectionRetrieveResponse:
        """
        Retrieve a single collection by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/bila/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        end_date: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["pending", "successful", "failed", "otp-required", "pay-offline"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        Retrieve a paginated list of payment collections for the authenticated merchant

        Args:
          account_id: Filter by account ID

          end_date: Filter by end date (ISO 8601)

          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          start_date: Filter by start date (ISO 8601)

          status: Filter by collection status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/bila/collections",
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
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionGetStatusByReferenceResponse:
        """
        Retrieve collection status by client reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference:
            raise ValueError(f"Expected a non-empty value for `reference` but received {reference!r}")
        return self._get(
            path_template("/api/v1/bila/collections/status/{reference}", reference=reference),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetStatusByReferenceResponse,
        )

    def initiate_mobile_money_collection(
        self,
        *,
        amount: float,
        country: Literal["zm"],
        operator: Literal["airtel", "mtn", "zamtel"],
        phone: str,
        reference: str,
        wallet_id: str,
        bearer: Literal["merchant", "customer"] | Omit = omit,
        customer_name: str | Omit = omit,
        narration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionInitiateMobileMoneyCollectionResponse:
        """Initiate a payment collection from a mobile money account.

        Creates a transaction
        record in your dashboard.

        Args:
          amount: Collection amount

          country: Country code

          operator: Mobile money operator

          phone: Customer phone number

          reference: Unique client reference

          wallet_id: Target wallet ID to credit

          bearer: Who bears the transaction fee

          customer_name: Customer name for the transaction record

          narration: Collection narration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/collections/mobile-money",
            body=maybe_transform(
                {
                    "amount": amount,
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "reference": reference,
                    "wallet_id": wallet_id,
                    "bearer": bearer,
                    "customer_name": customer_name,
                    "narration": narration,
                },
                collection_initiate_mobile_money_collection_params.CollectionInitiateMobileMoneyCollectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionInitiateMobileMoneyCollectionResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    """Payment collection operation endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bilasdk/python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bilasdk/python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

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
    ) -> CollectionRetrieveResponse:
        """
        Retrieve a single collection by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/bila/collections/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        end_date: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["pending", "successful", "failed", "otp-required", "pay-offline"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        Retrieve a paginated list of payment collections for the authenticated merchant

        Args:
          account_id: Filter by account ID

          end_date: Filter by end date (ISO 8601)

          page: Page number (default: 1)

          per_page: Items per page (default: 50)

          start_date: Filter by start date (ISO 8601)

          status: Filter by collection status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/bila/collections",
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
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionGetStatusByReferenceResponse:
        """
        Retrieve collection status by client reference

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference:
            raise ValueError(f"Expected a non-empty value for `reference` but received {reference!r}")
        return await self._get(
            path_template("/api/v1/bila/collections/status/{reference}", reference=reference),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetStatusByReferenceResponse,
        )

    async def initiate_mobile_money_collection(
        self,
        *,
        amount: float,
        country: Literal["zm"],
        operator: Literal["airtel", "mtn", "zamtel"],
        phone: str,
        reference: str,
        wallet_id: str,
        bearer: Literal["merchant", "customer"] | Omit = omit,
        customer_name: str | Omit = omit,
        narration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionInitiateMobileMoneyCollectionResponse:
        """Initiate a payment collection from a mobile money account.

        Creates a transaction
        record in your dashboard.

        Args:
          amount: Collection amount

          country: Country code

          operator: Mobile money operator

          phone: Customer phone number

          reference: Unique client reference

          wallet_id: Target wallet ID to credit

          bearer: Who bears the transaction fee

          customer_name: Customer name for the transaction record

          narration: Collection narration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/collections/mobile-money",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "country": country,
                    "operator": operator,
                    "phone": phone,
                    "reference": reference,
                    "wallet_id": wallet_id,
                    "bearer": bearer,
                    "customer_name": customer_name,
                    "narration": narration,
                },
                collection_initiate_mobile_money_collection_params.CollectionInitiateMobileMoneyCollectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionInitiateMobileMoneyCollectionResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.get_status_by_reference = to_raw_response_wrapper(
            collections.get_status_by_reference,
        )
        self.initiate_mobile_money_collection = to_raw_response_wrapper(
            collections.initiate_mobile_money_collection,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.get_status_by_reference = async_to_raw_response_wrapper(
            collections.get_status_by_reference,
        )
        self.initiate_mobile_money_collection = async_to_raw_response_wrapper(
            collections.initiate_mobile_money_collection,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.get_status_by_reference = to_streamed_response_wrapper(
            collections.get_status_by_reference,
        )
        self.initiate_mobile_money_collection = to_streamed_response_wrapper(
            collections.initiate_mobile_money_collection,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.get_status_by_reference = async_to_streamed_response_wrapper(
            collections.get_status_by_reference,
        )
        self.initiate_mobile_money_collection = async_to_streamed_response_wrapper(
            collections.initiate_mobile_money_collection,
        )
