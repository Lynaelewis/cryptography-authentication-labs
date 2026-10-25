"""Educational salted password hashing using Python's standard library.

PBKDF2 is demonstrated for learning; production systems should consider
well-maintained password hashing libraries with Argon2id support.
"""
from __future__ import annotations

import hashlib
import hmac
import os


ITERATIONS = 600_000
SALT_BYTES = 16


def hash_password(password: str, *, salt: bytes | None = None) -> str:
    if not password:
        raise ValueError("Password must not be empty")
    salt = os.urandom(SALT_BYTES) if salt is None else salt
    if len(salt) != SALT_BYTES:
        raise ValueError("Salt must be 16 bytes")
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
    return f"pbkdf2_sha256${ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, encoded: str) -> bool:
    try:
        algorithm, iterations_text, salt_hex, expected_hex = encoded.split("$")
        if algorithm != "pbkdf2_sha256":
            return False
        iterations = int(iterations_text)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(expected_hex)
        if iterations <= 0 or iterations > 2_000_000 or len(salt) != SALT_BYTES or len(expected) != 32:
            return False
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False
