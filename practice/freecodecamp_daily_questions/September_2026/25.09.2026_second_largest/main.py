# 2nd Largest
# Given an array, return the second largest distinct number.




def second_largest(arr):
    k = sorted(list(set(arr)))
    k.reverse()
    return k[1]






print(second_largest([1, 2, 3, 4])) #3

print(second_largest([10, -17, 55.5, 44, 91, 0])) #55.5
