class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dictionary = {}

        for i in range(len(nums)):

            if nums[i] in dictionary:

                first_index = dictionary[nums[i]]

                if abs(first_index-i) <= k:
                    return True

            dictionary[nums[i]] = i
        
        return False
