class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        import itertools
        all_combinations = itertools.combinations(nums,2)
        result = 0
        for x,y in all_combinations:
            if x + y < target:
                result += 1
        return result
        