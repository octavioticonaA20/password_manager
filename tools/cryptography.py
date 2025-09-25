from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

from argon2 import PasswordHasher
import os


def generate_derived_master_key(master_key: str, salt = os.urandom(16)):
    password_bytes = master_key.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = kdf.derive(password_bytes)

    return key, salt


def encrypt_AES(key, password):
    iv = os.urandom(16)

    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    encrypted_password = encryptor.update(password) + encryptor.finalize()
    tag = bytes(encryptor.tag)

    return bytes(encrypted_password), tag, iv


def decrypt_AES(key, encrypted_password, iv, tag):

    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    password_cracked = decryptor.update(encrypted_password) + decryptor.finalize()

    return password_cracked.decode('utf-8')
