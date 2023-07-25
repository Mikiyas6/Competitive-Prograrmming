class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        elif len(nums) == 1:
            return 1
        else:
            lists1, lists2 = [1], [1]*len(nums)
            lists3 = []
            for i in range(1,len(nums)):
                lists1.append(lists1[-1] * nums[i-1])
            for j in range(len(nums)-2,-1,-1):
                lists2[j] = (lists2[j+1] * nums[j+1])
            for k in range(len(nums)):
                lists3.append(lists1[k] * lists2[k])
            return lists3
        
        






        
        
        
        

        
        
