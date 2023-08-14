class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictionary = {}
        total = 0
        counter = 0
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                counter += 1
            if (total - k) in dictionary.keys():
                counter += dictionary[total-k]
            if total in dictionary:
                dictionary[total] += 1
            else:
                dictionary[total] = 1
        return counter
