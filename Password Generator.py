import secrets
import string


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a cryptographically strong random password."""
    character_pools = []
    guaranteed_chars = []

    if use_uppercase:
        pool = string.ascii_uppercase
        character_pools.append(pool)
        guaranteed_chars.append(secrets.choice(pool))

    if use_lowercase:
        pool = string.ascii_lowercase
        character_pools.append(pool)
        guaranteed_chars.append(secrets.choice(pool))

    if use_digits:
        pool = string.digits
        character_pools.append(pool)
        guaranteed_chars.append(secrets.choice(pool))

    if use_symbols:
        pool = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        character_pools.append(pool)
        guaranteed_chars.append(secrets.choice(pool))

    if not character_pools:
        raise ValueError("Select at least one character type.")

    if length < len(guaranteed_chars):
        raise ValueError(
            f"Password length must be at least {len(guaranteed_chars)} "
            f"to include all selected character types."
        )

    all_chars = "".join(character_pools)
    remaining_length = length - len(guaranteed_chars)

    password_chars = guaranteed_chars + [
        secrets.choice(all_chars) for _ in range(remaining_length)
    ]

    # Shuffle in place so guaranteed characters aren't always at the start
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def get_yes_no(prompt: str) -> bool:
    """Prompt user for a y/n answer and return a boolean."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main() -> None:
    print("=== Python Password Generator ===")
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 16): ").strip())
            if length <= 0:
                print("Length must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    use_uppercase = get_yes_no("Include uppercase letters (A-Z)?")
    use_lowercase = get_yes_no("Include lowercase letters (a-z)?")
    use_digits = get_yes_no("Include numbers (0-9)?")
    use_symbols = get_yes_no("Include symbols (!@#$...)?")

    try:
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_symbols=use_symbols,
        )
        print(f"\nGenerated Password: {password}")
    except ValueError as err:
        print(f"\nError: {err}")


if __name__ == "__main__":
    main()