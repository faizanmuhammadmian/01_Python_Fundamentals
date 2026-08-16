from cipher import create_characters, encrypt_message, decrypt_message
from key_manager import generate_key, save_key, load_key
from utils import show_menu, print_line


def setup_key(chars):
    """Load an existing key or create a new one."""
    key = load_key()

    if key is None:
        print("🔑 No encryption key found.")
        print("Generating a new key...")

        key = generate_key(chars)
        save_key(key)

        print("✅ New encryption key created and saved.")

    else:
        print("🔑 Existing encryption key loaded.")

    return key


def encrypt():
    """Get a message and encrypt it."""
    message = input("\nEnter your message: ")

    if not message:
        print("❌ Message cannot be empty.")
        return

    try:
        encrypted = encrypt_message(message, chars, key)

        print_line()
        print(f"Original Message : {message}")
        print(f"Encrypted Message: {encrypted}")
        print_line()

    except ValueError as error:
        print(f"❌ Error: {error}")


def decrypt():
    """Get an encrypted message and decrypt it."""
    message = input("\nEnter encrypted message: ")

    if not message:
        print("❌ Message cannot be empty.")
        return

    try:
        decrypted = decrypt_message(message, chars, key)

        print_line()
        print(f"Encrypted Message: {message}")
        print(f"Decrypted Message: {decrypted}")
        print_line()

    except ValueError as error:
        print(f"❌ Error: {error}")


# --------------------------------
# Program Setup
# --------------------------------

chars = create_characters()
key = setup_key(chars)


# --------------------------------
# Main Program
# --------------------------------

while True:

    show_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        encrypt()

    elif choice == "2":
        decrypt()

    elif choice == "3":
        print("\n👋 Thank you for using Message Encryptor!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1, 2, or 3.")