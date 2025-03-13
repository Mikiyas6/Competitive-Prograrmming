class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)
        left = 0
        right = 0

        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

            right += 1

        return left

        