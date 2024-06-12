class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        positions = ['.']*len(nums[0])
        
        hashmap = defaultdict(str)

        for value in nums:
            hashmap[value] = 1

        def dfs(i):

            if i == len(positions):
                if ''.join(positions) not in hashmap:
                    return True

                return False
            
            for j in range(i,len(nums[0])):

                positions[j] = '0'

                if dfs(j+1):
                    return True
                
                positions[j] = '1'

                if dfs(j+1):
                    return True
            
            return False
        
        dfs(0)
        return ''.join(positions)