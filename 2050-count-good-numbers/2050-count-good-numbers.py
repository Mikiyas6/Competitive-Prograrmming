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
            
            result = fun(num,pow//2)
            final_result = result*result*(num**(pow%2))
            return final_result%MOD

        for_even_numbers = fun(5,even)
        for_prime_numbers = fun(4,odd)
        return (for_even_numbers*for_prime_numbers)%MOD


