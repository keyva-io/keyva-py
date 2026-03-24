"""
Keyva — Python client for the Keyva Credential management server.

Auto-generated from keyva protocol spec. Do not edit.

Usage::

    from keyva import KeyvaClient

    async with await KeyvaClient.connect("keyva://://localhost") as client:
        result = await client.issue("my-keyspace", ttl_secs=3600)
        print(result.credential_id, result.token)
"""
from .client import KeyvaClient
from .errors import KeyvaError
from .types import ConfigGetResponse, HealthResponse, InspectResponse, IssueResponse, JwksResponse, KeysResponse, KeystateResponse, PasswordChangeResponse, PasswordImportResponse, PasswordSetResponse, PasswordVerifyResponse, RefreshResponse, RevokeResponse, RevokeBulkResponse, RevokeFamilyResponse, RotateResponse, SchemaResponse, VerifyResponse
from .errors import BadargError, ChainLimitError, CryptoError, DeniedError, DisabledError, ExpiredError, InternalError, LockedError, NotfoundError, NotreadyError, ReuseDetectedError, StateErrorError, StorageError, ValidationErrorError, WrongtypeError

__version__ = "0.1.0"

__all__ = [
    "KeyvaClient",
    "KeyvaError",
    "ConfigGetResponse",
    "HealthResponse",
    "InspectResponse",
    "IssueResponse",
    "JwksResponse",
    "KeysResponse",
    "KeystateResponse",
    "PasswordChangeResponse",
    "PasswordImportResponse",
    "PasswordSetResponse",
    "PasswordVerifyResponse",
    "RefreshResponse",
    "RevokeResponse",
    "RevokeBulkResponse",
    "RevokeFamilyResponse",
    "RotateResponse",
    "SchemaResponse",
    "VerifyResponse",
    "BadargError",
    "ChainLimitError",
    "CryptoError",
    "DeniedError",
    "DisabledError",
    "ExpiredError",
    "InternalError",
    "LockedError",
    "NotfoundError",
    "NotreadyError",
    "ReuseDetectedError",
    "StateErrorError",
    "StorageError",
    "ValidationErrorError",
    "WrongtypeError",
]
