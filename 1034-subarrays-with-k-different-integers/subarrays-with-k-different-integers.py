class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def at_most_k(nums: List[int], k: int) -> int:

            hashmap = defaultdict(int)

            counter = 0

            l = 0

            for r in range(len(nums)):

                if hashmap[nums[r]] == 0:

                    k -= 1
                
                hashmap[nums[r]] += 1

                while k < 0:

                    hashmap[nums[l]] -= 1

                    if hashmap[nums[l]] == 0:

                        k += 1
                    
                    l += 1
                
                counter += r - l + 1
            
            return counter
        
        return at_most_k(nums,k) - at_most_k(nums,k-1)
