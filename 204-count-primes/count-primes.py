class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True for _ in range(n)]
        primes[0] = False
        primes[1] = False
        i = 2

        while i * i < n :
            if primes[i]:
                j = i * i
                while j < n:
                    primes[j] = False
                    j += i
            i += 1

        return sum(primes)