#  Message Encryption & Decryption

A modular Python application that demonstrates **message encryption and decryption using a substitution cipher**.

The project was designed as a Python learning project and demonstrates important software development concepts including **functions, modules, file handling, JSON, exception handling, testing, and project organization**.

The application generates a randomized substitution key, stores the key locally, and uses the same key to encrypt and decrypt messages.

---

##  Features

*  Encrypt plain-text messages
*  Decrypt encrypted messages
*  Generate a randomized substitution key
*  Save the encryption key to a JSON file
*  Load an existing encryption key
*  Validate user input
*  Handle common errors
*  Modular multi-file architecture
*  Automated encryption/decryption testing
*  Simple command-line interface

---

##  Technologies Used

* **Python 3**
* `random`
* `string`
* `json`
* `pathlib`
* `pytest` for testing

The encryption application itself uses Python's standard library.

---

#  Project Structure

```text
Message-Encryption/
│
├── main.py
│
├── cipher.py
├── key_manager.py
├── utils.py
│
├── data/
│   └── encryption_key.json
│
├── tests/
│   └── test_cipher.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

#  Code Architecture

The project follows a simple **modular architecture**, where each file has one primary responsibility.

```text
                         ┌──────────────────────┐
                         │       main.py        │
                         │  Application Entry   │
                         │       Point          │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
          ┌────────────────┐ ┌───────────────┐ ┌──────────────┐
          │   cipher.py    │ │ key_manager.py│ │   utils.py   │
          │                │ │               │ │              │
          │ Encryption     │ │ Generate Key  │ │ Menu         │
          │ Decryption     │ │ Save Key      │ │ Formatting   │
          │ Characters     │ │ Load Key      │ │ Input        │
          └───────┬────────┘ └───────┬───────┘ └──────────────┘
                  │                  │
                  │                  ▼
                  │        ┌────────────────────┐
                  │        │       data/        │
                  │        │                    │
                  │        │ encryption_key.json│
                  │        └────────────────────┘
                  │
                  ▼
          ┌─────────────────┐
          │     tests/      │
          │ test_cipher.py  │
          │                 │
          │ Automated Tests │
          └─────────────────┘
```

---

#  Module Responsibilities

## `main.py`

The main entry point of the application.

Responsibilities:

* Start the application
* Load or generate the encryption key
* Display the menu
* Receive user input
* Call encryption/decryption functions
* Handle application flow

---

## `cipher.py`

Contains the core encryption and decryption logic.

Responsibilities:

* Create supported characters
* Encrypt messages
* Decrypt messages
* Validate supported characters

Example:

```python
encrypted = encrypt_message(message, chars, key)
```

---

## `key_manager.py`

Responsible for encryption-key management.

Responsibilities:

* Generate a randomized key
* Save the key
* Load the key
* Create the `data/` directory when necessary

The key is stored in:

```text
data/encryption_key.json
```

Keeping the key separate from the encryption logic makes the project easier to maintain.

---

## `utils.py`

Contains reusable helper functions.

Responsibilities:

* Display the application menu
* Print separators
* Handle common interface formatting

---

#  `tests/test_cipher.py`

The `test_cipher.py` file contains **automated tests** for the encryption and decryption functionality.

Its main purpose is to verify that:

```text
Message
   ↓
Encrypt
   ↓
Encrypted Message
   ↓
Decrypt
   ↓
Original Message
```

The test uses Python's `assert` statement to verify that the decrypted message matches the original message.

```python
assert decrypted == message
```

If the condition is true:

```text
PASSED 
```

If it is false:

```text
FAILED 
```

### Why automated testing?

Testing helps detect problems when the application is changed or expanded.

For example:

```text
Change cipher.py
      ↓
Run tests
      ↓
Tests pass? ── YES → Continue development
      │
      NO
      ↓
Investigate the problem
```

This is an important practice in professional software development.

---

#  How Encryption Works

The application uses a **substitution cipher**.

First, the program creates a list of supported characters:

```python
chars = " " + string.punctuation + string.digits + string.ascii_letters
```

A copy of this list is created:

```python
key = chars.copy()
```

The key is randomly shuffled:

```python
random.shuffle(key)
```

The character at each position in `chars` corresponds to the character at the same position in `key`.

For example:

```text
Original Characters:

A B C D E
│ │ │ │ │
↓ ↓ ↓ ↓ ↓
Key:

X 7 @ # P
```

Therefore:

```text
A → X
B → 7
C → @
D → #
E → P
```

---

#  Encryption & Decryption Flow

```text
                 USER MESSAGE
                       │
                       ▼
              ┌─────────────────┐
              │   Encrypt       │
              │   Message       │
              └────────┬────────┘
                       │
                       ▼
              ENCRYPTED MESSAGE
                       │
                       ▼
              ┌─────────────────┐
              │   Decrypt       │
              │   Message       │
              └────────┬────────┘
                       │
                       ▼
               ORIGINAL MESSAGE
```

---

#  Key Management Flow

The application does not generate a completely new key every time it starts.

Instead:

```text
                 Start Program
                      │
                      ▼
             Check for key file
                      │
             ┌────────┴────────┐
             │                 │
          Exists?            Missing?
             │                 │
             ▼                 ▼
        Load Key         Generate Key
             │                 │
             │                 ▼
             │             Save Key
             │                 │
             └────────┬────────┘
                      ▼
                  Run Program
```

This allows the same key to be reused for future encryption and decryption operations.

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Open the Project

```bash
cd Message-Encryption
```

## 3. Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

#  Install Dependencies

The main application uses only Python's standard library.

For testing:

```bash
pip install pytest
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
python main.py
```

You will see:

```text
=============================================
       MESSAGE ENCRYPTOR
=============================================
1. Encrypt Message
2. Decrypt Message
3. Exit
=============================================
Enter your choice:
```

---

#  Run Tests

From the project root:

```bash
pytest
```

A successful test should produce output similar to:

```text
1 passed
```

This confirms that the encryption/decryption process is working according to the test.

---

#  Example

### Encrypt

```text
Enter your choice: 1

Enter your message: Hello World!

Original Message : Hello World!
Encrypted Message: [encrypted text]
```

### Decrypt

```text
Enter your choice: 2

Enter encrypted message: [encrypted text]

Encrypted Message: [encrypted text]
Decrypted Message: Hello World!
```

---

#  Concepts Practiced

This project demonstrates:

* Python modules
* Functions
* Lists
* Strings
* Loops
* Conditional statements
* Exception handling
* File handling
* JSON
* `pathlib`
* Randomization
* Modular programming
* Unit testing
* Project structure
* `.gitignore`
* Virtual environments

---

#  Security Disclaimer

This project is intended for **educational purposes**.

The substitution cipher used here is **not considered secure modern cryptography** and should not be used to protect passwords, financial information, private communications, or other sensitive data.

For real-world security applications, established cryptographic algorithms and trusted libraries should be used.

---

#  Future Improvements

Possible future improvements include:

* [ ] Add an object-oriented architecture
* [ ] Add stronger input validation
* [ ] Add more unit tests
* [ ] Add test cases for invalid characters
* [ ] Add test cases for empty messages
* [ ] Add logging
* [ ] Add file-based message encryption
* [ ] Add a graphical user interface
* [ ] Add modern cryptography using a trusted library
* [ ] Add configuration management
* [ ] Improve command-line interface

---

#  Learning Objective

The main goal of this project is to understand how a Python application can be divided into **small, independent modules** instead of putting all functionality into one file.

It also introduces the idea of **automated testing**, where software can verify its own functionality instead of relying entirely on manual testing.

---

# Author

**Mian Muhammad Faizan**

Computer Science Student
Python | Data Analysis | Machine Learning

---

# License

This project is intended for educational and learning purposes.
