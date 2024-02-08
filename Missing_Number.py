class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        another_nums = list(range(n+1))

        set_nums = set(nums)
        set_another_nums = set(another_nums)

        missing_number = (list(set_another_nums - set_nums)[0])

        return missing_number
