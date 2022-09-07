from roman_numerals_conversion.conversions import CONVERSIONS


def get_key_from_value(value):
    list_of_keys = list(CONVERSIONS.keys())
    list_of_values = list(CONVERSIONS.values())
    value_index = list_of_values.index(value)

    return list_of_keys[value_index]


def create_roman_numeral_string(integer, digit):
    roman_numeral_list = [get_key_from_value(integer) for x in range(digit)]
    return "".join(roman_numeral_list)


def convert_roman_2_int(roman_numeral):
    """Receives an input like a roman numeral or an arabic
    number (integer), and converts it to the other
    """

    # split numeral into a list of letters
    numeral_split = [x for x in roman_numeral]

    # convert each roman numeral into its integer/arabic form
    integer_split = [CONVERSIONS[x] for x in numeral_split]

    # # items used for looping around list of integers
    output_length = len(integer_split)
    accumulator = []
    i = 0

    while i < output_length:

        # get the current number
        number = integer_split[i]

        # if only one roman numeral is present
        if output_length == 1:
            accumulator.append(number)
        else:
            # when roman numeral is larger, we have some special
            # rules to follow
            # 1. While reading from left to right, we need to know
            #    the next number in line
            # 2. We cannot look ahead of the last digit because there is
            #    nothing else
            # 3. If the next number is bigger, we need to subtract the current
            #    number from the bigger number to get our result
            # 4. If we have to subtract, then we use up 2 digits, so
            #    after evaluation, we need to skip to the following digit
            #    (i.e after next)
            # 5. If the next number is not bigger, we treat it normally
            #    by adding it

            # Rule 2: if we are on the last digit, then we cannot look ahead
            if i + 1 == output_length:
                accumulator.append(number)
            else:

                # Rule 1: get the next number in the list
                next_number = integer_split[i + 1]

                # Rule 3: when next number is bigger, subtract current from it
                if number < next_number:
                    sub_value = next_number - number
                    accumulator.append(sub_value)

                    # Rule 4: due to subtraction, we need to skip a digit
                    i += 1

                # Rule 5: when next is not bigger, add it normally
                else:
                    accumulator.append(number)

        i += 1

    return sum(accumulator)


def convert_int_2_roman(intg):

    integer = int(intg)

    # raise exception for numbers above 3999 or below 1
    # numbers above 3999 use a special syntax that we will
    # ignore for now
    if integer > 3999:
        raise ValueError("Numbdes above 3999 not allowed")
        # raisys.exit('Numbers above 3999 not allowed')

    if integer < 1:
        raise ValueError("Numbdes below 1 not allowed")

    # divide number to understand amount and remainder
    # start with the highest roman numeral digit and work down
    thousand = 0
    five_hundred = 0
    one_hundred = 0
    fifty = 0
    ten = 0
    five = 0

    # keep a remainder reference as we progress
    remainder = integer

    # if atleast 1 thousand
    if remainder // 1000 >= 1:

        thousand = remainder // 1000

        # subtract how many thousands from the original number
        # update the higher level reference remainder
        remainder = remainder - (1000 * int(thousand))

    # next weed out the five_hundreds
    if remainder // 500 >= 1:

        five_hundred = remainder // 500

        remainder = remainder - (500 * int(five_hundred))

    # now the one_hundreds
    if remainder // 100 >= 1:

        one_hundred = remainder // 100

        remainder = remainder - (100 * int(one_hundred))

    # now 50s
    if remainder // 50 >= 1:

        fifty = remainder // 50

        remainder = remainder - (50 * int(fifty))

    if remainder // 10 >= 1:

        ten = remainder // 10

        remainder = remainder - (10 * int(ten))

    if remainder // 5 >= 1:

        five = remainder // 5

        remainder = remainder - (5 * int(five))

    # create concatenated strings of the individual roman numerals
    # i.e ['MM', 'D', '', 'L', 'XX', 'V', 'III']
    i_list = [
        (CONVERSIONS["M"], thousand),
        (CONVERSIONS["D"], five_hundred),
        (CONVERSIONS["C"], one_hundred),
        (CONVERSIONS["L"], fifty),
        (CONVERSIONS["X"], ten),
        (CONVERSIONS["V"], five),
        (CONVERSIONS["I"], remainder),
    ]

    converted_string = [create_roman_numeral_string(x, y) for x, y in i_list]

    # Rule: You cannot have more than 3 consecuitve of the same roman numeral
    # i.e: 3 == III, but 4 == IV and NOT IIII
    # another example: 8 == VIII, but 9 == IX and not VIIII
    # this behavior seems to only happen if a digit is a 4 or a 9
    # in the hundreds, tens, or ones digits
    # the below is meant to handle this

    # if one_hundred occurs 4x and five_hundred 1x or 0x -> CM or CD
    if (one_hundred == 4) & (five_hundred == 1):
        converted_string[1] = "C"
        converted_string[2] = "M"

    if (one_hundred == 4) & (five_hundred == 0):
        converted_string[1] = "C"
        converted_string[2] = "D"

    # if ten occurs 4x and fifty 1x or 0x -> XC or XL
    if (ten == 4) & (fifty == 1):
        converted_string[3] = "X"
        converted_string[4] = "C"

    if (ten == 4) & (fifty == 0):
        converted_string[3] = "X"
        converted_string[4] = "L"

    # if remainder occurs 4x and five 1x or 0x -> IX or IV
    if (remainder == 4) & (five == 1):
        converted_string[5] = "I"
        converted_string[6] = "X"

    if (remainder == 4) & (five == 0):
        converted_string[5] = "I"
        converted_string[6] = "V"

    # print(converted_string)
    final_string = "".join(converted_string)

    return final_string
