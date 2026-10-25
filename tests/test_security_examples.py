"""Unit tests for safe, standard-library cryptography demonstrations."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from examples.file_integrity import sha256_file, verify_file
from examples.password_storage import hash_password, verify_password


class FileIntegrityTests(unittest.TestCase):
    def test_known_sha256(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "sample.txt"
            file.write_bytes(b"hello")
            expected = hashlib.sha256(b"hello").hexdigest()
            self.assertEqual(sha256_file(file), expected)
            self.assertTrue(verify_file(file, expected))

    def test_detects_modified_file(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "sample.txt"
            file.write_bytes(b"original")
            trusted_digest = sha256_file(file)
            file.write_bytes(b"modified")
            self.assertFalse(verify_file(file, trusted_digest))


class PasswordStorageTests(unittest.TestCase):
    def test_correct_password(self):
        encoded = hash_password("sample passphrase")
        self.assertTrue(verify_password("sample passphrase", encoded))

    def test_wrong_password(self):
        encoded = hash_password("sample passphrase")
        self.assertFalse(verify_password("not the passphrase", encoded))

    def test_unique_random_salts(self):
        first = hash_password("same password")
        second = hash_password("same password")
        self.assertNotEqual(first, second)

    def test_rejects_malformed_hash(self):
        self.assertFalse(verify_password("password", "not-a-valid-hash"))


if __name__ == "__main__":
    unittest.main()
