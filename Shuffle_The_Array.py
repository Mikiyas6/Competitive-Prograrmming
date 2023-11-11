class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        i = 0
        j = n 
        output = []

        while j < 2*n:

            output.append(nums[i])
            output.append(nums[j])

            i += 1
            j += 1
        
        return output
