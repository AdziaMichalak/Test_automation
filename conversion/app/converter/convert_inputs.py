import roman
from converter.utilities import *


# arabic to roman
def convert_to_roman(num):
    if int(num) != num:
        raise ValueError("Not integer")
    if not (0 < num < 4000):
        raise ValueError("number out of range (must be 1..3999)")

    result = ""
    for roman, arabic in numeral_map:
        while num >= arabic:
            result += roman
            num -= arabic
    return result


# roman to arabic
def convert_to_arabic(string):
    if string != string.upper():
        raise InputError("Input must be in Upper Cases")
    if validation_of_roman_numerals(string):
        arabic_number = roman.fromRoman(string)
        return arabic_number
    else:
        raise ValueError("invalid roman numeral")