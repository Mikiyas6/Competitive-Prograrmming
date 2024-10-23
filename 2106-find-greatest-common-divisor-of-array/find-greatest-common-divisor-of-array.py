class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi = float('inf')
        ma = 0

        for x in nums:
            mi = min(x, mi)
            ma = max(x, ma)

        return gcd(mi,ma)
        