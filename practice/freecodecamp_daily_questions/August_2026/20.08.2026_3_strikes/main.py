# Given an integer n (1 <= n <= 10,000), return a count of how many
# numbers from 1 up to n have a square that contains at least one digit 3.
#
# Example:
# n = 15
# squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225
# numbers whose square contains a "3": 6 (36), 13 (169) -> count = 2


def count_squares_with_three(n: int) -> int:
    counter = 0
    for x in range(1,n+1):
        s = x ** 2
        if '3' in str(s):
            counter += 1
    return counter

# Test cases
print(count_squares_with_three(10))

print(count_squares_with_three(100))

print(count_squares_with_three(10000))
