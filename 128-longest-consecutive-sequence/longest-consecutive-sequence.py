class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = []
        nums = list(set(nums))
        heapify(nums)
        for i in range(len(nums)):
            result.append(heappop(nums))
        max_length = 1
        i = 0
        j = 1
        length = 1
        while j < len(result):
            if result[j]-result[i] != 1:
                length = 1
            else:
                length += 1
                max_length = max(max_length,length)
            i += 1
            j += 1
        return max_length
        