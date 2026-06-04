# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import webhook_create_params, webhook_update_params, webhook_get_deliveries_params
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
from ..types.bila_response import BilaResponse
from ..types.webhook_list_response import WebhookListResponse
from ..types.webhook_create_response import WebhookCreateResponse
from ..types.webhook_update_response import WebhookUpdateResponse
from ..types.webhook_list_events_response import WebhookListEventsResponse
from ..types.webhook_rotate_secret_response import WebhookRotateSecretResponse
from ..types.webhook_get_deliveries_response import WebhookGetDeliveriesResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    """Webhook configuration and delivery history"""

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bila-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bila-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        events: List[
            Literal[
                "order.created",
                "order.paid",
                "order.cancelled",
                "stock.low",
                "payment.created",
                "payment.completed",
                "payment.failed",
                "collection.pending",
                "collection.completed",
                "collection.failed",
                "withdrawal.created",
                "withdrawal.completed",
                "withdrawal.failed",
                "transaction.updated",
                "transfer.pending",
                "transfer.completed",
                "transfer.failed",
                "settlement.completed",
            ]
        ],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Create a webhook config

        Args:
          events: Event types to subscribe to

          url: Webhook endpoint URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/bila/webhooks",
            body=maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        events: List[
            Literal[
                "order.created",
                "order.paid",
                "order.cancelled",
                "stock.low",
                "payment.created",
                "payment.completed",
                "payment.failed",
                "collection.pending",
                "collection.completed",
                "collection.failed",
                "withdrawal.created",
                "withdrawal.completed",
                "withdrawal.failed",
                "transaction.updated",
                "transfer.pending",
                "transfer.completed",
                "transfer.failed",
                "settlement.completed",
            ]
        ]
        | Omit = omit,
        is_active: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook config

        Args:
          events: Event types to subscribe to

          is_active: Whether the webhook is active

          url: Webhook endpoint URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/v1/bila/webhooks/{id}", id=id),
            body=maybe_transform(
                {
                    "events": events,
                    "is_active": is_active,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """List webhook configs"""
        return self._get(
            "/api/v1/bila/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BilaResponse:
        """
        Deactivate a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/api/v1/bila/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BilaResponse,
        )

    def get_deliveries(
        self,
        id: str,
        *,
        end_date: str | Omit = omit,
        event_type: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetDeliveriesResponse:
        """
        Get delivery history

        Args:
          end_date: ISO 8601 end of createdAt range (inclusive)

          event_type: Filter by event type

          page: Page number

          per_page: Items per page

          start_date: ISO 8601 start of createdAt range (inclusive)

          status: Filter by status (QUEUED, DELIVERED, FAILED, RETRYING)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1/bila/webhooks/{id}/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "event_type": event_type,
                        "page": page,
                        "per_page": per_page,
                        "start_date": start_date,
                        "status": status,
                    },
                    webhook_get_deliveries_params.WebhookGetDeliveriesParams,
                ),
            ),
            cast_to=WebhookGetDeliveriesResponse,
        )

    def list_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEventsResponse:
        """List webhook event types"""
        return self._get(
            "/api/v1/bila/webhooks/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListEventsResponse,
        )

    def rotate_secret(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRotateSecretResponse:
        """
        Rotate webhook signing secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/api/v1/bila/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRotateSecretResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    """Webhook configuration and delivery history"""

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/bila-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/bila-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        events: List[
            Literal[
                "order.created",
                "order.paid",
                "order.cancelled",
                "stock.low",
                "payment.created",
                "payment.completed",
                "payment.failed",
                "collection.pending",
                "collection.completed",
                "collection.failed",
                "withdrawal.created",
                "withdrawal.completed",
                "withdrawal.failed",
                "transaction.updated",
                "transfer.pending",
                "transfer.completed",
                "transfer.failed",
                "settlement.completed",
            ]
        ],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Create a webhook config

        Args:
          events: Event types to subscribe to

          url: Webhook endpoint URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/bila/webhooks",
            body=await async_maybe_transform(
                {
                    "events": events,
                    "url": url,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        events: List[
            Literal[
                "order.created",
                "order.paid",
                "order.cancelled",
                "stock.low",
                "payment.created",
                "payment.completed",
                "payment.failed",
                "collection.pending",
                "collection.completed",
                "collection.failed",
                "withdrawal.created",
                "withdrawal.completed",
                "withdrawal.failed",
                "transaction.updated",
                "transfer.pending",
                "transfer.completed",
                "transfer.failed",
                "settlement.completed",
            ]
        ]
        | Omit = omit,
        is_active: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook config

        Args:
          events: Event types to subscribe to

          is_active: Whether the webhook is active

          url: Webhook endpoint URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/v1/bila/webhooks/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "events": events,
                    "is_active": is_active,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """List webhook configs"""
        return await self._get(
            "/api/v1/bila/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    async def deactivate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BilaResponse:
        """
        Deactivate a webhook

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/api/v1/bila/webhooks/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BilaResponse,
        )

    async def get_deliveries(
        self,
        id: str,
        *,
        end_date: str | Omit = omit,
        event_type: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetDeliveriesResponse:
        """
        Get delivery history

        Args:
          end_date: ISO 8601 end of createdAt range (inclusive)

          event_type: Filter by event type

          page: Page number

          per_page: Items per page

          start_date: ISO 8601 start of createdAt range (inclusive)

          status: Filter by status (QUEUED, DELIVERED, FAILED, RETRYING)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1/bila/webhooks/{id}/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "event_type": event_type,
                        "page": page,
                        "per_page": per_page,
                        "start_date": start_date,
                        "status": status,
                    },
                    webhook_get_deliveries_params.WebhookGetDeliveriesParams,
                ),
            ),
            cast_to=WebhookGetDeliveriesResponse,
        )

    async def list_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListEventsResponse:
        """List webhook event types"""
        return await self._get(
            "/api/v1/bila/webhooks/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListEventsResponse,
        )

    async def rotate_secret(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRotateSecretResponse:
        """
        Rotate webhook signing secret

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/api/v1/bila/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRotateSecretResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.deactivate = to_raw_response_wrapper(
            webhooks.deactivate,
        )
        self.get_deliveries = to_raw_response_wrapper(
            webhooks.get_deliveries,
        )
        self.list_events = to_raw_response_wrapper(
            webhooks.list_events,
        )
        self.rotate_secret = to_raw_response_wrapper(
            webhooks.rotate_secret,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            webhooks.deactivate,
        )
        self.get_deliveries = async_to_raw_response_wrapper(
            webhooks.get_deliveries,
        )
        self.list_events = async_to_raw_response_wrapper(
            webhooks.list_events,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            webhooks.rotate_secret,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            webhooks.deactivate,
        )
        self.get_deliveries = to_streamed_response_wrapper(
            webhooks.get_deliveries,
        )
        self.list_events = to_streamed_response_wrapper(
            webhooks.list_events,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            webhooks.rotate_secret,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            webhooks.deactivate,
        )
        self.get_deliveries = async_to_streamed_response_wrapper(
            webhooks.get_deliveries,
        )
        self.list_events = async_to_streamed_response_wrapper(
            webhooks.list_events,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            webhooks.rotate_secret,
        )
