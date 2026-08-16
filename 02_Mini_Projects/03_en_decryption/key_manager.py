import json
import random
from pathlib import Path


KEY_FILE = Path("data/encryption_key.json")


def generate_key(chars):
    """Generate a shuffled encryption key."""
    key = chars.copy()
    random.shuffle(key)

    return key


def save_key(key):
    """Save the encryption key to a JSON file."""
    KEY_FILE.parent.mkdir(exist_ok=True)

    with open(KEY_FILE, "w", encoding="utf-8") as file:
        json.dump(key, file, ensure_ascii=False, indent=4)


def load_key():
    """Load the encryption key from the JSON file."""
    if not KEY_FILE.exists():
        return None

    with open(KEY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)