

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


def convert(input):
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

                # if the next numeral is bigger, then we subtract the current from the next, then skip ahead
                if number < next_number:
                    sub_value = next_number - number
                    accumulator.append(sub_value)
                    i += 1
                else: # everything else is business as usual
                    accumulator.append(number)

        i += 1

    return sum(accumulator)
       

if __name__ == '__main__':
    convert()