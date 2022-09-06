from conversion.roman_numerals import convert


def test_one():
    expected = 1
    actual = convert("I")

    assert expected == actual


def test_three():
    expected = 3
    actual = convert("III")

    assert expected == actual


def test_four():
    expected = 4
    actual = convert("IV")

    assert expected == actual


def test_nineteen():
    expected = 19
    actual = convert("XIX")

    assert expected == actual


def test_fournine():
    expected = 49
    actual = convert("XLIX")

    assert expected == actual


def test_onesevennine():
    expected = 179
    actual = convert("CLXXIX")

    assert expected == actual


def test_twozerosixseven():
    expected = 2067
    actual = convert("MMLXVII")

    assert expected == actual


def test_threeoneonenine():
    expected = 3119
    actual = convert("MMMCXIX")

    assert expected == actual
