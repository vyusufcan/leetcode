class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
       for x in range(len(nums)):
           if val in nums:
               nums.remove(val)
       return len(nums)

p1 = Solution()

# Provided examples
print(p1.removeElement([3,2,2,3],3))
