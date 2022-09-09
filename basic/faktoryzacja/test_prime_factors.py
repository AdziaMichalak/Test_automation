import pytest
from prime import prime_factors


def test_prime_factors():
    assert callable(prime_factors)


def test_illegal_symbols():
    with pytest.raises(ValueError):
        prime_factors("screwdriver")


def test_num_as_prime():
    with pytest.raises(ValueError):
        prime_factors(47)


def test_factors():
    result = prime_factors(86)
    assert result == [2, 43]


def test_prime_factors_task():
    result = prime_factors(3958159172)
    assert result == [2, 2, 11, 2347, 38329]