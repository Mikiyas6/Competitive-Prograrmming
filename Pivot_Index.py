class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        prefix_sums_forward = []
        prefix_sums_reversed = []
        lists = []
        for i in range(len(nums)):
            sums += nums[i]
            prefix_sums_forward.append(sums)
        sums = 0
        for j in range(-1,-len(nums)-1,-1):
            sums += nums[j]
            prefix_sums_reversed.append(sums)
        for k in range(len(prefix_sums_reversed)):
            lists.append(prefix_sums_reversed[-1])
            prefix_sums_reversed.pop(-1)
        prefix_sums_reversed = lists
        # print(prefix_sums_forward)
        # print(prefix_sums_reversed)
        for z in range (len(prefix_sums_forward)):
            if (prefix_sums_forward[z] == prefix_sums_reversed[z]):
                return z
        else:
            return -1
                

    
            

    
            
