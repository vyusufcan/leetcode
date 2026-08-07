class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        
        my = {}       
        for x in nums:
            sum = 1
            if my.get(x):
                sum += sum
                my[x] = sum
            else:
                my[x] = sum

        for key,val in my.items():
            if val == 1:
                return key
            
            
            
        


        
p1 = Solution()

# Provided examples
print(p1.singleNumber([2,2,1]))
print(p1.singleNumber([4,1,2,1,2]))
print(p1.singleNumber([1, 1, 1, 2]))


# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1