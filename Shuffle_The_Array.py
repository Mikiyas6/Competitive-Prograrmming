class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        i = 0
        j = n

        output = []

        while j < len(nums):

            output.extend([nums[i],nums[j]])
        
            i += 1

            j += 1
        
        return output
