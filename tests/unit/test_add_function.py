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


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("1e100", "1e100", "2e100"),
        ("0.001", "0.0001", "0.0011"),
        ("1.5", "-1.5", "0"),
    ],
)
def test_add_edge_cases(a, b, expected):
    assert Calculator.add(Decimal(a), Decimal(b)) == Decimal(expected)
