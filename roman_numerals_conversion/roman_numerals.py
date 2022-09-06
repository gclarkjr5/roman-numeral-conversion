import sys


one = {"roman_numeral": "I", "numeric": 1}
five = {"roman_numeral": "V", "numeric": 5}
ten = {"roman_numeral": "X", "numeric": 10}
fifty = {"roman_numeral": "L", "numeric": 50}
one_hundred = {"roman_numeral": "C", "numeric": 100}
five_hundred = {"roman_numeral": "D", "numeric": 500}
thousand = {"roman_numeral": "M", "numeric": 1000}


# convert each numeral into its number value
def numeral_to_int(roman_numeral):
    match roman_numeral:
        case "I":
            return one["numeric"]
        case "V":
            return five["numeric"]
        case "X":
            return ten["numeric"]
        case "L":
            return fifty["numeric"]
        case "C":
            return one_hundred["numeric"]
        case "D":
            return five_hundred["numeric"]
        case "M":
            return thousand["numeric"]
        case _:
            return "Something wrong!!!"


# convert each numeral into its number value
def int_to_numeral(integer):
    match integer:
        case 1:
            return one["roman_numeral"]
        case 5:
            return five["roman_numeral"]
        case 10:
            return ten["roman_numeral"]
        case 50:
            return fifty["roman_numeral"]
        case 100:
            return one_hundred["roman_numeral"]
        case 500:
            return five_hundred["roman_numeral"]
        case 1000:
            return thousand["roman_numeral"]
        case _:
            return "Something wrong!!!"


def convert_roman_2_int(input):
    """Receives an input like a roman numeral or an arabic
    number, and converts it to the other
    """

    # split numeral into a list of letters
    numeral_split = [x for x in input]

    # convert each roman numeral into its integer/arabic form
    outputs = [numeral_to_int(x) for x in numeral_split]

    # items used for looping around list of integers
    output_length = len(outputs)
    accumulator = []
    i = 0

    while i < output_length:

        # get the current number
        number = outputs[i]

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
                next_number = outputs[i + 1]

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


def convert_int_2_roman(integer):

    # raise exception for numbers above 3999
    # numbers above 3999 use a special syntax that we will
    # ignore for now
    if int(integer) > 3999:
        sys.exit('Numbers above 3999 not allowed')

    # divide number to understand amount and remainder
    # start with the highest roman numeral digit and work down
    thousand = 0
    five_hundred = 0
    one_hundred = 0
    fifty = 0
    ten = 0
    five = 0

    # keep a remainder reference as we progress
    remainder = int(integer)

    # if atleast 1 thousand
    if int(remainder) // 1000 >= 1:

        thousand = int(remainder) // 1000

        # subtract how many thousands from the original number
        # update the higher level reference remainder
        remainder = int(remainder) - (1000 * int(thousand))

    # next weed out the five_hundreds
    if int(remainder) // 500 >= 1:

        five_hundred = int(remainder) // 500

        remainder = int(remainder) - (500 * int(five_hundred))

    # now the one_hundreds
    if int(remainder) // 100 >= 1:

        one_hundred = int(remainder) // 100

        remainder = int(remainder) - (100 * int(one_hundred))

    # now 50s
    if int(remainder) // 50 >= 1:

        fifty = int(remainder) // 50

        remainder = int(remainder) - (50 * int(fifty))

    if int(remainder) // 10 >= 1:

        ten = int(remainder) // 10

        remainder = int(remainder) - (10 * int(ten))

    if int(remainder) // 5 >= 1:

        five = int(remainder) // 5

        remainder = int(remainder) - (5 * int(five))

    # create concatenated strings of the individual roman numerals
    # i.e ['MM', 'D', '', 'L', 'XX', 'V', 'III']
    converted_string = [
        "".join([int_to_numeral(1000) for x in range(thousand)]),
        "".join([int_to_numeral(500) for x in range(five_hundred)]),
        "".join([int_to_numeral(100) for x in range(one_hundred)]),
        "".join([int_to_numeral(50) for x in range(fifty)]),
        "".join([int_to_numeral(10) for x in range(ten)]),
        "".join([int_to_numeral(5) for x in range(five)]),
        "".join([int_to_numeral(1) for x in range(remainder)]),
    ]

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
