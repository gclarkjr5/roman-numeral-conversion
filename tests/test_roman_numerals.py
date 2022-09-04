from roman_numerals_conversion.roman_numerals import convert

def test_one():
    expected = 3
    actual = convert("III")

    assert expected == actual

# def test_three():
#     expected = 1
#     actual = convert("I")

#     assert expected == actual

# def test_four():
#     expected = 1
#     actual = convert("I")

#     assert expected == actual

# def test_nineteen():
#     expected = 1
#     actual = convert("I")

#     assert expected == actual
