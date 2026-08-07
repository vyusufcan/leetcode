class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {'I': 1, 'V': 5, 'X': 10, "L":50, "C":100, "D":500 , "M":1000}
        x = list(s)
        sum = 0
        for k in range(len(x) - 1):  # ✅ son elemanda durur
            if symbols[x[k]] < symbols[x[k+1]]:
                sum -= symbols[x[k]]
            else:
                sum += symbols[x[k]]

        sum += symbols[x[-1]]  # son elemanı ayrıca ekle

        return sum
            
        
        
        
        
        
        
        
p1 = Solution()

# Provided examples
print(p1.romanToInt("IIIV"))




        