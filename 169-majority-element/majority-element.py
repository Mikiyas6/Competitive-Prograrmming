class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = Counter(nums)
        hashset = set(nums)
        max_length = 1
        answer = nums[0]
        for value in hashset:
            if hashmap[value] > n//2 and hashmap[value] > max_length:
                max_length = hashmap[value]
                answer = value
        return answer
