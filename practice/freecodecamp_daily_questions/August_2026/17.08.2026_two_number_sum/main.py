# Two Number Sum (freeCodeCamp)
#
# Given an array of numbers and an integer target, find two unique
# numbers in the array that add up to the target value. Return an
# array with the indices of those two numbers, or "Target not found"
# if no two numbers sum up to the target.
#
# The returned array should have the indices in ascending order.
#
# Example:
# nums = [2, 7, 11, 15], target = 9
# nums[0] + nums[1] = 9 -> [0, 1]


def two_number_sum(nums, target):
    for x in nums:
        print(x)
        for k in nums:
            print(k)

    pass

# Test cases
print(two_number_sum([2, 7, 11, 15], 9))
# print(two_number_sum([3, 2, 4], 6))
# print(two_number_sum([1, 2, 3], 100))
