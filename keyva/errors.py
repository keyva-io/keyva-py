"""
Keyva error types.

Auto-generated from keyva protocol spec. Do not edit.
"""
from __future__ import annotations


class KeyvaError(Exception):
    """Base exception for all Keyva operations."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

    @classmethod
    def _from_server(cls, code: str, message: str) -> "KeyvaError":
        """Internal: construct the appropriate error subclass from a server error."""
        subclass = _ERROR_MAP.get(code, KeyvaError)
        return subclass(code, message)


class BadargError(KeyvaError):
    """Missing or malformed command argument"""


class ChainLimitError(KeyvaError):
    """Refresh token chain limit exceeded"""


class CryptoError(KeyvaError):
    """Cryptographic operation failed"""


class DeniedError(KeyvaError):
    """Authentication required or insufficient permissions"""


class DisabledError(KeyvaError):
    """Keyspace is disabled"""


class ExpiredError(KeyvaError):
    """Credential has expired"""


class InternalError(KeyvaError):
    """Unexpected internal error"""


class LockedError(KeyvaError):
    """Account temporarily locked due to too many failed attempts"""


class NotfoundError(KeyvaError):
    """Credential, keyspace, or resource does not exist"""


class NotreadyError(KeyvaError):
    """Server is not ready (still starting up)"""


class ReuseDetectedError(KeyvaError):
    """Refresh token reuse detected — family revoked"""


class StateErrorError(KeyvaError):
    """Credential is in wrong state for this operation"""


class StorageError(KeyvaError):
    """Storage engine error"""


class ValidationErrorError(KeyvaError):
    """Metadata or claims failed schema validation"""


class WrongtypeError(KeyvaError):
    """Operation not supported for this keyspace type"""


_ERROR_MAP: dict[str, type[KeyvaError]] = {
    "BADARG": BadargError,
    "CHAIN_LIMIT": ChainLimitError,
    "CRYPTO": CryptoError,
    "DENIED": DeniedError,
    "DISABLED": DisabledError,
    "EXPIRED": ExpiredError,
    "INTERNAL": InternalError,
    "LOCKED": LockedError,
    "NOTFOUND": NotfoundError,
    "NOTREADY": NotreadyError,
    "REUSE_DETECTED": ReuseDetectedError,
    "STATE_ERROR": StateErrorError,
    "STORAGE": StorageError,
    "VALIDATION_ERROR": ValidationErrorError,
    "WRONGTYPE": WrongtypeError,
}
