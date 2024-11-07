class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        maxSum = 0
        total = sum(nums[:k])
        hashmap = Counter(nums[:k])
        if len(hashmap) == k:
            maxSum = total
        left = 0
        for right in range(k,n):
            total -= nums[left]
            total += nums[right]
            hashmap[nums[left]] -= 1
            if not hashmap[nums[left]]:
                del hashmap[nums[left]]
            hashmap[nums[right]] += 1
            if len(hashmap) == k:
                maxSum = max(maxSum,total)
            left += 1
        return maxSum 
