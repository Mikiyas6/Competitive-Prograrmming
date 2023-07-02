class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        lists = []
        for i in range(len(nums)):
            if nums[i] == target:
                lists.append(i)
        return lists
