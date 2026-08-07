import math
def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, int(math.sqrt(n))+1):
       if n % x == 0:
           return False
    return True


# Test cases
print(is_prime(7))    # True
print(is_prime(8))    # False
print(is_prime(1))    # False
print(is_prime(2))    # True
print(is_prime(121))    # False
