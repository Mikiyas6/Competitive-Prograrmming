class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        lists = []

        for i in range(len(nums)):

            min_index = i

            for j in range(i+1,len(nums)):

                if nums[j] < nums[min_index]:
                    min_index = j
                
            nums[i],nums[min_index] = nums[min_index], nums[i]
            
            if nums[i] == target:
                lists.append(i)

        return lists
