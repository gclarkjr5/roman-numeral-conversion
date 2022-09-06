from roman_numerals_conversion.roman_numerals import convert_int_2_roman

# tests: 1000, 1020, 1500, 1505
def test_thousand():
    expected = "M"
    actual = convert_int_2_roman(1000)

    assert expected == actual
