class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        longest = 0
        hashmap = defaultdict(int)
        cumulative = 0
        length = 0

        for index,value in enumerate(nums):

            if value == 0:

                nums[index] = -1

        for index,value in enumerate(nums):

            cumulative += value

            if cumulative == 0:

                length = index + 1

            elif cumulative in hashmap:

                length = index-hashmap[cumulative]
            
            longest = max(longest,length)
            
            if cumulative not in hashmap:
            
                hashmap[cumulative] = index
        
        return longest


