class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a,int("".join(list(map(str,b)))),1337)