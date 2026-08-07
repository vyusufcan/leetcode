
class Solution:
    def isHappy(self, n: int) -> bool:
        
        c =[]
        while True :
            my_list = list(str(n))
            c.append(n)
            sum = 0
            for x in my_list:
                sum = sum + pow(int(x), 2)
            my_list = []
            n = sum
            if n == 1:
                return True
            if n in c:
                return False
         
           
            

p1 = Solution()

# Provided examples
print(p1.isHappy(2))

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false