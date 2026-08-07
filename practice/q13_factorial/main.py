def factorial(n: int) -> int:
    if n in {0,1}:
        return 1
    else:
       return  n * factorial(n-1)

def factorial_loop(n: int) -> int:
    if n in {0,1}:
        return 1

    result = 1
    for x in range(1,n+1):
        result = x * result
    return result
      


# Test cases
# print(factorial(0))
# # 1

# print(factorial(1))
# 1

print(factorial(5))
# 120
