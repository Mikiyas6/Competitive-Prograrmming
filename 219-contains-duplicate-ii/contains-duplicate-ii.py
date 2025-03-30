class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)
        for index,value in enumerate(nums):
            hashmap[value].append(index)
        for value in hashmap:
            if len(hashmap[value]) > 1:
                for index in range(1,len(hashmap[value])):
                    if hashmap[value][index] - hashmap[value][index-1] <= k:
                        return True
        return False