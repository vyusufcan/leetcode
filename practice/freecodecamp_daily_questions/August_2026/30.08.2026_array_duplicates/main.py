# Array Duplicates (freeCodeCamp)
#
# Given an array of integers, return an array of integers that appear more
# than once in the initial array, sorted in ascending order. If no values
# appear more than once, return an empty array.
#
# Only include one instance of each value in the returned array.

def find_duplicates(arr):

    ud = {}
    for x in arr:
        if x in ud:
            ud[x] += 1
        else:
            ud[x] = 1

    keys = [k for k, v in ud.items() if v > 1]
    return sorted(keys)
        

print(find_duplicates([]))
print(find_duplicates([1, 2, 3, 4, 5]))

print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))