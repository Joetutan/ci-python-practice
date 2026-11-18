from decimal import Decimal, InvalidOperation


def read_decimal(prompt: str) -> Decimal:
    """Prompt until the user enters a valid decimal number.

    Args:
        prompt: Text shown on each input attempt.

    Returns:
        The Decimal parsed from the user's input.

    Notes:
        Invalid input prints an error message and prompts again indefinitely.
    """
    while True:
        try:
            return Decimal(input(prompt).strip())
        except InvalidOperation:
            print("Not a valid number, try again.\n")
