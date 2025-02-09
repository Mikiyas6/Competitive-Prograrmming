class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        hashmap=defaultdict(int)
        cntBadPair=(n-1)*n/2
        for i in range(0, n):
            val=hashmap[nums[i]-i]
            cntBadPair-=val
            hashmap[nums[i]-i]=val+1

        return int(cntBadPair)