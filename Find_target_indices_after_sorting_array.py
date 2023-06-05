class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lists = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == len(nums) - i -1:
                    break
                elif (nums[j+1] < nums[j]):
                    self.swap(nums,j,j+1)
        for k in range(len(nums)):
            if nums[k] == target:
                lists.append(k)
        return lists
    def swap(self,a,x,y):
        temp = a[x]
        a[x] = a[y]
        a[y] = temp
