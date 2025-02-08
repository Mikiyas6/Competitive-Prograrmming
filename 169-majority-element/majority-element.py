class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        majority_element = 0
        max_occurance = 0
        print(hashmap)
        for value in nums:
            if hashmap[value] > max_occurance:
                majority_element = value
                max_occurance = hashmap[value]
        return majority_element