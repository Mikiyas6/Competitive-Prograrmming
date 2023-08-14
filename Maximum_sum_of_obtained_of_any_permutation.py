class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lists = [0] * (len(nums)+1)
        frequency = [0] * len(nums)
        for request in requests:
            start = request[0]
            end = request[1]
            lists[start] += 1
            lists[end+1] -= 1
        lists = lists[:len(lists)-1]
        frequency[0] = lists[0]
        for i in range(1,len(lists)):
            frequency[i] = frequency[i-1] + lists[i]
        frequency = sorted(frequency)
        nums = sorted(nums)
        total = 0
        for i in range(len(frequency)):
            total += frequency[i] * nums[i]
        return total%(10**9 + 7)
