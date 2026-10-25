"""Educational SHA-256 file integrity verification (standard library only).

A digest detects accidental or malicious changes only when the expected digest
comes from a trusted, independent source.
"""
from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_file(path: str | Path, trusted_expected_hex: str) -> bool:
    """Compare a local file digest to a separately trusted SHA-256 value."""
    return hashlib.compare_digest(sha256_file(path), trusted_expected_hex.lower()) if hasattr(hashlib, "compare_digest") else __import__("hmac").compare_digest(sha256_file(path), trusted_expected_hex.lower())
