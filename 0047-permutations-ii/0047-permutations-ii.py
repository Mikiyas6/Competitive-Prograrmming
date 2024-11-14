class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashmap = Counter(nums)
        result = []
        visited = set()

        def backtrack(localHashmap,path):

            if len(path) == len(nums):
                if tuple(path) not in visited:
                    visited.add(tuple(path))
                    result.append(path[:])
                return

            for num in nums:
                if localHashmap[num] < hashmap[num]:
                    localHashmap[num] += 1
                    path.append(num)
                    backtrack(localHashmap,path)
                    path.pop()
                    localHashmap[num] -= 1
        
        backtrack(defaultdict(int),[])
        return result
            