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


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("1", "0.25", "4"),
        ("-9", "-3", "3"),
        ("1e100", "1e50", "1e50"),
    ],
)
def test_divide_edge_cases(a, b, expected):
    assert Calculator.divide(Decimal(a), Decimal(b)) == Decimal(expected)


@pytest.mark.parametrize("zero", ["0", "0.000"])
def test_divide_by_zero_raises(zero):
    with pytest.raises(ZeroDivisionError, match="Zero division not allowed"):
        Calculator.divide(Decimal(1), Decimal(zero))
