class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_value = float('inf')
        max_value = 0

        for x in nums:
            min_value = min(x, min_value)
            max_value= max(x, max_value)

        return gcd(min_value,max_value)
        