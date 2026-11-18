from decimal import Decimal

import pytest

from app.calculator import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("6", "3", "2"),
        ("-8", "2", "-4"),
        ("7.5", "2.5", "3"),
        ("0", "5", "0"),
    ],
)
def test_divide(a, b, expected):
    assert Calculator.divide(Decimal(a), Decimal(b)) == Decimal(expected)
