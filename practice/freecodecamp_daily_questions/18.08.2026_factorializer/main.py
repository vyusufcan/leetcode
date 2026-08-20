# Factorializer (freeCodeCamp)
#
# Given an integer n (0 <= n <= 20), return the factorial of that number.
# The factorial of a number is the product of all the numbers between
# 1 and the given number.
#
# The factorial of zero is 1.
#
# Example:
# n = 5
# 5 * 4 * 3 * 2 * 1 = 120


def factorialize(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorialize(n-1)


# Test cases
print(factorialize(0))
print(factorialize(1))

print(factorialize(5))

print(factorialize(20))
