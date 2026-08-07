class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        if len(digits) == 1:
            return list(map(int, str(digits[0] + 1)))
        else:
            while True:
                digits[-1] = digits[-1] + 1
                if digits[-1] == 10:
                    digits[-1] = 0
                    if digits[:-1][-1] == 9:
                        digits[:-1][-1] = 0
                    print(digits)
                else:
                    return digits

            print(digits)
               






p1 = Solution()

# Provided examples
#print(p1.plusOne([9]))
print(p1.plusOne([1,2,3]))
print(p1.plusOne([2, 9, 9])) # [[1,0,0]]

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].