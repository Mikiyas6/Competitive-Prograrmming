class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictionary = {}

        for i in range(len(nums)):
            if nums[i] not in dictionary.keys():
                dictionary[nums[i]] = 1
            else:
                dictionary[nums[i]] += 1

        maximum = 0
        for key, value in dictionary.items():
            
            if value > maximum:
                max_value = key
                maximum = value
            
        return max_value
