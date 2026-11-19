# Python Password Generator

A simple, beginner-friendly command-line password generator written in Python. It uses Python's built-in `secrets` module to generate cryptographically strong passwords with customizable length and character types.

## Features

- **Cryptographically Secure:** Uses `secrets` instead of `random` for unpredictable password generation.
- **Customizable Options:** Choose password length and toggle uppercase letters, lowercase letters, digits, and symbols.
- **Guaranteed Variety:** Ensures at least one character from each selected category appears in the final password, then shuffles the characters securely.
- **Input Validation:** Handles invalid lengths or unselected character sets gracefully.

## Requirements

- Python 3.6 or higher (no external packages required—uses only the Python Standard Library).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing `password_generator.py`.
3. Run the script:

```bash
python password_generator.py
```

## Example Usage

```text
=== Python Password Generator ===
Enter desired password length (e.g., 16): 16
Include uppercase letters (A-Z)? (y/n): y
Include lowercase letters (a-z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include symbols (!@#$...)? (y/n): y

Generated Password: K9#mP2$vL8@xQ4!z
```

## Project Ideas to Extend This

- Add a **password strength scorer** (Weak, Medium, Strong).
- Save generated passwords (or copy directly to the clipboard using `pyperclip`).
- Add command-line flags using `argparse` (e.g., `python password_generator.py --length 20 --no-symbols`).