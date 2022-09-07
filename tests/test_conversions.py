import pytest
from roman_numerals_conversion.roman_numerals import (
    convert_int_2_roman,
    convert_roman_2_int,
)

test_fixtures = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (11, "XI"),
    (22, "XXII"),
    (33, "XXXIII"),
    (44, "XLIV"),
    (55, "LV"),
    (66, "LXVI"),
    (77, "LXXVII"),
    (88, "LXXXVIII"),
    (99, "XCIX"),
    (299, "CCXCIX"),
    (1224, "MCCXXIV"),
    (3444, "MMMCDXLIV"),
    (3999, "MMMCMXCIX"),
]


@pytest.mark.parametrize("number, roman", test_fixtures)
def test_numeral_to_roman(number, roman):
    assert convert_int_2_roman(number) == roman


@pytest.mark.parametrize("number, roman", test_fixtures)
def test_roman_to_number(number, roman):
    assert convert_roman_2_int(roman) == number


@pytest.mark.parametrize("number", [-1, 4000])
def test_numeral_to_roman_unhappy(number):
    with pytest.raises(ValueError):
        convert_int_2_roman(number)
