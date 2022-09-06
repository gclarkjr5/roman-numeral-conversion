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
