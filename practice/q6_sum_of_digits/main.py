def sum_of_digits(n: int) -> int:
    
    count = 0 
    for x in str(n):
        count += int(x)
    return count

sum_of_digits(1000)
