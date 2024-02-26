class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def get_sum(val):
            return sum(val if x > val else x for x in arr)
        
        max_val = max(arr)
        left, right = 0, max_val
        
        while left < right:
            mid = (left + right) // 2
            total = sum(mid if x > mid else x for x in arr)
            
            if total < target:
                left = mid + 1
            else:
                right = mid
        
        if abs(get_sum(left) - target) >= abs(get_sum(left - 1) - target):
            return left - 1
        return left