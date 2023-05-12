class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        # """
        # for i in range(len(nums)-(k%len(nums))):
        #     nums.insert(len(nums)-1,nums.pop(0))
        # for i in range(k%len(nums)):
        #     nums.insert(0,nums.pop())
        for i in range(len(nums) - k%len(nums)):
            nums.append(nums.pop(0))


            


    
