# Given a positive integer n (1 <= n <= 1,000), return the sum of all
# the integers squared from 1 up to n.
#
# Example:
# n = 3
# 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14


def sum_of_squares(n: int) -> int:
    counter = 0
    for x in range(1, n+1):
        counter  = counter + (x ** 2)
    return counter



# Test cases
print(sum_of_squares(3))

print(sum_of_squares(10))

print(sum_of_squares(1000))
