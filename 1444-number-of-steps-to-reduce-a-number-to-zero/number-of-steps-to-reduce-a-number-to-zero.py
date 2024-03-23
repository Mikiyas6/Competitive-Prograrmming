class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        def fun(num,counter):

            if num == 0:

                return counter
            
            if num %2 != 0:

                num -= 1
            
            else:

                num /= 2
            
            return fun(num,counter+1)
        
        return fun(num,0)