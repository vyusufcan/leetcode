# Missing Numbers (freeCodeCamp)
#
# Given an array of integers from 1 to n, inclusive, return an array of
# all the missing integers between 1 and n (where n is the largest number
# in the given array).
#
# - The given array may be unsorted and may contain duplicates.
# - The returned array should be in ascending order.
# - If no integers are missing, return an empty array.
#
# Tests:
# 1. find_missing_numbers([1, 3, 5]) should return [2, 4]
# 2. find_missing_numbers([1, 2, 3, 4, 5]) should return []
# 3. find_missing_numbers([1, 10]) should return [2, 3, 4, 5, 6, 7, 8, 9]
# 4. find_missing_numbers([10, 1, 10, 1, 10, 1]) should return
#    [2, 3, 4, 5, 6, 7, 8, 9]
# 5. find_missing_numbers([3, 1, 4, 1, 5, 9]) should return [2, 6, 7, 8]
# 6. find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4])
#    should return [11]

def find_missing_numbers(nums):
    max_num = max(nums)

    #normal_list = [x for x in range(1,max_num+1)]

    diff = sorted(list(set(range(1,max_num+1)) - set(nums)))

    return diff


print(find_missing_numbers([1, 3, 5]))
print(find_missing_numbers([1, 2, 3, 4, 5]))
print(find_missing_numbers([1, 10]))
print(find_missing_numbers([10, 1, 10, 1, 10, 1]))
print(find_missing_numbers([3, 1, 4, 1, 5, 9]))
print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]))
