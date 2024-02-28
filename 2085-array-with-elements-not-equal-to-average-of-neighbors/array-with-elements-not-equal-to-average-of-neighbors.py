class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        rearranged = [0] * n
        i, j = 0, n - 1
        for k in range(n):
            if k % 2 == 0:
                rearranged[k] = nums[i]
                i += 1
            else:
                rearranged[k] = nums[j]
                j -= 1
        return rearranged