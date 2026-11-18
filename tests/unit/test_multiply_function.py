from decimal import Decimal

import pytest

from app.calculator import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("6", "7", "42"),
        ("-2", "-3", "6"),
        ("2.5", "4", "10.0"),
        ("0", "9", "0"),
    ],
)
def test_multiply(a, b, expected):
    assert Calculator.multiply(Decimal(a), Decimal(b)) == Decimal(expected)
