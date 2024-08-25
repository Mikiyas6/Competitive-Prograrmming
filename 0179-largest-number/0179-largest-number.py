class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x, y):
            return int(y + x) - int(x + y)
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums_str)
        return largest_num if largest_num[0] != '0' else '0'
