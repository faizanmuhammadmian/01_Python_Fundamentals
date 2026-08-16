def print_line():
    """Print a separator line."""
    print("=" * 45)


def show_menu():
    """Display the main menu."""
    print_line()
    print("       🔐 MESSAGE ENCRYPTOR")
    print_line()
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    print_line()


def get_choice():
    """Get a valid menu choice from the user."""
    while True:
        choice = input("Enter your choice: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("❌ Invalid choice. Please enter 1, 2, or 3.")