class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0 and sum(nums[i+1:]) == 0:
                return 0
            elif sum(nums[i+1:]) == sum(nums[:i]):
                return i
            elif (i == len(nums) -1):
                if (sum(nums[:i]) == 0):
                    return i
                else:
                    return -1
    
            
