class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lists = []
        for k in range(len(nums)):
            counter = 0
            for l in range(len(nums)):
                if nums[k] > nums[l]:
                    counter += 1
            lists.append(counter)
        return lists
