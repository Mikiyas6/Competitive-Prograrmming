class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counter = 0

        hashmap = defaultdict(int)

        hashmap[0] = 1

        total = 0

        for value in nums:

            total += value

            Mod = total % k

            if Mod in hashmap:

                counter += hashmap[Mod]
            
            hashmap[Mod] += 1
        
        return counter