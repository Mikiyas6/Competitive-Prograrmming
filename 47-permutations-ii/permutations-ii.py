class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashmap = Counter(nums)
        self.result = []
        self.size = len(nums)
        def dfs(hashmap,permute,length):
            if length == self.size:
                self.result.append(permute[:])
                return
            for value in hashmap:
                if hashmap[value] > 0:
                    hashmap[value] -= 1
                    dfs(hashmap,permute+[value],length+1)
                    hashmap[value] += 1
        dfs(hashmap,[],0)
        return self.result