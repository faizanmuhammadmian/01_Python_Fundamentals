import string


def create_characters():
    """Create the list of supported characters."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    return list(chars)


def encrypt_message(message, chars, key):
    """Encrypt a message using the substitution key."""
    encrypted_message = ""

    for letter in message:
        if letter not in chars:
            raise ValueError(f"Unsupported character: {letter}")

        index = chars.index(letter)
        encrypted_message += key[index]

    return encrypted_message


def decrypt_message(encrypted_message, chars, key):
    """Decrypt an encrypted message using the substitution key."""
    decrypted_message = ""

    for letter in encrypted_message:
        if letter not in key:
            raise ValueError(f"Invalid encrypted character: {letter}")

        index = key.index(letter)
        decrypted_message += chars[index]

    return decrypted_message