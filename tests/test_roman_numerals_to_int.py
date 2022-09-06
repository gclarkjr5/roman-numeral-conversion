from roman_numerals_conversion.roman_numerals import convert_roman_2_int


def test_one():
    expected = 1
    actual = convert_roman_2_int("I")

    assert expected == actual


def test_three():
    expected = 3
    actual = convert_roman_2_int("III")

    assert expected == actual


def test_four():
    expected = 4
    actual = convert_roman_2_int("IV")

    assert expected == actual


def test_nineteen():
    expected = 19
    actual = convert_roman_2_int("XIX")

    assert expected == actual


def test_fournine():
    expected = 49
    actual = convert_roman_2_int("XLIX")

    assert expected == actual


def test_onesevennine():
    expected = 179
    actual = convert_roman_2_int("CLXXIX")

    assert expected == actual


def test_twozerosixseven():
    expected = 2067
    actual = convert_roman_2_int("MMLXVII")

    assert expected == actual


def test_threeoneonenine():
    expected = 3119
    actual = convert_roman_2_int("MMMCXIX")

    assert expected == actual
