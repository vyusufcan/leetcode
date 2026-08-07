class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        my_list = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 ==0:
                #print("FizzBuzz")
                my_list.append("FizzBuzz")
            elif x % 5 == 0:
                #print("Fizz")
                my_list.append("Buzz")
            elif x % 3 == 0:
                #print("Buzz")
                my_list.append("Fizz")
            else:
                #print(x)
                my_list.append(str(x))
        
        return my_list


p1 = Solution()

# Provided examples
print(p1.fizzBuzz(16))
