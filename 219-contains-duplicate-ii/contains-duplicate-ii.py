class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap = defaultdict(int)
        # for right in range(len(nums)):
        #     if hashmap[nums[right]] and right+1 - hashmap[nums[right]] <= k:
        #         return True
        #     hashmap[nums[right]] = right+1
        # return False
        window = set()
        left = 0
        for right in range(len(nums)):
            if right-left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False

