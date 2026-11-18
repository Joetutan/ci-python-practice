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


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("1e50", "1e50", "1e100"),
        ("0.001", "0.001", "0.000001"),
        ("-1", "123.456", "-123.456"),
    ],
)
def test_multiply_edge_cases(a, b, expected):
    assert Calculator.multiply(Decimal(a), Decimal(b)) == Decimal(expected)
