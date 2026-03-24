"""
Keyva response types.

Auto-generated from keyva protocol spec. Do not edit.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass
class ConfigGetResponse:
    """Response from CONFIG command."""

    value: str = ""

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "ConfigGetResponse":
        return cls(
            value = data["value"],
        )


@dataclass
class HealthResponse:
    """Response from HEALTH command."""

    state: Optional[str] = None
    keyspaces: Optional[dict[str, Any]] = None
    count: Optional[int] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "HealthResponse":
        return cls(
            state = data.get("state"),
            keyspaces = data.get("keyspaces"),
            count = data.get("count"),
        )


@dataclass
class InspectResponse:
    """Response from INSPECT command."""

    credential_id: str = ""
    state: str = ""
    created_at: int = 0
    expires_at: Optional[int] = None
    last_verified_at: Optional[int] = None
    meta: Optional[dict[str, Any]] = None
    family_id: Optional[str] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "InspectResponse":
        return cls(
            credential_id = data["credential_id"],
            state = data["state"],
            created_at = data["created_at"],
            expires_at = data.get("expires_at"),
            last_verified_at = data.get("last_verified_at"),
            meta = data.get("meta"),
            family_id = data.get("family_id"),
        )


@dataclass
class IssueResponse:
    """Response from ISSUE command."""

    credential_id: str = ""
    token: str = ""
    expires_at: Optional[int] = None
    family_id: Optional[str] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "IssueResponse":
        return cls(
            credential_id = data["credential_id"],
            token = data["token"],
            expires_at = data.get("expires_at"),
            family_id = data.get("family_id"),
        )


@dataclass
class JwksResponse:
    """Response from JWKS command."""

    jwks: str = ""

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "JwksResponse":
        return cls(
            jwks = data["jwks"],
        )


@dataclass
class KeysResponse:
    """Response from KEYS command."""

    cursor: str = ""
    keys: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "KeysResponse":
        return cls(
            cursor = data["cursor"],
            keys = data["keys"],
        )


@dataclass
class KeystateResponse:
    """Response from KEYSTATE command."""

    keys: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "KeystateResponse":
        return cls(
            keys = data["keys"],
        )


@dataclass
class PasswordChangeResponse:
    """Response from PASSWORD command."""

    credential_id: str = ""
    updated_at: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "PasswordChangeResponse":
        return cls(
            credential_id = data["credential_id"],
            updated_at = data["updated_at"],
        )


@dataclass
class PasswordImportResponse:
    """Response from PASSWORD command."""

    credential_id: str = ""
    user_id: str = ""
    algorithm: str = ""
    created_at: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "PasswordImportResponse":
        return cls(
            credential_id = data["credential_id"],
            user_id = data["user_id"],
            algorithm = data["algorithm"],
            created_at = data["created_at"],
        )


@dataclass
class PasswordSetResponse:
    """Response from PASSWORD command."""

    credential_id: str = ""
    user_id: str = ""
    algorithm: str = ""
    created_at: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "PasswordSetResponse":
        return cls(
            credential_id = data["credential_id"],
            user_id = data["user_id"],
            algorithm = data["algorithm"],
            created_at = data["created_at"],
        )


@dataclass
class PasswordVerifyResponse:
    """Response from PASSWORD command."""

    valid: bool = False
    credential_id: str = ""
    metadata: Optional[dict[str, Any]] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "PasswordVerifyResponse":
        return cls(
            valid = data["valid"],
            credential_id = data["credential_id"],
            metadata = data.get("metadata"),
        )


@dataclass
class RefreshResponse:
    """Response from REFRESH command."""

    credential_id: str = ""
    token: str = ""
    family_id: str = ""
    expires_at: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "RefreshResponse":
        return cls(
            credential_id = data["credential_id"],
            token = data["token"],
            family_id = data["family_id"],
            expires_at = data["expires_at"],
        )


@dataclass
class RevokeResponse:
    """Response from REVOKE command."""

    revoked: Optional[int] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "RevokeResponse":
        return cls(
            revoked = data.get("revoked"),
        )


@dataclass
class RevokeBulkResponse:
    """Response from REVOKE command."""

    revoked: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "RevokeBulkResponse":
        return cls(
            revoked = data["revoked"],
        )


@dataclass
class RevokeFamilyResponse:
    """Response from REVOKE command."""

    revoked: int = 0

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "RevokeFamilyResponse":
        return cls(
            revoked = data["revoked"],
        )


@dataclass
class RotateResponse:
    """Response from ROTATE command."""

    new_key_id: str = ""
    old_key_id: str = ""
    dryrun: Optional[str] = None

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "RotateResponse":
        return cls(
            new_key_id = data["new_key_id"],
            old_key_id = data["old_key_id"],
            dryrun = data.get("dryrun"),
        )


@dataclass
class SchemaResponse:
    """Response from SCHEMA command."""

    schema: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "SchemaResponse":
        return cls(
            schema = data["schema"],
        )


@dataclass
class VerifyResponse:
    """Response from VERIFY command."""

    credential_id: str = ""
    claims: Optional[dict[str, Any]] = None
    meta: Optional[dict[str, Any]] = None
    state: str = ""

    @classmethod
    def _from_dict(cls, data: dict[str, Any]) -> "VerifyResponse":
        return cls(
            credential_id = data["credential_id"],
            claims = data.get("claims"),
            meta = data.get("meta"),
            state = data["state"],
        )


