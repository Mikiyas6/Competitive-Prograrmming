class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        negative_nums = 0
        positive_nums = 0
        for value in hashmap:
            if value < 0:
                negative_nums += hashmap[value]
            elif value > 0:
                positive_nums += hashmap[value]
        return max(negative_nums,positive_nums)