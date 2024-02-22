class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd = [x for x in nums if x % 2 == 1]
        even = [x for x in nums if x % 2 == 0]
        
        odd.sort()
        even.sort()
        
        result = [0] * len(nums)
        result[::2] = even
        result[1::2] = odd
        
        return result