class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = defaultdict(int)

        for index, value in enumerate(nums):

            if value in hashmap.keys():

                diff = index - hashmap[value]

                if diff <= k:

                    return True
            
            hashmap[value] = index
        
        return False
        
       
