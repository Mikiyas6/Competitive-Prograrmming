class Solution:
    def countPrimes(self, n: int) -> int:
        
      visited = set()

      prime_numbers = []

      if n <= 2:

        return 0
      
      for i in range(2,n):

        if i not in visited:

          prime_numbers.append(i)

          for j in range(i**2,n,i):

            visited.add(j)
      
      return len(prime_numbers)
