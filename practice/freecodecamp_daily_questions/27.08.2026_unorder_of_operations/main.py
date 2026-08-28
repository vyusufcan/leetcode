# Unorder of Operations (freeCodeCamp)
#
# Given an array of integers and an array of string operators, apply the
# operations to the numbers sequentially from left-to-right. Repeat the
# operations as needed until all numbers are used. Return the final result.
#
# For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of
# evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of
# operations.
#
# Valid operators are +, -, *, /, and %.

import operator
def unorder_of_operations(numbers: list, operators: list):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
    }
    counter = 0
    result = numbers[0]
    for k in numbers[1:]:

        result = ops[operators[counter]](result, k)
        counter = counter +1
        if counter == len(operators):
            counter = 0

    return int(result)


# Test cases
print(unorder_of_operations([1, 2, 3, 4, 5], ['+', '*']))
