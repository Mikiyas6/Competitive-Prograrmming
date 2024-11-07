class Solution:
    def xorAllNums(self, a: List[int], b: List[int]) -> int:
        return reduce(xor, a * (len(b) & 1) + b * (len(a) & 1), 0)