from decimal import Decimal

import pytest

from app.calculator import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("5", "3", "2"),
        ("-1.5", "0.5", "-2.0"),
        ("1", "2", "-1"),
        ("7.25", "0", "7.25"),
        ("0.3", "0.1", "0.2"),
    ],
)
def test_subtract(a, b, expected):
    assert Calculator.subtract(Decimal(a), Decimal(b)) == Decimal(expected)
