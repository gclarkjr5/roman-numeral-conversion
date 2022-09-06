from roman_numerals_conversion.roman_numerals import convert_roman_2_int


def test_3999():
    expected = 3999
    actual = convert_roman_2_int("MMMCMXCIX")

    assert expected == actual


def test_3444():
    expected = 3444
    actual = convert_roman_2_int("MMMCDXLIV")

    assert expected == actual


def test_299():
    expected = 299
    actual = convert_roman_2_int("CCXCIX")

    assert expected == actual


def test_44():
    expected = 44
    actual = convert_roman_2_int("XLIV")

    assert expected == actual
