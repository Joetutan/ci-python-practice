from decimal import Decimal


class Calculator:
    """Basic arithmetic operations on Decimal values."""

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Return a minus b."""
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Return a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Zero division not allowed...")
        return a / b
