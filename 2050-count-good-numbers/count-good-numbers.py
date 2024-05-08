class Solution:
    def countGoodNumbers(self, n: int) -> int:
       
        MOD = (10**9)+7

        even = (n//2) + (n%2)
        odd = n//2

        def fun(num,pow):

            if pow == 0:
                return 1
            if pow == 1:
                return num
            
            ans = fun(num,pow//2)
            ans = ans * ans

            if pow %2 == 0:
                return ans%MOD
            else:
                return (ans*num)%MOD
        
        for_even_positions = fun(5,even)
        for_odd_positions = fun(4,odd)

        return (for_even_positions * for_odd_positions)%MOD
        
        # prime = {2,3,5,7}
        # MOD = (10**9)+7
 
        # def fun(string,position):  

        #     if position == n:
        #         return 1
            
        #     counter = 0  
        #     for i in range(10):
        #         if (position %2 == 0 and i%2 == 0) or (position %2 != 0 and i in prime):
        #             string.append(i)
        #             position += 1
        #             counter += fun(string,position)
        #             string.pop()
        #             position -= 1
                
        #     return counter%MOD

        # final_answer = fun([],0)
        # return final_answer
