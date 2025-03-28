class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_nums = list(range(1,n+1))
        hashset = set(nums)
        result = [value for value in full_nums if value not in hashset]
        return result
