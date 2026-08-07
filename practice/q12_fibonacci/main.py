def fibonacci(n: int) -> int:
    if n in {0,1}:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#Test cases
#print(fibonacci(0))
# 0

#print(fibonacci(1))
#1

print(fibonacci(6))
# 8

#print(fibonacci(15))
