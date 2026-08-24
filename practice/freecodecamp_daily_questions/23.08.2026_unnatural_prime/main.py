import math
# Unnatural Prime (freeCodeCamp)
#
# Given an integer, determine if that number is a prime number or a
# negative prime number.
#
# A prime number is a positive integer greater than 1 that is only
# divisible by 1 and itself.
# A negative prime number is the negative version of a positive prime
# number.
# 1 and 0 are not considered prime numbers.
#
# Example:
# n = 7    -> True   (7 is prime)
# n = -7   -> True   (-7 is a negative prime, since 7 is prime)
# n = 8    -> False  (8 is not prime)
# n = 1    -> False
# n = 0    -> False


def is_unnatural_prime(n: int) -> bool:
     if n == 1 or n == 0 or n == -1:
          return False
     if n == 2:
          return True
     for x in range(2, int(math.sqrt(abs(n)))+1):
          if n % x == 0:
               return False

     return True     


# Test cases
print(is_unnatural_prime(7))     # True
print(is_unnatural_prime(-7))    # True
print(is_unnatural_prime(8))     # False
print(is_unnatural_prime(-8))    # False
print(is_unnatural_prime(1))     # False
print(is_unnatural_prime(-1))    # False
print(is_unnatural_prime(0))     # False
