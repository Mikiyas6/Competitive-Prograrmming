class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return 0
        
        def counting_sort(nums):

            length = max(nums) + 1
            frequency = [0] * length

            for i in range(len(nums)):
                frequency[nums[i]] += 1
            
            new_list = []
            
            for i in range(len(frequency)):

                if frequency[i]:

                    offset = frequency[i]
                    length = len(new_list)

                    new_list[length:length+offset] = [i] * offset

            return new_list

        new_list = nums
        new_list.sort()

        i = 0
        j = i + 1
        lists = []

        while j < len(new_list):

            lists.append(new_list[j]-new_list[i])
            i += 1
            j += 1
        
        min_value = max(lists)
        return min_value
