class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        map = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            map[nums[r]] += 1
            keys = list(map.keys())
            minimum = min(keys)
            maximum = max(keys)
            while maximum - minimum > 2:
                map[nums[l]] -= 1
                if map[nums[l]] == 0:
                    del map[nums[l]]
                keys = list(map.keys())
                minimum = min(keys)
                maximum = max(keys)
                l += 1
            res += r - l + 1
        return res