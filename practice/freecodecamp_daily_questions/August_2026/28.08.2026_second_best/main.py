# Second Best (freeCodeCamp)
#
# Given an array of integers representing the price of different laptops,
# and an integer representing your budget, return:
#
# The second most expensive laptop if it is within your budget, or
# The most expensive laptop that is within your budget, or
# 0 if no laptops are within your budget.
#
# Duplicate prices should be ignored.

def second_best(laptops: list, budget: int):

    if len(sorted(list(set(laptops)))[::-1]) == 0:
        return 0
    if len(sorted(list(set(laptops)))[::-1]) == 1:
        if budget >= sorted(list(set(laptops)))[::-1][0]:
            return sorted(list(set(laptops)))[::-1][0]
        else:
            return 0
    second_best = sorted(list(set(laptops)))[::-1][1]
    if budget >= second_best:
        return second_best
    else:
        for x in sorted(list(set(laptops)))[::-1]:
            if budget >= x:
                return x
        return 0




# Test cases
print(second_best([500, 500, 500], 600))
print(second_best([500, 500, 500], 400))
print(second_best([500, 700, 1000, 700, 300], 800))
print(second_best([1500, 2000, 1800, 1400], 1900))
print(second_best([1500, 2000, 2000, 1800, 1400], 1900))
print(second_best([2099, 1599, 1899, 1499], 2200))
print(second_best([2099, 1599, 1899, 1499], 1000))
print(second_best([1200, 1500, 1600, 1800, 1400, 2000], 1450))
