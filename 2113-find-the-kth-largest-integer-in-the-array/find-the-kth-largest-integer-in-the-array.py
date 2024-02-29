class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        integer_nums = [int(string) for string in nums]

        integer_nums.sort()

        integer_nums = integer_nums[::-1]

        return str(integer_nums[k-1])