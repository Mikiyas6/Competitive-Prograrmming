class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)//2
        
        positive_numbers = []
        negative_numbers = []

        for value in nums:

            if value > 0:

                positive_numbers.append(value)
            
            else:

                negative_numbers.append(value)
        
        i = 0
        j = 0

        output = []

        while j < n:

            output.extend([positive_numbers[i],negative_numbers[j]])

            i += 1
            j += 1
        
        return output