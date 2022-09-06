one = {"roman_numeral": "I", "numeric": 1}
five = {"roman_numeral": "V", "numeric": 5}
ten = {"roman_numeral": "X", "numeric": 10}
fifty = {"roman_numeral": "L", "numeric": 50}
one_hundred = {"roman_numeral": "C", "numeric": 100}
five_hundred = {"roman_numeral": "D", "numeric": 500}
thousand = {"roman_numeral": "M", "numeric": 1000}

options = ["roman_numeral", "numeric"]


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
    # split numeral
    numeral_split = [x for x in input]

    # convert each numeral into its integer form
    outputs = [numeral_to_int(x) for x in numeral_split]

    output_length = len(outputs)

    accumulator = []

    i = 0
    while i < output_length:
        number = outputs[i]

        # for only one roman numeral
        if output_length == 1:
            accumulator.append(number)
        else:
            # when the numeral is more than 2 digits, we need to look ahead

            # if we are on the last digit, then we cannot look ahead
            if i + 1 == output_length:
                accumulator.append(number)
            else:
                next_number = outputs[i + 1]

                # if the next numeral is bigger, then we subtract the current
                # from the next, then skip ahead
                if number < next_number:
                    sub_value = next_number - number
                    accumulator.append(sub_value)
                    i += 1
                else:  # everything else is business as usual
                    accumulator.append(number)

        i += 1

    return sum(accumulator)


def convert_int_2_roman(integer):

    # weed out the thousands, the result is the amount of thousands digits
    thousand = int(integer)//1000

    if thousand >= 1:
        integer = int(integer) - (1000 * int(thousand))

        # weed out the 500s
        five_hundred = int(integer)//500

    if five_hundred >= 1:
        integer = int(integer) - (500 * int(five_hundred))

        one_hundred = int(integer)//100

    if one_hundred >= 1:
        integer = int(integer) - (100 * int(one_hundred))

        fifty = int(integer)//50

    if fifty >= 1:
        integer = int(integer) - (50 * int(fifty))

        ten = int(integer)//10

    if ten >= 1:
        integer = int(integer) - (10 * int(ten))

        five = int(integer)//5

    if five >= 1:
        integer = int(integer) - (5 * int(five))

    print(thousand, five_hundred, one_hundred, fifty, ten, five, integer)

    return integer
