class Solution:
    def isPalindrome(self, x: int) -> bool:
        k =  list(str(x))
        reversed = k[::-1]
        print(k,reversed)
        if x < 0:
            return False
        if k == reversed:
            return True
        return False
        
        
        
        
p1 = Solution()

# Provided examples
print(p1.isPalindrome(121))     
print(p1.isPalindrome(-121))
print(p1.isPalindrome(10))
        