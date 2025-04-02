class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set([0])
        while n != 1:
            temp = n
            total = 0
            while temp != 0:
                total +=  (temp%10)**2
                temp //= 10
            if total in hashset:
                return False
            n = total
            hashset.add(total)
        return True