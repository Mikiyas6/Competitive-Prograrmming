class Solution:
    def findLHS(self, nums: List[int]) -> int:

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        max_length = 0
        for num in freq_map:
            if num + 1 in freq_map:
                max_length = max(max_length, freq_map[num] + freq_map[num + 1])

        return max_length