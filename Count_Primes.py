class Solution:
    def countPrimes(self, n: int) -> int:

        prime_numbers = [True] * n

        for i in range(2,math.floor(sqrt(n))+1):

            if prime_numbers[i]:

                for j in range(i**2,n,i):

                    prime_numbers[j] = False
        
        total = 0
        
        for value in prime_numbers[2:]:

            if value:

                total += 1
        
        return total
            

