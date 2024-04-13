class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()

            min_deque.append(right)
            max_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len