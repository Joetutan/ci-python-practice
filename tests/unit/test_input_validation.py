from decimal import Decimal
from unittest.mock import patch

import pytest

from utils.input_validation import read_decimal


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("42.5", Decimal("42.5")),
        ("  -3.14  ", Decimal("-3.14")),
    ],
)
def test_read_decimal_returns_decimal(raw, expected):
    with patch("builtins.input", return_value=raw):
        assert read_decimal("Enter number...\n") == expected


@pytest.mark.parametrize("invalid", ["not-a-number", "1,5", ""])
def test_read_decimal_retries_on_invalid_input(invalid, capsys):
    with patch("builtins.input", side_effect=[invalid, "7"]):
        assert read_decimal("Enter number...\n") == Decimal(7)
    assert "Not a valid number" in capsys.readouterr().out
