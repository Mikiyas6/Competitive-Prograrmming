class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            temp = n
            total = 0
            while temp != 0:
                total += (temp % 10)**2
                temp //= 10
            if total in visited:
                return False
            visited.add(total)
            n = total
        return True