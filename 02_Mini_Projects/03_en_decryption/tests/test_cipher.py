from cipher import create_characters, encrypt_message, decrypt_message
from key_manager import generate_key


def test_encryption_and_decryption():

    chars = create_characters()
    key = generate_key(chars)

    message = "Hello World!"

    encrypted = encrypt_message(message, chars, key)
    decrypted = decrypt_message(encrypted, chars, key)

    assert decrypted == message