class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(nums, k):
            count = defaultdict(int)
            left = 0
            result = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1

                result += right - left + 1

            return result

        return atMostK(nums, k) - atMostK(nums, k - 1)
        
        # hashmap = defaultdict(int)

        # l = 0

        # counter = 0

        # for r in range(len(nums)):

        #     hashmap[nums[r]] += 1
            
        #     while len(hashmap) > k:

        #         hashmap[nums[l]] -= 1

        #         if hashmap[nums[l]] == 0:

        #             del hashmap[nums[l]]
                
        #         l += 1
            
        #     if len(hashmap) == k:

        #         counter += (r-l+1) - k + 1

        # return counter