class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_indicator = 0
        queue = []
        
        for i in range(n):
            # Remove indices from the queue that are out of the window
            if queue and queue[0] == i - k:
                queue.pop(0)
                flip_indicator ^= 1  # Toggle flip indicator
                
            # If the current element needs to be flipped
            if (nums[i] == 0 and flip_indicator % 2 == 0) or (nums[i] == 1 and flip_indicator % 2 == 1):
                if i + k > n:
                    return -1
                flips += 1
                flip_indicator ^= 1  # Toggle flip indicator
                queue.append(i)
        
        return flips