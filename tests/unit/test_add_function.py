from decimal import Decimal

import pytest

from app.calculator import Calculator


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("1", "2", "3"),
        ("-1.5", "0.5", "-1.0"),
        ("7.25", "0", "7.25"),
        ("0.1", "0.2", "0.3"),
    ],
)
def test_add(a, b, expected):
    assert Calculator.add(Decimal(a), Decimal(b)) == Decimal(expected)
