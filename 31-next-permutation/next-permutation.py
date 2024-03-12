class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        pointer = n - 2

        while pointer >= 0:

            if nums[pointer + 1] > nums[pointer]:

                break
            
            pointer -= 1
        

        if pointer < 0:

            i = 0
            j = n - 1

            while i <= j:

                nums[i], nums[j] = nums[j], nums[i]

                i += 1
                j -= 1
        else:

            value = nums[pointer]

            new_pointer = n - 1

            while new_pointer >= 0:

                if nums[new_pointer] > value:

                    nums[new_pointer],nums[pointer] = nums[pointer], nums[new_pointer]

                    break
                
                new_pointer -= 1
            
            second_part = nums[pointer+1:]

            first_part = nums[:pointer+1]

            second_part.sort()

            new_array = first_part + second_part

            for i in range(n):

                nums[i] = new_array[i]






