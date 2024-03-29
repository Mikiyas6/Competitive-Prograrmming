class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        left = 0
        count = 0
        max_num = max(nums)
        max_count = 0

        for right in range(n):
            if nums[right] == max_num:
                max_count += 1

            while max_count >= k:
                count += n - right
                if nums[left] == max_num:
                    max_count -= 1
                left += 1

        return count
                                