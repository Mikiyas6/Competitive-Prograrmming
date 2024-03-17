class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        n = len(nums)

        if indexDifference >= n:

            return [-1,-1]
        
        min_index, max_index = 0, 0

        pointer = 1
        
        for index in range(indexDifference,n):

            diff1 = abs(nums[index] - nums[min_index])
            diff2 = abs(nums[index] - nums[max_index])

            if diff1 >= valueDifference:

                return [min_index,index]
            
            if diff2 >= valueDifference:

                return [max_index,index]
            
            if pointer < n:

                if nums[pointer] < nums[min_index]:
            
                    min_index = pointer
                
                if nums[pointer] > nums[max_index]:

                    max_index = pointer
            
            pointer += 1
        
        return [-1,-1]


