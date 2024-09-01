class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=list(bin(n))
        l=l[2:]
        for i in range(1,len(l)):
            if l[i-1]==l[i]:
                return False
        return True