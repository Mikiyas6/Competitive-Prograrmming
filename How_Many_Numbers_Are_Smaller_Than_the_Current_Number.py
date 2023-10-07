class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        lists = sorted(nums)

        dictionary = {}

        for i in range(len(lists)):

            if lists[i] not in dictionary.keys():
                dictionary[lists[i]] = i
            
        print(dictionary)
            
        new_list = []

        for i in range(len(nums)):
            new_list.append(dictionary[nums[i]])
        
        return new_list

        
        
