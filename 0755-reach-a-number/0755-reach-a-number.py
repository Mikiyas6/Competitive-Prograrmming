class Solution:
    def reachNumber(self, target: int) -> int:
      target = abs(target)
      n = (((1 + 8 * target)**(1/2) - 1) / 2) // 1
      n = ceil((((1 + 8 * target)**(1/2) - 1) / 2))

      total = n * (n + 1) / 2
      reste = total - target
      if reste % 2 == 0:
          return int(n)

      if n % 2 == 0:
          supp = 1
      else:
          supp = 2

      return int(n + supp)