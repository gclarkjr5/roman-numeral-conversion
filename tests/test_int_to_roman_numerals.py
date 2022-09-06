import pytest
from roman_numerals_conversion.roman_numerals import convert_int_2_roman


def test_above_3999():
    with pytest.raises(SystemExit):
        assert convert_int_2_roman(4000)


def test_3999():
    expected = "MMMCMXCIX"
    actual = convert_int_2_roman(3999)

    assert expected == actual


def test_3444():
    expected = "MMMCDXLIV"
    actual = convert_int_2_roman(3444)

    assert expected == actual


def test_299():
    expected = "CCXCIX"
    actual = convert_int_2_roman(299)

    assert expected == actual


def test_44():
    expected = "XLIV"
    actual = convert_int_2_roman(44)

    assert expected == actual
