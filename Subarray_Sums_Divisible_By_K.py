class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        cumulative = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0

        for value in nums:

            cumulative += value
            modulus = cumulative % k

            if modulus in hashmap:

                count += hashmap[modulus]
            
            hashmap[modulus] += 1
        
        return count




# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
#         curr_sum = 0
#         res = 0
#         prefix_sum = {0:1}

#         for i in range(len(nums)):

#             curr_sum += nums[i]
#             remainder = curr_sum % k

#             res += prefix_sum.get(remainder,0)
#             prefix_sum[remainder] = 1 + prefix_sum.get(remainder,0)
        
#         return res
