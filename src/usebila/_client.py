# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BilaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import banks, resolve, accounts, webhooks, transfers, collections, transactions, transfer_recipients
    from .resources.banks import BanksResource, AsyncBanksResource
    from .resources.resolve import ResolveResource, AsyncResolveResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.transfers import TransfersResource, AsyncTransfersResource
    from .resources.collections import CollectionsResource, AsyncCollectionsResource
    from .resources.transactions import TransactionsResource, AsyncTransactionsResource
    from .resources.transfer_recipients import TransferRecipientsResource, AsyncTransferRecipientsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Bila",
    "AsyncBila",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.usebila.com",
    "sandbox": "https://sandbox.usebila.com",
}


class Bila(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Bila client instance.

        This automatically infers the `api_key` argument from the `BILA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BILA_API_KEY")
        if api_key is None:
            raise BilaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BILA_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("BILA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BILA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("BILA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AccountsResource:
        """Account/wallet management endpoints"""
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def transfer_recipients(self) -> TransferRecipientsResource:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import TransferRecipientsResource

        return TransferRecipientsResource(self)

    @cached_property
    def transfers(self) -> TransfersResource:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import TransfersResource

        return TransfersResource(self)

    @cached_property
    def collections(self) -> CollectionsResource:
        """Payment collection operation endpoints"""
        from .resources.collections import CollectionsResource

        return CollectionsResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        """Transaction history endpoints"""
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def banks(self) -> BanksResource:
        """Bank reference data endpoints"""
        from .resources.banks import BanksResource

        return BanksResource(self)

    @cached_property
    def resolve(self) -> ResolveResource:
        """Account resolution/verification endpoints"""
        from .resources.resolve import ResolveResource

        return ResolveResource(self)

    @cached_property
    def with_raw_response(self) -> BilaWithRawResponse:
        return BilaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BilaWithStreamedResponse:
        return BilaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._x_api_key if security.get("x_api_key", False) else {}),
        }

    @property
    def _x_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBila(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBila client instance.

        This automatically infers the `api_key` argument from the `BILA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BILA_API_KEY")
        if api_key is None:
            raise BilaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BILA_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("BILA_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BILA_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("BILA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Account/wallet management endpoints"""
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def transfer_recipients(self) -> AsyncTransferRecipientsResource:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import AsyncTransferRecipientsResource

        return AsyncTransferRecipientsResource(self)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import AsyncTransfersResource

        return AsyncTransfersResource(self)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        """Payment collection operation endpoints"""
        from .resources.collections import AsyncCollectionsResource

        return AsyncCollectionsResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """Transaction history endpoints"""
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def banks(self) -> AsyncBanksResource:
        """Bank reference data endpoints"""
        from .resources.banks import AsyncBanksResource

        return AsyncBanksResource(self)

    @cached_property
    def resolve(self) -> AsyncResolveResource:
        """Account resolution/verification endpoints"""
        from .resources.resolve import AsyncResolveResource

        return AsyncResolveResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBilaWithRawResponse:
        return AsyncBilaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBilaWithStreamedResponse:
        return AsyncBilaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._x_api_key if security.get("x_api_key", False) else {}),
        }

    @property
    def _x_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BilaWithRawResponse:
    _client: Bila

    def __init__(self, client: Bila) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """Account/wallet management endpoints"""
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def transfer_recipients(self) -> transfer_recipients.TransferRecipientsResourceWithRawResponse:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import TransferRecipientsResourceWithRawResponse

        return TransferRecipientsResourceWithRawResponse(self._client.transfer_recipients)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithRawResponse:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import TransfersResourceWithRawResponse

        return TransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithRawResponse:
        """Payment collection operation endpoints"""
        from .resources.collections import CollectionsResourceWithRawResponse

        return CollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithRawResponse:
        """Transaction history endpoints"""
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def banks(self) -> banks.BanksResourceWithRawResponse:
        """Bank reference data endpoints"""
        from .resources.banks import BanksResourceWithRawResponse

        return BanksResourceWithRawResponse(self._client.banks)

    @cached_property
    def resolve(self) -> resolve.ResolveResourceWithRawResponse:
        """Account resolution/verification endpoints"""
        from .resources.resolve import ResolveResourceWithRawResponse

        return ResolveResourceWithRawResponse(self._client.resolve)


class AsyncBilaWithRawResponse:
    _client: AsyncBila

    def __init__(self, client: AsyncBila) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """Account/wallet management endpoints"""
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def transfer_recipients(self) -> transfer_recipients.AsyncTransferRecipientsResourceWithRawResponse:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import AsyncTransferRecipientsResourceWithRawResponse

        return AsyncTransferRecipientsResourceWithRawResponse(self._client.transfer_recipients)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithRawResponse:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import AsyncTransfersResourceWithRawResponse

        return AsyncTransfersResourceWithRawResponse(self._client.transfers)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithRawResponse:
        """Payment collection operation endpoints"""
        from .resources.collections import AsyncCollectionsResourceWithRawResponse

        return AsyncCollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithRawResponse:
        """Transaction history endpoints"""
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def banks(self) -> banks.AsyncBanksResourceWithRawResponse:
        """Bank reference data endpoints"""
        from .resources.banks import AsyncBanksResourceWithRawResponse

        return AsyncBanksResourceWithRawResponse(self._client.banks)

    @cached_property
    def resolve(self) -> resolve.AsyncResolveResourceWithRawResponse:
        """Account resolution/verification endpoints"""
        from .resources.resolve import AsyncResolveResourceWithRawResponse

        return AsyncResolveResourceWithRawResponse(self._client.resolve)


class BilaWithStreamedResponse:
    _client: Bila

    def __init__(self, client: Bila) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """Account/wallet management endpoints"""
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def transfer_recipients(self) -> transfer_recipients.TransferRecipientsResourceWithStreamingResponse:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import TransferRecipientsResourceWithStreamingResponse

        return TransferRecipientsResourceWithStreamingResponse(self._client.transfer_recipients)

    @cached_property
    def transfers(self) -> transfers.TransfersResourceWithStreamingResponse:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import TransfersResourceWithStreamingResponse

        return TransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithStreamingResponse:
        """Payment collection operation endpoints"""
        from .resources.collections import CollectionsResourceWithStreamingResponse

        return CollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithStreamingResponse:
        """Transaction history endpoints"""
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def banks(self) -> banks.BanksResourceWithStreamingResponse:
        """Bank reference data endpoints"""
        from .resources.banks import BanksResourceWithStreamingResponse

        return BanksResourceWithStreamingResponse(self._client.banks)

    @cached_property
    def resolve(self) -> resolve.ResolveResourceWithStreamingResponse:
        """Account resolution/verification endpoints"""
        from .resources.resolve import ResolveResourceWithStreamingResponse

        return ResolveResourceWithStreamingResponse(self._client.resolve)


class AsyncBilaWithStreamedResponse:
    _client: AsyncBila

    def __init__(self, client: AsyncBila) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """Account/wallet management endpoints"""
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def transfer_recipients(self) -> transfer_recipients.AsyncTransferRecipientsResourceWithStreamingResponse:
        """Transfer recipient management endpoints"""
        from .resources.transfer_recipients import AsyncTransferRecipientsResourceWithStreamingResponse

        return AsyncTransferRecipientsResourceWithStreamingResponse(self._client.transfer_recipients)

    @cached_property
    def transfers(self) -> transfers.AsyncTransfersResourceWithStreamingResponse:
        """Payout/transfer operation endpoints"""
        from .resources.transfers import AsyncTransfersResourceWithStreamingResponse

        return AsyncTransfersResourceWithStreamingResponse(self._client.transfers)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithStreamingResponse:
        """Payment collection operation endpoints"""
        from .resources.collections import AsyncCollectionsResourceWithStreamingResponse

        return AsyncCollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithStreamingResponse:
        """Transaction history endpoints"""
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Webhook configuration and delivery history"""
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def banks(self) -> banks.AsyncBanksResourceWithStreamingResponse:
        """Bank reference data endpoints"""
        from .resources.banks import AsyncBanksResourceWithStreamingResponse

        return AsyncBanksResourceWithStreamingResponse(self._client.banks)

    @cached_property
    def resolve(self) -> resolve.AsyncResolveResourceWithStreamingResponse:
        """Account resolution/verification endpoints"""
        from .resources.resolve import AsyncResolveResourceWithStreamingResponse

        return AsyncResolveResourceWithStreamingResponse(self._client.resolve)


Client = Bila

AsyncClient = AsyncBila
