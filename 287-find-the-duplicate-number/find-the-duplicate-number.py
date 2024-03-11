class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums.sort()

        i = 0
        j = i + 1

        while j < len(nums):

            if nums[i] == nums[j]:

                return nums[j]
                break
            
            i += 1
            j += 1