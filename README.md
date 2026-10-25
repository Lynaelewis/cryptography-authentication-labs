# Cryptography & Authentication Labs

**Educational security demonstrations | Python | SHA-256 | Password hashing**

This public repository contains **new, sanitized, AI-assisted learning examples** inspired by cybersecurity topics studied in coursework. It does **not** contain copied course submissions, private assignment materials, attack scripts, real credentials, or sensitive data.

## What is included

| File | Topic | Security concept |
| --- | --- | --- |
| [examples/file_integrity.py](examples/file_integrity.py) | SHA-256 file hashing | Detecting file changes using a separately trusted expected digest |
| [examples/password_storage.py](examples/password_storage.py) | Salted PBKDF2-HMAC-SHA256 | Password storage, salts, and constant-time verification |
| [tests/test_security_examples.py](tests/test_security_examples.py) | Unit tests | Checking expected outcomes and negative cases |

## Run the tests

Requires **Python 3.10+**. No third-party packages required.

```bash
python -m unittest discover -s tests -v
```

The tests cover known SHA-256 outputs, file modification detection, correct/incorrect passwords, random salts, and malformed stored hashes.

## Why these controls matter

**File integrity:** A SHA-256 digest can reveal whether a downloaded file differs from an expected version. The expected digest must come from an independent, trusted source; a digest published by the same compromised source may not establish authenticity.

**Password storage:** Storing plaintext passwords or using a fast unsalted digest is unsafe. PBKDF2 combines a unique salt with repeated hashing to increase the cost of offline guessing. Real systems should use an appropriate modern password-hashing library, preferably Argon2id where available, and follow current organizational guidance.

## Project provenance and scope

These demonstrations were drafted with AI assistance for a public portfolio and are **not** presented as independently authored original coursework. They are intended for review, experimentation, and explanation. The repository does not yet demonstrate RSA signatures or AES encryption; those may be added later after separate review and testing.

## Suggested learning exercises

1. Change a file after recording its trusted digest and rerun the verification.
2. Hash the same sample password twice and compare the stored representations.
3. Explain why a random salt is public but still valuable.
4. Compare integrity verification with authenticity verification using a digital signature.

## References

- [NIST SP 800-63B — Digital Identity Guidelines: Authentication and Lifecycle Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
