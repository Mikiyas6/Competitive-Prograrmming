class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        min_length = float('inf')
        queue = deque()

        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_length = min(min_length, i - queue.popleft())
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(i)

        return min_length if min_length != float('inf') else -1



