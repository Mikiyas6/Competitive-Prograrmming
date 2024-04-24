class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        mono_queue = deque()
        result = []

        for i in range(len(nums)):
                  
            while mono_queue and mono_queue[0] < i - k + 1:
                mono_queue.popleft()

            while mono_queue and nums[i] > nums[mono_queue[-1]]:
                mono_queue.pop()

            mono_queue.append(i)

            if i >= k - 1:
                result.append(nums[mono_queue[0]])

        return result