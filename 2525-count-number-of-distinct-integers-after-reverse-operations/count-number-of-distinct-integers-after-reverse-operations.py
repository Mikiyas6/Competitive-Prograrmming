class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def reverseInteger(n):
            return int(str(n)[::-1])

        distinct_set = set()
        for num in nums:
            distinct_set.add(num)
            distinct_set.add(reverseInteger(num))
        return len(distinct_set)