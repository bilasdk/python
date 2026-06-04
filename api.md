# Accounts

Types:

```python
from bila.types import (
    BilaResponse,
    AccountRetrieveResponse,
    AccountListResponse,
    AccountGetBalanceResponse,
)
```

Methods:

- <code title="get /api/v1/bila/accounts/{id}">client.accounts.<a href="./src/bila/resources/accounts.py">retrieve</a>(id) -> <a href="./src/bila/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /api/v1/bila/accounts">client.accounts.<a href="./src/bila/resources/accounts.py">list</a>(\*\*<a href="src/bila/types/account_list_params.py">params</a>) -> <a href="./src/bila/types/account_list_response.py">AccountListResponse</a></code>
- <code title="get /api/v1/bila/accounts/{id}/balance">client.accounts.<a href="./src/bila/resources/accounts.py">get_balance</a>(id) -> <a href="./src/bila/types/account_get_balance_response.py">AccountGetBalanceResponse</a></code>

# TransferRecipients

Types:

```python
from bila.types import (
    TransferRecipientRetrieveResponse,
    TransferRecipientListResponse,
    TransferRecipientCreateBankAccountResponse,
    TransferRecipientCreateMobileMoneyResponse,
)
```

Methods:

- <code title="get /api/v1/bila/transfer-recipients/{id}">client.transfer_recipients.<a href="./src/bila/resources/transfer_recipients.py">retrieve</a>(id) -> <a href="./src/bila/types/transfer_recipient_retrieve_response.py">TransferRecipientRetrieveResponse</a></code>
- <code title="get /api/v1/bila/transfer-recipients">client.transfer_recipients.<a href="./src/bila/resources/transfer_recipients.py">list</a>(\*\*<a href="src/bila/types/transfer_recipient_list_params.py">params</a>) -> <a href="./src/bila/types/transfer_recipient_list_response.py">TransferRecipientListResponse</a></code>
- <code title="post /api/v1/bila/transfer-recipients/bank-account">client.transfer_recipients.<a href="./src/bila/resources/transfer_recipients.py">create_bank_account</a>(\*\*<a href="src/bila/types/transfer_recipient_create_bank_account_params.py">params</a>) -> <a href="./src/bila/types/transfer_recipient_create_bank_account_response.py">TransferRecipientCreateBankAccountResponse</a></code>
- <code title="post /api/v1/bila/transfer-recipients/mobile-money">client.transfer_recipients.<a href="./src/bila/resources/transfer_recipients.py">create_mobile_money</a>(\*\*<a href="src/bila/types/transfer_recipient_create_mobile_money_params.py">params</a>) -> <a href="./src/bila/types/transfer_recipient_create_mobile_money_response.py">TransferRecipientCreateMobileMoneyResponse</a></code>

# Transfers

Types:

```python
from bila.types import (
    TransferRetrieveResponse,
    TransferListResponse,
    TransferGetStatusByReferenceResponse,
    TransferInitiateBankTransferResponse,
    TransferInitiateMobileMoneyTransferResponse,
)
```

Methods:

- <code title="get /api/v1/bila/transfers/{id}">client.transfers.<a href="./src/bila/resources/transfers.py">retrieve</a>(id) -> <a href="./src/bila/types/transfer_retrieve_response.py">TransferRetrieveResponse</a></code>
- <code title="get /api/v1/bila/transfers">client.transfers.<a href="./src/bila/resources/transfers.py">list</a>(\*\*<a href="src/bila/types/transfer_list_params.py">params</a>) -> <a href="./src/bila/types/transfer_list_response.py">TransferListResponse</a></code>
- <code title="get /api/v1/bila/transfers/status/{reference}">client.transfers.<a href="./src/bila/resources/transfers.py">get_status_by_reference</a>(reference) -> <a href="./src/bila/types/transfer_get_status_by_reference_response.py">TransferGetStatusByReferenceResponse</a></code>
- <code title="post /api/v1/bila/transfers/bank-account">client.transfers.<a href="./src/bila/resources/transfers.py">initiate_bank_transfer</a>(\*\*<a href="src/bila/types/transfer_initiate_bank_transfer_params.py">params</a>) -> <a href="./src/bila/types/transfer_initiate_bank_transfer_response.py">TransferInitiateBankTransferResponse</a></code>
- <code title="post /api/v1/bila/transfers/mobile-money">client.transfers.<a href="./src/bila/resources/transfers.py">initiate_mobile_money_transfer</a>(\*\*<a href="src/bila/types/transfer_initiate_mobile_money_transfer_params.py">params</a>) -> <a href="./src/bila/types/transfer_initiate_mobile_money_transfer_response.py">TransferInitiateMobileMoneyTransferResponse</a></code>

# Collections

Types:

```python
from bila.types import (
    CollectionRetrieveResponse,
    CollectionListResponse,
    CollectionGetStatusByReferenceResponse,
    CollectionInitiateMobileMoneyCollectionResponse,
)
```

Methods:

- <code title="get /api/v1/bila/collections/{id}">client.collections.<a href="./src/bila/resources/collections.py">retrieve</a>(id) -> <a href="./src/bila/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>
- <code title="get /api/v1/bila/collections">client.collections.<a href="./src/bila/resources/collections.py">list</a>(\*\*<a href="src/bila/types/collection_list_params.py">params</a>) -> <a href="./src/bila/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="get /api/v1/bila/collections/status/{reference}">client.collections.<a href="./src/bila/resources/collections.py">get_status_by_reference</a>(reference) -> <a href="./src/bila/types/collection_get_status_by_reference_response.py">CollectionGetStatusByReferenceResponse</a></code>
- <code title="post /api/v1/bila/collections/mobile-money">client.collections.<a href="./src/bila/resources/collections.py">initiate_mobile_money_collection</a>(\*\*<a href="src/bila/types/collection_initiate_mobile_money_collection_params.py">params</a>) -> <a href="./src/bila/types/collection_initiate_mobile_money_collection_response.py">CollectionInitiateMobileMoneyCollectionResponse</a></code>

# Transactions

Types:

```python
from bila.types import TransactionRetrieveResponse, TransactionListResponse
```

Methods:

- <code title="get /api/v1/bila/transactions/{id}">client.transactions.<a href="./src/bila/resources/transactions.py">retrieve</a>(id) -> <a href="./src/bila/types/transaction_retrieve_response.py">TransactionRetrieveResponse</a></code>
- <code title="get /api/v1/bila/transactions">client.transactions.<a href="./src/bila/resources/transactions.py">list</a>(\*\*<a href="src/bila/types/transaction_list_params.py">params</a>) -> <a href="./src/bila/types/transaction_list_response.py">TransactionListResponse</a></code>

# Webhooks

Types:

```python
from bila.types import (
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookGetDeliveriesResponse,
    WebhookListEventsResponse,
    WebhookRotateSecretResponse,
)
```

Methods:

- <code title="post /api/v1/bila/webhooks">client.webhooks.<a href="./src/bila/resources/webhooks.py">create</a>(\*\*<a href="src/bila/types/webhook_create_params.py">params</a>) -> <a href="./src/bila/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="patch /api/v1/bila/webhooks/{id}">client.webhooks.<a href="./src/bila/resources/webhooks.py">update</a>(id, \*\*<a href="src/bila/types/webhook_update_params.py">params</a>) -> <a href="./src/bila/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /api/v1/bila/webhooks">client.webhooks.<a href="./src/bila/resources/webhooks.py">list</a>() -> <a href="./src/bila/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /api/v1/bila/webhooks/{id}">client.webhooks.<a href="./src/bila/resources/webhooks.py">deactivate</a>(id) -> <a href="./src/bila/types/bila_response.py">BilaResponse</a></code>
- <code title="get /api/v1/bila/webhooks/{id}/deliveries">client.webhooks.<a href="./src/bila/resources/webhooks.py">get_deliveries</a>(id, \*\*<a href="src/bila/types/webhook_get_deliveries_params.py">params</a>) -> <a href="./src/bila/types/webhook_get_deliveries_response.py">WebhookGetDeliveriesResponse</a></code>
- <code title="get /api/v1/bila/webhooks/events">client.webhooks.<a href="./src/bila/resources/webhooks.py">list_events</a>() -> <a href="./src/bila/types/webhook_list_events_response.py">WebhookListEventsResponse</a></code>
- <code title="post /api/v1/bila/webhooks/{id}/rotate-secret">client.webhooks.<a href="./src/bila/resources/webhooks.py">rotate_secret</a>(id) -> <a href="./src/bila/types/webhook_rotate_secret_response.py">WebhookRotateSecretResponse</a></code>

# Banks

Types:

```python
from bila.types import BankListResponse
```

Methods:

- <code title="get /api/v1/bila/banks">client.banks.<a href="./src/bila/resources/banks.py">list</a>(\*\*<a href="src/bila/types/bank_list_params.py">params</a>) -> <a href="./src/bila/types/bank_list_response.py">BankListResponse</a></code>

# Resolve

Types:

```python
from bila.types import ResolveBankAccountResponse, ResolveMobileMoneyResponse
```

Methods:

- <code title="post /api/v1/bila/resolve/bank-account">client.resolve.<a href="./src/bila/resources/resolve.py">bank_account</a>(\*\*<a href="src/bila/types/resolve_bank_account_params.py">params</a>) -> <a href="./src/bila/types/resolve_bank_account_response.py">ResolveBankAccountResponse</a></code>
- <code title="post /api/v1/bila/resolve/mobile-money">client.resolve.<a href="./src/bila/resources/resolve.py">mobile_money</a>(\*\*<a href="src/bila/types/resolve_mobile_money_params.py">params</a>) -> <a href="./src/bila/types/resolve_mobile_money_response.py">ResolveMobileMoneyResponse</a></code>
