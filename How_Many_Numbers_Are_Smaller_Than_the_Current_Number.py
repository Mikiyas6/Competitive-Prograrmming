class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        new_array = sorted(nums)

        dictionary = {}

        lists = []

        for i in range(len(nums)):

            if new_array[i] not in dictionary:
                dictionary[new_array[i]] = i
        
        for i in range(len(nums)):

            lists.append(dictionary[nums[i]])
        
        return lists
