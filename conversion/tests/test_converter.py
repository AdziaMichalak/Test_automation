import pytest


from converter.convert_inputs import convert_to_roman, convert_to_arabic
from converter.utilities import *


# roman converter tests
test_cases = [(5, "V"), (4, "IV"), (9, "IX"), (11, "XI"), (90, "XC"), (110, "CX"), (777, "DCCLXXVII")]


def test_number_out_of_range():
    with pytest.raises(ValueError):
        convert_to_roman(5000)


def test_number_not_ingeger():
    with pytest.raises(ValueError):
        convert_to_roman("Ala Ma Kota")


@pytest.mark.parametrize("test_input,expected", test_cases)
def test_converting_to_roman(test_input, expected):
    assert convert_to_roman(test_input) == expected


# arabic converter tests


def test_if_valid_roman_num():
    with pytest.raises(ValueError):
        convert_to_arabic("MMMM")


@pytest.mark.parametrize("expected,test_input", test_cases)
def test_converting_to_arabic(test_input, expected):
    assert convert_to_arabic(test_input) == expected