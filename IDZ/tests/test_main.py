import pytest
from app.main import calculate_total


def test_calculate_total_integers():
    assert calculate_total([10, 20, 30]) == 60


def test_calculate_total_floats():
    assert calculate_total([5.5, 4.5]) == 10.0


def test_empty_list():
    assert calculate_total([]) == 0


def test_negative_price():
    with pytest.raises(ValueError, match="Ціна не може бути від'ємною"):
        calculate_total([10, -5])
