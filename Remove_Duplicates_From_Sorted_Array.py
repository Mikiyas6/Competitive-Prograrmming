class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = i + 1
        total = 1

        while j < len(nums):

            if nums[i] != nums[j]:

                nums[i+1] = nums[j]
                i += 1
                total += 1

            j += 1

        return total

           


            


