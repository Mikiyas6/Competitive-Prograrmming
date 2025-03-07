class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        marked = set()
        for i in range(2,right+1):
            if i not in marked:
                if i >= left:
                    primes.append(i)
                for j in range(i,right+1,i):
                    marked.add(j)
        min_diff = float("inf")
        result = []
        for j in range(1,len(primes)):
            if primes[j] - primes[j-1] < min_diff:
                min_diff = primes[j]-primes[j-1]
                result = [primes[j],primes[j-1]]
        return result[::-1] if result else [-1,-1]
