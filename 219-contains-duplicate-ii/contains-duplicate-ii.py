class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(int)
        for right in range(len(nums)):
            if hashmap[nums[right]] and right+1 - hashmap[nums[right]] <= k:
                return True
            hashmap[nums[right]] = right+1
        return False

